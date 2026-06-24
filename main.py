from crew import crew

def run():
    result = crew.kickoff(inputs={
        "background": "I am a beginner in programming. I know basic HTML and CSS, but no JavaScript or backend languages.",
    "goal": "I want to become a Full-Stack Backend Engineer using Python and Django within 6 months."
    })
    print("\n \n the result is " , result)

if __name__ == "__main__":
    run()