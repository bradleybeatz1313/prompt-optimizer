# Contributing to Prompt Optimizer

## Adding New Techniques

1. Add the technique to `core/techniques.md`
2. Create a deep-dive doc in `docs/technique-deep-dives/`
3. Add benchmark test cases in `benchmarks/datasets/`
4. Update both `desktop/SKILL.md` and `code/SKILL.md` (or just the relevant one)
5. Add an example in the appropriate `examples/` directory
6. Update `CHANGELOG.md`

## Adding Templates

1. Create a new `.md` file in `templates/`
2. Follow the existing template format (role + context + instruction blocks)
3. Include at least one worked example

## Running Benchmarks

```bash
cd benchmarks
python benchmark_runner.py --all
```

## Running Tests

```bash
python -m pytest tests/ -v
```

## Running Evals

```bash
cd evals
python eval_framework.py
```

## Version Numbering

- Desktop edition: v2.1.x
- Code edition: v2.0.x
- Core framework: follows desktop versioning
