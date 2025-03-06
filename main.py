import streamlit as st
from chatbot import get_chatbot_chain
from ollama import Client

OLLAMA_BASEURL='http://192.168.1.99:11434'

client = Client(
  host=OLLAMA_BASEURL
)
ollama_models = [m.model for m in client.list()['models']]

with st.sidebar:
    st.title("Select your model")
    model = st.selectbox("Model", ollama_models)
    temperature = st.slider("Temperature", 0.0, 1.0, 0.5)

chain = get_chatbot_chain("llama3.2:latest", base_url=OLLAMA_BASEURL, temperature=temperature)
st.title("Chat with Lumina")
st.caption(f"Using model: {model}")

messages = st.container()
# Session State initialization
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for msg in st.session_state['messages']:
    with messages:
        st.chat_message(msg[0]).write(msg[1])

if user_input := st.chat_input("Say something"):
    st.chat_message("user").write(user_input)
    response = st.chat_message("assistant").write_stream(chain.stream({"history":  st.session_state['messages'], "user_input": user_input}))
    st.session_state['messages'].append(("user", user_input))
    st.session_state['messages'].append(("assistant", response))
