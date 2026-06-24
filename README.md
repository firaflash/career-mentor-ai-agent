
# Career Mentor Multi-AI Agent

A Python-based AI assistant that generates personalized career-learning roadmaps using multiple AI agents orchestrated with CrewAI.

## What It Does

This project analyzes a user's current background and desired career path, then automatically:

1. Identifies missing skills.
2. Creates a structured learning roadmap.
3. Recommends learning resources.
4. Reviews and improves the final plan.

The workflow is powered by multiple specialized CrewAI agents working together sequentially.

---

## Features

* Multi-agent architecture using CrewAI.
* Skill gap analysis.
* Learning roadmap generation.
* Resource recommendations.
* Final quality review.
* Support for multiple LLM providers:
  * Groq
  * Mistral AI
* Built-in compatibility patch for CrewAI/LiteLLM message formatting.
* Optional task delays to reduce Groq rate-limit errors.

---

## Installation

### Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

### Using Groq

```env
GROQ_API_KEY=your_groq_api_key
```

### Using Mistral AI

```env
MISTRAL_API_KEY=your_mistral_api_key
```

Only provide the key for the provider you intend to use.

---

## Supported Models

### Option 1: Groq

Recommended when fast inference is required.

Example configuration in `agents.py`:

```python
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.3,
    max_tokens=800
)
```

### Option 2: Mistral AI

Recommended when higher-quality reasoning is preferred.

```python
llm = LLM(
    model="mistral/mistral-large-latest",
    temperature=0.3,
    max_tokens=800
)
```

Switch providers by changing only the model name.

---

## LiteLLM Compatibility Patch

Some CrewAI versions inject hidden metadata into messages:

```python
cache_breakpoint
```

Groq does not support this parameter and rejects requests with an error similar to:

```text
property 'cache_breakpoint' is unsupported
```

To prevent this issue, the project includes a LiteLLM patch in `main.py`:

```python
import litellm

original_completion = litellm.completion

def clean_messages(*args, **kwargs):
    if "messages" in kwargs:
        for msg in kwargs["messages"]:
            if isinstance(msg, dict):
                msg.pop("cache_breakpoint", None)

    return original_completion(*args, **kwargs)

litellm.completion = clean_messages
```

This removes unsupported metadata before the request reaches the model provider.

---

## Groq Rate-Limit Handling

Groq free-tier models enforce Tokens Per Minute (TPM) and Requests Per Minute (RPM) limits.

Because this project uses multiple agents, several model calls may occur within a short time period.

To reduce rate-limit errors, a delay callback is included between certain tasks:

```python
import time

time.sleep(20)
```

The 20-second delay helps:

* Reduce TPM spikes.
* Reduce RPM spikes.
* Improve reliability for free-tier Groq accounts.
* Prevent frequent `RateLimitError` exceptions.

This delay is primarily recommended when using:

```python
groq/llama-3.1-8b-instant
```

---

## Running the Project

Execute:

```bash
python3 main.py
```

Example input:

```python
crew.kickoff(
    inputs={
        "user_background": "I know HTML and CSS.",
        "career_goal": "Become a Full-Stack Backend Engineer using Python and Django."
    }
)
```

The crew will:

1. Assess skills.
2. Build a roadmap.
3. Recommend resources.
4. Review the final plan.

---

## Project Structure

```text
.
├── agents.py
├── tasks.py
├── crew.py
├── main.py
├── test.py
├── requirements.txt
├── .env
└── docs/
    └── architecture.md
```

### File Descriptions

| File                 | Purpose                                         |
| -------------------- | ----------------------------------------------- |
| agents.py            | Defines all CrewAI agents and LLM configuration |
| tasks.py             | Defines tasks and task relationships            |
| crew.py              | Creates the CrewAI workflow                     |
| main.py              | Entry point and LiteLLM compatibility patch     |
| test.py              | Testing and experimentation                     |
| requirements.txt     | Project dependencies                            |
| docs/architecture.md | System architecture documentation               |
