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
llm = LLM(
    model="mistral/mistral-large-latest",
    temperature=0.7
)

# Create your CrewAI agents with role, main goal/objective, and backstory/personality
summarizer = Agent(
    role='Documentation Summarizer', # Agent's job title/function
    goal='Create concise summaries of technical documentation', # Agent's main objective
    backstory='Technical writer who excels at simplifying complex concepts', # Agent's background/expertise
    llm=llm, # LLM that powers your agent
    verbose=True # Show agent's thought process as it completes its task
)

translator = Agent(
    role='Technical Translator',
    goal='Translate technical documentation to other languages',
    backstory='Technical translator specializing in software documentation',
    llm=llm,
    verbose=True
)

# Define your agents' tasks
summary_task = Task(
    description='Summarize this React hook documentation:\n\nuseFetch(url) is a custom hook for making HTTP requests. It returns { data, loading, error } and automatically handles loading states.',
    expected_output="A clear, concise summary of the hook's functionality",
    agent=summarizer # Agent assigned to task
)

translation_task = Task(
    description='Translate the summary to Turkish',
    expected_output="Turkish translation of the hook documentation",
    agent=translator,
    dependencies=[summary_task] # Must run after the summary task
)

# Create crew to manage agents and task workflow
crew = Crew(
    agents=[summarizer, translator], # Agents to include in your crew
    tasks=[summary_task, translation_task], # Tasks in execution order
    verbose=True,
    memory=False,      # <--- MUST BE FALSE
    planning=False,    # <--- MUST BE FALSE (Planning sometimes uses hidden caching)
    cache=False 

)

result = crew.kickoff()
print(result)
