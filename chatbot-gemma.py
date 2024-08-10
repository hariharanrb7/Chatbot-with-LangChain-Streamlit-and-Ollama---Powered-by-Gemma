from langchain_openai import ChatOpenAI 
from langchain_core.prompts import  ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRANCING_V2"]="True"
os.environ["LANCHAIN_API_KEY"]=os.getenv("LANCHAIN_API_KEY")

#prompt template

prompt = ChatPromptTemplate.from_messages(

    [
        ("system","you are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)



#streamlit webapp

st.title("Chatbot using Langchain and Gemma")
input_text=st.text_input("search the topic u want")

#ollama llm
llm=Ollama(model="gemma")
output_parser=StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))
