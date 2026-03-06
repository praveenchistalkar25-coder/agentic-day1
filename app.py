from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Initialize OpenAI model
llm = ChatOpenAI()

# Call OpenAI with a simple string
resp1 = llm.invoke("We are building an AI system for processing medical insurance claims.")
resp2 = llm.invoke("What are the main risks in this system?")

print(resp1.content)
print(resp2.content)

# Call OpenAI with multiple messages
messages = [
    SystemMessage(content="You are a senior AI architect reviewing production systems."),
    HumanMessage(content="We are building an AI system for processing medical insurance claims."),
    HumanMessage(content="What are the main risks in this system?")
]

resp2 = llm.invoke(messages)
print(resp2.content)

"""
Reflection:

1. Why did string-based invocation fail?
2. Why does message-based invocation work?
3. What would break in a production AI system if we ignore message history?
"""
