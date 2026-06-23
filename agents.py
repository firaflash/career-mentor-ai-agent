from crewai import Agent , LLM
qwen =  LLM(
    model="ollama/qwen3:8b",
    base_url="http://localhost:11434"
)

researcher_agent = Agent(
    role = "Research Analyst",
    goal="Find key factual information about a topic",
    backstory="You are a technical researcher who extracts structured facts.",
    verbose=True, #verbose mode will print out the reasoning and thought process of the agent as it works on the task
    iterations=5, #iterations is the number of times the agent will work on the task before returning a final answer
    llm=qwen
)
writer_agent= Agent(
    role = "Technical Writer",
    goal="Convert research into a clear structured article",
    backstory="You simplify complex information for beginners.",
    verbose=True, #verbose mode will print out the reasoning and thought process of the agent as it works on the task
    iterations=5, #iterations is the number of times the agent will work on the task before returning a final answer
    llm=qwen # qwen is a large language model that is optimized for reasoning and problem solving

)