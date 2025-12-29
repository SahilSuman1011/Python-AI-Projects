from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent

import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

tools = []
agent_executor = create_react_agent(model, tools) 

print("Agent is ready to use. Type 'quit' to exit.")
print("You can ask questions like 'What is the capital of France?' or 'Who won the World Series in 2020?'")

while True:
    user_input = input("\nYou: ").strip()