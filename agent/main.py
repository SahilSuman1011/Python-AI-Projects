from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent

import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic operations."""
    print("tool has been called.")
    return f"The Sum of {a} and {b} is {a + b}."


# Initialize Gemini LLM
def main():
    model = ChatGoogleGenerativeAI(model="gemini-3-pro-preview")

    tools = [calculator]
    agent_executor = create_agent(model, tools)

    print("Agent is ready to use. Type 'quit' to exit.")
    print("You can ask questions like 'What is the capital of France?' or 'Who won the World Series in 2020?'")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
    ):
        
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
    print()

if __name__ == "__main__":
    main()
