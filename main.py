import ollama

def run_agent():
    goal = input("Enter your goal: ")

    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "system", "content": "You create structured step-by-step plans."},
            {"role": "user", "content": goal}
        ]
    )

    print("\nGenerated Output:\n")
    print(response['message']['content'])

if __name__ == "__main__":
    run_agent()