from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(user_input):
    completions = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are a helpful assistant.
                you know a lot about animals, plants, and countries.
                """
            },
            {
                "role": "user",
                "content": user_input
            },
        ],
    )

    return completions.choices[0].message.content

def main():
    print("Welcome to Universe Facts Chatbot! (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()