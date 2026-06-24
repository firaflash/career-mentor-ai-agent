from crew import crew

def run():
    result = crew.kickoff(
    inputs={
        "background": """
        I have experience with C++, HTML, CSS, JavaScript, Python, Git, Linux, SQL, and web development.
        I have built personal and academic projects including web applications, automation tools, and AI-agent based systems using CrewAI.
        I am currently working on software development and AI-related projects and want to improve my backend engineering and AI engineering skills.
        """,

                "goal": """
        Build a Telegram bot platform that automatically generates and posts educational content about AI, programming, software engineering, and technology.
        The platform should support scheduled posting, content generation using AI agents, topic management, analytics, and multi-channel publishing.
        I want a roadmap that helps me design, build, deploy, and scale this platform while improving my backend engineering and AI agent development skills.
        """
            }
        )
    print("\n \n the result is " , result)

if __name__ == "__main__":
    run()