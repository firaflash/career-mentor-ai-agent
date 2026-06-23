from crewai import Task
from agents import researcher_agent, writer_agent

researcher_task = Task(
    name="Researcher Task",
    description="""
    Research the following topic thoroughly:
    {topic}

    Provide key facts, structured bullet points, and important insights.
    """,
    expected_output="A structured list of key facts and information about the topic.", # This was missing!
    agent= researcher_agent
)

writer_task = Task(
    name="Writer Task",
    description="""
    Using the research provided about:
    {topic}

    Write a structured article with:
    - Introduction
    - Key points
    - Explanation
    - Conclusion
    """,
    expected_output="A clear and structured article or report based on the research findings.", # This was missing!
    agent= writer_agent
)