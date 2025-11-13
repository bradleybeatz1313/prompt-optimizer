#!/usr/bin/env python3
"""
Prompt scoring engine for the benchmark suite.

Evaluates prompts across multiple quality dimensions without
requiring actual LLM API calls — uses heuristic analysis.
"""

import re
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ScoreCard:
    """Quality scores for a single prompt evaluation."""
    clarity: float = 0.0        # 0-1: How unambiguous is the prompt?
    specificity: float = 0.0    # 0-1: How specific are the instructions?
    structure: float = 0.0      # 0-1: Is the prompt well-organized?
    technique_coverage: float = 0.0  # 0-1: Were expected techniques applied?
    conciseness: float = 0.0    # 0-1: Is it specific without being wordy?
    positive_framing: float = 0.0    # 0-1: Positive instructions vs constraints?
    overall: float = 0.0        # Weighted average


POWER_VERBS = {
    "act", "analyze", "categorize", "classify", "contrast", "compare",
    "create", "describe", "define", "evaluate", "extract", "find",
    "generate", "identify", "list", "measure", "organize", "parse",
    "pick", "predict", "provide", "rank", "recommend", "return",
    "retrieve", "rewrite", "select", "show", "sort", "summarize",
    "translate", "write", "build", "design", "implement", "debug",
    "refactor", "optimize", "assess", "detect", "group", "explain",
}

WEAK_VERBS = {
    "think", "help", "look", "try", "maybe", "consider", "check",
    "do", "make", "get", "put", "take", "give", "use",
}

NEGATIVE_PATTERNS = [
    r"\bdon'?t\b", r"\bdo not\b", r"\bnever\b", r"\bavoid\b",
    r"\brefrain\b", r"\bwithout\b",
]

STRUCTURAL_MARKERS = [
    r"<\w+>", r"```", r"---", r"\|.*\|", r"^\d+\.",
    r"^[-*]", r"#{1,3}\s",
]


class PromptScorer:
    """Heuristic prompt quality scorer."""

    def score_prompt(
        self,
        original: str,
        expected_techniques: Optional[List[str]] = None,
        complexity: str = "medium",
    ) -> ScoreCard:
        """Score a prompt across quality dimensions."""

        card = ScoreCard()
        words = original.lower().split()
        word_count = len(words)

        # Clarity: length, question marks, specific nouns
        card.clarity = self._score_clarity(original, words, word_count)

        # Specificity: numbers, formats, constraints mentioned
        card.specificity = self._score_specificity(original, words)

        # Structure: delimiters, sections, formatting
        card.structure = self._score_structure(original)

        # Technique coverage
        if expected_techniques:
            card.technique_coverage = self._score_technique_coverage(
                original, expected_techniques
            )

        # Conciseness: power verbs vs weak verbs, filler ratio
        card.conciseness = self._score_conciseness(original, words)

        # Positive framing: instructions vs constraints
        card.positive_framing = self._score_positive_framing(original)

        # Weighted overall
        weights = {
            "clarity": 0.25,
            "specificity": 0.20,
            "structure": 0.15,
            "technique_coverage": 0.15,
            "conciseness": 0.15,
            "positive_framing": 0.10,
        }

        card.overall = round(sum(
            getattr(card, k) * v for k, v in weights.items()
        ), 3)

        return card

    def _score_clarity(self, text: str, words: list, word_count: int) -> float:
        score = 0.5  # baseline

        # Longer prompts tend to be clearer (up to a point)
        if 20 <= word_count <= 200:
            score += 0.2
        elif word_count > 200:
            score += 0.1

        # Contains specific output format mention
        format_words = {"json", "table", "list", "markdown", "csv", "xml", "yaml"}
        if format_words & set(words):
            score += 0.15

        # Contains audience/persona mention
        audience_words = {"audience", "reader", "user", "developer", "beginner", "expert"}
        if audience_words & set(words):
            score += 0.15

        return min(round(score, 3), 1.0)

    def _score_specificity(self, text: str, words: list) -> float:
        score = 0.3

        # Numbers indicate specificity
        numbers = re.findall(r'\d+', text)
        score += min(len(numbers) * 0.1, 0.3)

        # Specific format requests
        if any(w in words for w in ["format", "structure", "schema", "template"]):
            score += 0.15

        # Length/count constraints
        if any(w in words for w in ["words", "sentences", "paragraphs", "lines", "items"]):
            score += 0.15

        # Specific tools/technologies mentioned
        if re.search(r'[A-Z][a-z]+(?:[A-Z][a-z]+)+|[A-Z]{2,}', text):
            score += 0.1

        return min(round(score, 3), 1.0)

    def _score_structure(self, text: str) -> float:
        score = 0.2

        for pattern in STRUCTURAL_MARKERS:
            if re.search(pattern, text, re.MULTILINE):
                score += 0.12

        # Multiple paragraphs
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        if len(paragraphs) >= 2:
            score += 0.1

        return min(round(score, 3), 1.0)

    def _score_technique_coverage(self, text: str, expected: List[str]) -> float:
        if not expected:
            return 1.0

        text_lower = text.lower()
        found = 0
        for technique in expected:
            keywords = technique.lower().replace("_", " ").replace("-", " ").split()
            if any(kw in text_lower for kw in keywords):
                found += 1

        return round(found / len(expected), 3)

    def _score_conciseness(self, text: str, words: list) -> float:
        word_set = set(words)

        power_count = len(word_set & POWER_VERBS)
        weak_count = len(word_set & WEAK_VERBS)

        total_verbs = power_count + weak_count
        if total_verbs == 0:
            return 0.5

        ratio = power_count / total_verbs
        return round(0.3 + ratio * 0.7, 3)

    def _score_positive_framing(self, text: str) -> float:
        negative_count = sum(
            len(re.findall(p, text, re.IGNORECASE))
            for p in NEGATIVE_PATTERNS
        )

        sentences = text.count(".") + text.count("!") + text.count("?") + 1
        neg_ratio = negative_count / max(sentences, 1)

        # Lower negative ratio = higher score
        return round(max(0, 1.0 - neg_ratio * 2), 3)
