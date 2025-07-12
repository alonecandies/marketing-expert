from langchain_openai import ChatOpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-xxx")

llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-4-turbo"
)

def generate_marketing_response(messages):
    # messages: list of dicts with 'role' and 'content'
    chat_history = [(m['role'], m['content']) for m in messages]
    response = llm.invoke(chat_history)
    return response.content
