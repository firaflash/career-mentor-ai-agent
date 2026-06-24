from crewai import Task
from agents import (
    skill_assessment_agent, 
    roadmap_planner_agent, 
    resource_agent, 
    reviewer_agent
)

# 1. Assessment Task (Takes user input)
assessment_task = Task(
    description=(
        "Analyze the user's current background and their target career goal.\n"
        "User Background: {background}\n"
        "User Goal: {goal}\n"
        "Identify the missing skills required to achieve the goal."
    ),
    expected_output="A structured 'Skill Gap Report' categorizing missing skills into 'Must-Have', 'Nice-to-Have', and 'Foundational'.",
    agent=skill_assessment_agent
)

# 2. Roadmap Task (Takes the output of Task 1)
roadmap_task = Task(
    description=(
        "Using the Skill Gap Report provided, create a chronological, step-by-step learning roadmap."
    ),
    expected_output="A structured 'Learning Roadmap' broken down by weeks or months, detailing exactly what to learn in each phase.",
    agent=roadmap_planner_agent,
    context=[assessment_task] # <--- MAGIC: Feeds the Skill Gap Report into this task
)

# 3. Resource Task (Takes the output of Task 2)
resource_task = Task(
    description=(
        "Using the Learning Roadmap provided, find and recommend specific learning resources for each phase."
    ),
    expected_output="A 'Resource Guide' listing specific course names, book titles, or documentation links for each step of the roadmap.",
    agent=resource_agent,
    context=[roadmap_task] # <--- MAGIC: Feeds the Roadmap into this task
)

# 4. Reviewer Task (Takes the output of Task 2 AND Task 3)
review_task = Task(
    description=(
        "Review the Learning Roadmap and the Resource Guide. Ensure the plan is realistic, not overwhelming, "
        "and that the resources actually match the roadmap steps. Provide final feedback and improvements."
    ),
    expected_output="A 'Final Mentor Review' containing constructive feedback, any necessary corrections to the plan, and a final encouraging summary.",
    agent=reviewer_agent,
    context=[roadmap_task, resource_task] # <--- MAGIC: Feeds BOTH the roadmap and resources to the reviewer
)