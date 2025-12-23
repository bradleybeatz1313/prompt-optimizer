#!/usr/bin/env python3
"""
Evaluation framework for the Prompt Optimizer.

Runs test cases through the scoring engine and generates
pass/fail reports with detailed analysis.
"""

import json
import sys
from pathlib import Path
from typing import List, Dict

sys.path.insert(0, str(Path(__file__).parent.parent / "benchmarks"))
from scoring import PromptScorer, ScoreCard


class EvalRunner:
    """Run evaluation test cases and report results."""

    def __init__(self):
        self.scorer = PromptScorer()
        self.results = []

    def load_test_cases(self, path: str = "test_cases.json") -> List[Dict]:
        with open(path) as f:
            return json.load(f).get("cases", [])

    def evaluate(self, cases: List[Dict]) -> Dict:
        passed = 0
        failed = 0
        details = []

        for case in cases:
            score = self.scorer.score_prompt(
                original=case["prompt"],
                expected_techniques=case.get("expected_techniques", []),
                complexity=case.get("complexity", "medium"),
            )

            threshold = case.get("min_score", 0.5)
            pass_fail = score.overall >= threshold

            if pass_fail:
                passed += 1
            else:
                failed += 1

            details.append({
                "id": case["id"],
                "passed": pass_fail,
                "score": score.overall,
                "threshold": threshold,
                "clarity": score.clarity,
                "specificity": score.specificity,
            })

        return {
            "total": len(cases),
            "passed": passed,
            "failed": failed,
            "pass_rate": round(passed / max(len(cases), 1), 3),
            "details": details,
        }

    def print_report(self, results: Dict):
        print(f"\n{'='*50}")
        print(f"EVAL RESULTS: {results['passed']}/{results['total']} passed ({results['pass_rate']:.0%})")
        print(f"{'='*50}")

        for d in results["details"]:
            status = "✅" if d["passed"] else "❌"
            print(f"  {status} {d['id']:20s} score={d['score']:.3f} (min={d['threshold']})")


if __name__ == "__main__":
    runner = EvalRunner()
    cases = runner.load_test_cases(
        str(Path(__file__).parent / "test_cases.json")
    )
    results = runner.evaluate(cases)
    runner.print_report(results)
