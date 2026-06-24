import litellm

original_completion = litellm.completion

def clean_messages(*args, **kwargs):
    if "messages" in kwargs:
        for msg in kwargs["messages"]:
            if isinstance(msg, dict):
                msg.pop("cache_breakpoint", None)

    return original_completion(*args, **kwargs)

litellm.completion = clean_messages

from crewai import Agent , LLM
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.3,
    max_tokens=800
)

researcher_agent = Agent(
    role = "Research Analyst",
    goal="Find key factual information about a topic",
    backstory="You are a technical researcher who extracts structured facts.",
    verbose=True, #verbose mode will print out the reasoning and thought process of the agent as it works on the task
    iterations=5, #iterations is the number of times the agent will work on the task before returning a final answer
    llm=llm
)
writer_agent= Agent(
    role = "Technical Writer",
    goal="Convert research into a clear structured article",
    backstory="You simplify complex information for beginners.",
    verbose=True, #verbose mode will print out the reasoning and thought process of the agent as it works on the task
    iterations=5, #iterations is the number of times the agent will work on the task before returning a final answer
    llm=llm # qwen is a large language model that is optimized for reasoning and problem solving

)