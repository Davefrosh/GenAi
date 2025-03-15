import os
import sys
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

# Load the environment variables
os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
os.environ['LANGSMITH_TRACING'] = 'true'
os.environ['LANGSMITH_PROJECT'] = os.getenv('LANGSMITH_PROJECT')


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#Crafting my Prompt Template
prompt = ChatPromptTemplate([
    ('system', "You are an AI Code Assistant, who will assist me with coding so many operations."),
    ('user','{question}')
])

st.title("LLM_APP")
st.write("This model is designed to provide coding assistance with regards to any questions asked.")


#Getting my LLM model
from langchain_community.llms import Ollama
llm = Ollama(model = 'gemma2:2b')
parse = StrOutputParser()
chain = prompt|llm|parse

input_text = st.text_input("Ask a question")


if input_text:
    output = chain.invoke({'question': input_text})
    st.write(output)



