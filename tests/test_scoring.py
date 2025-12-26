#!/usr/bin/env python3
"""Unit tests for the prompt scoring engine."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "benchmarks"))
from scoring import PromptScorer, ScoreCard


class TestPromptScorer(unittest.TestCase):
    def setUp(self):
        self.scorer = PromptScorer()

    def test_vague_prompt_scores_low(self):
        score = self.scorer.score_prompt("help me with something")
        self.assertLess(score.overall, 0.5)

    def test_specific_prompt_scores_higher(self):
        prompt = ("Analyze the Q4 2025 revenue data by product line. "
                  "Return a JSON table with columns: product, revenue, "
                  "growth_pct. Sort by growth descending.")
        score = self.scorer.score_prompt(prompt)
        self.assertGreater(score.overall, 0.5)

    def test_power_verbs_improve_conciseness(self):
        weak = "think about summarizing this document for me"
        strong = "summarize this document in 3 bullet points"
        weak_score = self.scorer.score_prompt(weak)
        strong_score = self.scorer.score_prompt(strong)
        self.assertGreater(strong_score.conciseness, weak_score.conciseness)

    def test_negative_framing_lowers_score(self):
        negative = "Don't use jargon. Don't be verbose. Never include examples."
        positive = "Write in plain language at a 10th-grade level. Be concise."
        neg_score = self.scorer.score_prompt(negative)
        pos_score = self.scorer.score_prompt(positive)
        self.assertGreater(pos_score.positive_framing, neg_score.positive_framing)

    def test_structured_prompt_scores_high_structure(self):
        prompt = """<role>Senior developer</role>
<context>Python web app using Flask</context>
<instruction>Review this code for security issues</instruction>"""
        score = self.scorer.score_prompt(prompt)
        self.assertGreater(score.structure, 0.3)

    def test_technique_coverage(self):
        prompt = "analyze step by step using chain of thought reasoning"
        score = self.scorer.score_prompt(
            prompt, expected_techniques=["chain_of_thought", "analysis"]
        )
        self.assertGreater(score.technique_coverage, 0.3)

    def test_empty_prompt(self):
        score = self.scorer.score_prompt("")
        self.assertLessEqual(score.overall, 0.5)

    def test_scorecard_has_all_fields(self):
        score = self.scorer.score_prompt("test prompt")
        self.assertIsInstance(score.clarity, float)
        self.assertIsInstance(score.specificity, float)
        self.assertIsInstance(score.structure, float)
        self.assertIsInstance(score.conciseness, float)
        self.assertIsInstance(score.positive_framing, float)
        self.assertIsInstance(score.overall, float)


if __name__ == "__main__":
    unittest.main(verbosity=2)
