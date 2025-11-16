#!/usr/bin/env python3
"""
Prompt Optimizer Benchmark Runner

Evaluates prompt optimization quality by comparing original vs optimized
prompts across multiple dimensions: clarity, specificity, technique
application, and estimated output quality improvement.

Usage:
    python benchmark_runner.py --dataset datasets/code_prompts.json --output results/
    python benchmark_runner.py --dataset datasets/writing_prompts.json --verbose
    python benchmark_runner.py --all  # Run all datasets
"""

import os
import sys
import json
import time
import argparse
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field, asdict

from scoring import PromptScorer, ScoreCard


@dataclass
class BenchmarkCase:
    """Single benchmark test case."""
    id: str
    category: str
    original_prompt: str
    expected_techniques: List[str]
    complexity: str  # "light", "medium", "heavy"
    description: str = ""
    optimized_prompt: Optional[str] = None
    score: Optional[dict] = None


@dataclass
class BenchmarkResult:
    """Results from a benchmark run."""
    run_id: str
    dataset: str
    version: str
    timestamp: str
    total_cases: int
    scores: Dict[str, float]
    per_case: List[dict]
    duration_seconds: float
    config: dict = field(default_factory=dict)


class BenchmarkRunner:
    """Execute benchmark suites against prompt optimization rules."""

    def __init__(self, config: Optional[dict] = None):
        self.config = config or {}
        self.scorer = PromptScorer()
        self.results: List[BenchmarkResult] = []

    def load_dataset(self, path: str) -> List[BenchmarkCase]:
        """Load a benchmark dataset from JSON."""
        with open(path) as f:
            data = json.load(f)

        cases = []
        for item in data.get("cases", []):
            cases.append(BenchmarkCase(
                id=item["id"],
                category=item.get("category", "general"),
                original_prompt=item["original_prompt"],
                expected_techniques=item.get("expected_techniques", []),
                complexity=item.get("complexity", "medium"),
                description=item.get("description", ""),
            ))

        return cases

    def evaluate_case(self, case: BenchmarkCase) -> ScoreCard:
        """Evaluate a single benchmark case.

        Scores the original prompt on optimization dimensions and
        checks whether the expected techniques would be triggered.
        """
        score = self.scorer.score_prompt(
            original=case.original_prompt,
            expected_techniques=case.expected_techniques,
            complexity=case.complexity,
        )
        return score

    def run_dataset(self, dataset_path: str) -> BenchmarkResult:
        """Run a full benchmark dataset."""
        cases = self.load_dataset(dataset_path)
        dataset_name = Path(dataset_path).stem

        start_time = time.time()
        per_case_results = []

        for case in cases:
            score = self.evaluate_case(case)
            case.score = asdict(score)

            per_case_results.append({
                "id": case.id,
                "category": case.category,
                "complexity": case.complexity,
                "score": asdict(score),
            })

        duration = time.time() - start_time

        # Aggregate scores
        all_scores = [r["score"] for r in per_case_results]
        avg_scores = {}
        if all_scores:
            for key in all_scores[0]:
                if isinstance(all_scores[0][key], (int, float)):
                    avg_scores[key] = round(
                        sum(s[key] for s in all_scores) / len(all_scores), 3
                    )

        result = BenchmarkResult(
            run_id=hashlib.md5(
                f"{dataset_name}-{datetime.now().isoformat()}".encode()
            ).hexdigest()[:12],
            dataset=dataset_name,
            version="2.1.0",
            timestamp=datetime.now().isoformat(),
            total_cases=len(cases),
            scores=avg_scores,
            per_case=per_case_results,
            duration_seconds=round(duration, 2),
            config=self.config,
        )

        self.results.append(result)
        return result

    def run_all(self, datasets_dir: str = "datasets") -> List[BenchmarkResult]:
        """Run all datasets in the datasets directory."""
        results = []
        datasets_path = Path(datasets_dir)

        for dataset_file in sorted(datasets_path.glob("*.json")):
            print(f"Running: {dataset_file.name}")
            result = self.run_dataset(str(dataset_file))
            results.append(result)
            print(f"  Cases: {result.total_cases}, Avg clarity: {result.scores.get('clarity', 'N/A')}")

        return results

    def save_results(self, output_dir: str = "results"):
        """Save all results to JSON files."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        for result in self.results:
            filename = f"{result.dataset}_{result.run_id}.json"
            filepath = output_path / filename

            with open(filepath, "w") as f:
                json.dump(asdict(result), f, indent=2)

            print(f"Saved: {filepath}")

    def print_summary(self):
        """Print a formatted summary of all results."""
        print("\n" + "=" * 60)
        print("BENCHMARK SUMMARY")
        print("=" * 60)

        for result in self.results:
            print(f"\nDataset: {result.dataset}")
            print(f"  Cases: {result.total_cases}")
            print(f"  Duration: {result.duration_seconds}s")
            print(f"  Scores:")
            for metric, value in result.scores.items():
                bar = "█" * int(value * 10) + "░" * (10 - int(value * 10))
                print(f"    {metric:20s} {bar} {value:.3f}")

        print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Prompt Optimizer Benchmarks")
    parser.add_argument("--dataset", help="Path to a specific dataset JSON")
    parser.add_argument("--all", action="store_true", help="Run all datasets")
    parser.add_argument("--output", default="results", help="Output directory")
    parser.add_argument("--verbose", "-v", action="store_true")

    args = parser.parse_args()

    runner = BenchmarkRunner()

    if args.all:
        runner.run_all()
    elif args.dataset:
        runner.run_dataset(args.dataset)
    else:
        parser.print_help()
        return

    runner.save_results(args.output)
    runner.print_summary()


if __name__ == "__main__":
    main()
