from crewai import Crew
from tasks import researcher_task, writer_task
from agents import researcher_agent, writer_agent 

crew = Crew(
    agents = [ researcher_agent , writer_agent],
    tasks = [researcher_task , writer_task],
    verbose= True
)

