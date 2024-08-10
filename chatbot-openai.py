'''
To use chatgpt turbo we needs subscription, there are some open source llm, chatbot-gemma.py file in this repository,that uses Gemma opensource llm model and doesn't charges any amount
'''
from langchain_openai import ChatOpenAI
from langchain_core.prompts import  ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#langsmith tracking
os.environ['LANGCHAIN_TRANCING_V2']="True"
os.environ['LANCHAIN_API_KEY']=os.getenv("LANCHAIN_API_KEY")

#prompt template

prompt = ChatPromptTemplate.from_messages(

    [
        ("system","you are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)

#streamlit webapp

st.title("Chatbot using Langchain and OpenAI")
input_text=st.text_input("search the topic u want")

#openAI llm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
