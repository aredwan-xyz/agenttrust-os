# Contributing

AgentTrust OS is early. The best contributions make AI agent behavior easier to inspect, explain, replay, and improve.

## Good First Contributions

- Add a scenario file in `scenarios/`
- Add an example manifest in `examples/`
- Improve a report recommendation
- Add a missing check to `src/agenttrust/report.py`
- Improve documentation with a real agent workflow
- Add tests for a parser or risk check

## Local Setup

```bash
git clone https://github.com/aredwan-xyz/agenttrust-os.git
cd agenttrust-os
PYTHONPATH=src python3 -m unittest discover -s tests
PYTHONPATH=src python3 -m agenttrust scan agenttrust.example.yaml
```

## Design Principles

- Local-first: useful from a clean clone.
- Explainable: reports should be readable by builders and clients.
- Practical: prefer checks that produce clear fixes.
- Conservative: do not imply safety guarantees.
- Framework-friendly: adapters should preserve the core manifest/report model.

## Pull Request Checklist

- Tests pass with `PYTHONPATH=src python3 -m unittest discover -s tests`
- New checks include at least one test
- New scenarios include expected behavior
- Docs are updated when behavior changes
- Claims are specific and not overstated
