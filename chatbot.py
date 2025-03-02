from langchain_ollama.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

OLLAMA_BASEURL='http://192.168.1.99:11434/'

def get_chatbot_chain(model='llama3.2:latest', temperature=0.3):
    llm = ChatOllama(
            model = model,
            temperature = temperature,
            base_url = OLLAMA_BASEURL
        )

    prompt = ChatPromptTemplate(messages=[
        ("system", "You are a helpful AI bot. Your name is Lumina."),
        ("human", "{user_input}"),
    ])

    chain = prompt | llm | StrOutputParser()
    return chain