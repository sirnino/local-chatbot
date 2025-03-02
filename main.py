import streamlit as st
from langchain_ollama.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

OLLAMA_BASEURL='http://192.168.1.99:11434/'
OLLAMA_MODEL='llama3.2:latest'

llm = ChatOllama(
        model = OLLAMA_MODEL,
        temperature = 0.6,
        base_url = OLLAMA_BASEURL
    )

prompt = ChatPromptTemplate(messages=[
    ("system", "You are a helpful AI bot. Your name is Jarvis."),
    ("human", "{user_input}"),
])

chain = prompt | llm | StrOutputParser()

messages = st.container()
if user_input := st.chat_input("Say something"):
    messages.chat_message("user").write(user_input)
    response = chain.invoke({"user_input": user_input})
    messages.chat_message("assistant").write(response)