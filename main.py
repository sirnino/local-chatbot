import streamlit as st
from chatbot import get_chatbot_chain
from ollama import Client

client = Client(
  host='http://192.168.1.99:11434'
)
ollama_models = [m.model for m in client.list()['models']]

with st.sidebar:
    st.title("Select your model")
    model = st.selectbox("Model", ollama_models)
    temperature = st.slider("Temperature", 0.0, 1.0, 0.5)

chain = get_chatbot_chain("llama3.2:latest", temperature)
st.title("Chat with Lumina")
st.write(f"Using model: {model}")

messages = st.container()
# Session State initialization
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

if user_input := st.chat_input("Say something"):
    st.session_state['messages'].append(("user", user_input))
    response = chain.invoke({"user_input": user_input})
    st.session_state['messages'].append(("assistant", response))

for msg in st.session_state['messages']:
    with messages:
        st.chat_message(msg[0]).write(msg[1])