# Career Mentor AI Agent

## Problem

People often don't know what skills they need to achieve a specific career goal.

## Goal

Generate a personalized learning roadmap by using a chain of AI agents to assess skill gaps, plan learning steps, recommend resources, and review the final plan.

## Architecture Overview

The project is built around CrewAI and a small set of Python modules:

* `agents.py` defines the AI agents with roles, goals, backstories, and model configuration.
* `tasks.py` defines the agent tasks and task dependencies, including the sequential workflow.

* `crew.py` assembles the `Crew` from agents and tasks.
* `main.py` contains a sample runner and a compatibility patch for `litellm`.

### Workflow

1. `main.py`  starts the process.
2. `crew.py` creates a `Crew` with all four agents and the sequential process.
3. The workflow runs through four tasks:
   - `assessment_task`
   - `roadmap_task`
   - `resource_task`
   - `review_task`
4. Task outputs are passed to later tasks through the `context` field.

## Agents

### 1. Skill Assessment Agent

Input:

- User background
- User goal

Output:

- Skill gap report

### 2. Roadmap Planner Agent

Input:

- Skill gap report

Output:

- Learning roadmap

### 3. Resource Agent

Input:

- Learning roadmap

Output:

- Learning resources

### 4. Reviewer Agent

Input:

- Learning roadmap
- Resource guide

Output:

- Final mentor review with feedback and improvements

## Notes

- `main.py` includes a custom `litellm` wrapper that strips unsupported hidden message metadata before calling `litellm.completion`.
- The project uses `mistral/mistral-large-latest` as the default LLM model in `main.py`.
