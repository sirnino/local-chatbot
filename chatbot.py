from langchain_ollama.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

def get_chatbot_chain(model='llama3.2:latest', base_url='http://127.0.0.1:11434', temperature=0.3):
    llm = ChatOllama(
            model = model,
            temperature = temperature,
            base_url = base_url
        )

    prompt = ChatPromptTemplate(messages=[
        ("system", "You are a helpful AI bot. Your name is Lumina."),
        MessagesPlaceholder("history"),
        ("human", "{user_input}"),
    ])

    chain = prompt | llm | StrOutputParser()
    return chain