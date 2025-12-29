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

# Example prompt and message
prompt = "Hello, Gemini! How can you help me build AI apps?"
response = llm.invoke(prompt)
print(response)