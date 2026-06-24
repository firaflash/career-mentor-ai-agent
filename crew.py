from crewai import Crew, Process
from tasks import assessment_task, roadmap_task, resource_task, review_task
from agents import skill_assessment_agent, roadmap_planner_agent, resource_agent, reviewer_agent

# Create the Crew
crew = Crew(
    agents=[skill_assessment_agent, roadmap_planner_agent, resource_agent, reviewer_agent],
    tasks=[assessment_task, roadmap_task, resource_task, review_task],
    process=Process.sequential,
    verbose=True
)

