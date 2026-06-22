from crewai import Agent

researcher_agent = Agent(
    name="Researcher Agent",
    role = "Research Analyst",
    goal="Find key factual information about a topic",
    backstory="You are a technical researcher who extracts structured facts.",
    verbose=True, #verbose mode will print out the reasoning and thought process of the agent as it works on the task
    iterations=5, #iterations is the number of times the agent will work on the task before returning a final answer
    llm="gemini-1.5" # gemini-1.5 is a large language model that is optimized for reasoning and problem solving
)
writer_agent= Agent(
    name="Writter Agent",
    role = "Technical Writter",
    goal="Convert research into a clear structured article",
    backstory="You simplify complex information for beginners.",
    verbose=True, #verbose mode will print out the reasoning and thought process of the agent as it works on the task
    iterations=5, #iterations is the number of times the agent will work on the task before returning a final answer
    llm="gemini-1.5" # gemini-1.5 is a large language model that is optimized for reasoning and problem solving

)