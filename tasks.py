from crewai import Task
from agents import resrercher_agent, writter_agent

researcher_task = Task(
    name="Resercher Task",
    description="This task is to research and gather information on a specific topic or question.",
    agent= resrercher_agent
)

writer_task = Task(
    name="Writter Task",
    description="This task is to write a report or document based on the information gathered by the researcher agent.",
    agent= writter_agent
)