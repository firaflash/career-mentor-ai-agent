import litellm

# 1. Save the original LiteLLM function
original_completion = litellm.completion

# 2. Create a custom function that deletes the hidden parameter
def clean_messages(*args, **kwargs):
    if 'messages' in kwargs:
        for msg in kwargs['messages']:
            if isinstance(msg, dict):
                msg.pop('cache_breakpoint', None) # <--- Deletes the offending parameter
    return original_completion(*args, **kwargs)

# 3. Force CrewAI to use our clean function instead
litellm.completion = clean_messages

# ... rest of your main.py code ...
from crewai import Agent, Task, Crew, LLM


# Initialize Large Language Model (LLM) of your choice (see all models on our Models page)
llm = LLM(model="groq/llama-3.1-8b-instant")


# 1. SKILL ASSESSMENT AGENT
skill_assessment_agent = Agent(
    role="Senior Career Skill Assessor",
    goal="Identify top 10 missing skills and categorize them by priority.",
    backstory="Experienced tech career coach specializing in skill-gap analysis.",
    llm=llm, # Change to your preferred LLM
    verbose=True,
    max_iter=1,
    allow_delegation=False
)

# 2. ROADMAP PLANNER AGENT
roadmap_planner_agent = Agent(
    role="Strategic Learning Path Architect",
    goal="Create a structured, step-by-step, time-bound learning roadmap to bridge the identified skill gaps.",
    backstory=(
        "You are an expert curriculum designer and educational strategist. "
        "You excel at breaking down complex career goals into actionable, logical, and realistic learning milestones. "
        "You always structure your roadmaps chronologically, ensuring foundational skills are learned before advanced ones."
    ),
    llm=llm,
    verbose=True,
    max_iter=1,
    allow_delegation=False
)

# 3. RESOURCE AGENT
resource_agent = Agent(
    role="Curated Educational Resource Finder",
    goal="Find and recommend the best, most up-to-date, and high-quality learning resources for each step of the roadmap.",
    backstory=(
        "You are a master of educational content. You know the best books, interactive courses, documentation, and YouTube channels. "
        "You only recommend practical, high-quality, and accessible resources. "
        "You always specify whether a resource is free or paid, and its format (video, text, interactive)."
    ),
    llm=llm,
    verbose=True,
    max_iter=1,
    allow_delegation=False
)

# 4. REVIEWER AGENT
reviewer_agent = Agent(
    role="Expert Career Mentor and Quality Reviewer",
    goal="Critically review the proposed roadmap and resources, ensuring they are realistic, cohesive, and perfectly aligned with the user's ultimate career goal.",
    backstory=(
        "You are a senior engineering manager and mentor. You are critical but constructive. "
        "You review learning plans to ensure they aren't overwhelming for a beginner. "
        "You check that the resources actually match the roadmap steps, and you provide final actionable feedback to perfect the plan."
    ),
    llm=llm,
    verbose=True,
    max_iter=1,
    allow_delegation=True # Allows the reviewer to ask the planner to fix things if the plan is bad!
)