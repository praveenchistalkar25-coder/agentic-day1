from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

resp1 = llm.invoke("We are building an AI system for processing medical insurance claims.")
resp2 = llm.invoke("What are the main risks in this system?")

print(response.content)

messages = [
    SystemMessage(content="You are a senior AI architect reviewing production systems."),
    HumanMessage(content="We are building an AI system for processing medical insurance claims."),
    HumanMessage(content="What are the main risks in this system?")
]

llm.invoke(messages)

"""
Reflection:

1. Why did string-based invocation fail?
2. Why does message-based invocation work?
3. What would break in a production AI system if we ignore message history?
"""
