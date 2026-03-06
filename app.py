from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Initialize OpenAI model
llm = ChatOpenAI(model="gpt-4.1-nano")

# Call OpenAI with simple string prompts
resp1 = llm.invoke("We are building an AI system for processing medical insurance claims.")
resp2 = llm.invoke("What are the main risks in this system?")

print("=== resp1 (single prompt 1) ===")
print(resp1.content)
print("\n=== resp2 (single prompt 2) ===")
print(resp2.content)

# String calls (invoke("...")) → stateless, no memory.-“this system” is ambiguous because the model has no prior context

# Call OpenAI with multiple messages (system + conversation history)
messages = [
    SystemMessage(content="You are a senior AI architect reviewing production systems."),
    HumanMessage(content="We are building an AI system for processing medical insurance claims."),
    HumanMessage(content="What are the main risks in this system?")
]

resp_messages = llm.invoke(messages)
print("\n=== resp_messages (message list) ===")
print(resp_messages.content)

"""
Reflection:

1. Why did string-based invocation fail? - String-based invocation fails because each call is stateless and forgets prior context.

2. Why does message-based invocation work? - Message-based invocation works because it explicitly pass the conversation history for continuity

3. What would break in a production AI system if we ignore message history? Ignoring history in production breaks context, leading to inconsistent, inaccurate, or non‑compliant outputs.

"""
