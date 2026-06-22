from crewai import Crew
from tasks import resercher_task, writter_task
from agents import researcher_agent, writter_agent 

crew = Crew(
    agents = [ researcher_agent , writter_agent],
    tasks = [researcher_task , writter_task],
    verbose= True
)

