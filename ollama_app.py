import streamlit as st
from utils.langchain_tracking import activate_langchain_tracking
from utils.response import generate_response

## activate tracking
activate_langchain_tracking()


## #Title of the app
st.title("Enhanced Q&A Chatbot With OpenAI")

## Select the LLM model
llm = st.sidebar.selectbox(
    "Select Open Source model", ["llama2-uncensored", "mistral", "gemma2:2b"]
)

## Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## MAin interface for user input
st.write("Goe ahead and ask any question")
user_input = st.text_input("You:")


if user_input:
    response = generate_response(
        user_input, 
        llm, 
        temperature, 
        max_tokens
    )
    st.write(response)
else:
    st.write("Please provide the user input")
