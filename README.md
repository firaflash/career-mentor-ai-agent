# Career Mentor AI Agent

A Python-based AI assistant that builds personalized career learning roadmaps by chaining multiple specialized agents using CrewAI.

## What it does

This project uses a multi-agent workflow to take a user background and career goal, then:

1. Identifies missing skills.
2. Builds a step-by-step learning roadmap.
3. Suggests resources for each learning phase.
4. Reviews the final plan for realism and quality.

## Key features

- Four specialized agents: skill assessment, roadmap planning, resource recommendation, and final review.
- Task-level chaining via CrewAI `Task` context inputs.
- Example entrypoints in `main.py` and `test.py`.
- Configured for LLM usage through `crewai` and `litellm`.

## Installation

1. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Run the sample flow

```bash
python main.py
```

This script runs a single kickoff example with a sample user background and goal.

## Project files

- `agents.py` — defines the four AI agents, their roles, goals, and prompt backstories.
- `tasks.py` — defines the sequential task pipeline, including the callback pause helper.
- `crew.py` — constructs the `Crew` with agents, tasks, and process configuration.
- `main.py` — sample runner demonstrating a kickoff call using a user background and goal.
- `requirements.txt` — pinned Python dependencies.
- `docs/architecture.md` — project architecture and workflow documentation.

## Notes

- The project currently uses `mistral/mistral-large-latest` via `LLM(model=...)` in `main.py`.
- `main.py` includes a compatibility patch for `litellm` to remove unsupported hidden message metadata.
- Customize user input values in `main.py` to test different career goals and backgrounds.

## License

This repository is licensed under the terms of the `LICENSE` file.
