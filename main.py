from crew import crew

def run():
    result = crew.kickoff(inputs={
        "topic": "What are the latest advancements in AI research and their potential impact on society?"
    })
    print("\n \n the result is " , result)

if __name__ == "__main__":
    run()