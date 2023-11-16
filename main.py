from dotenv import load_dotenv

load_dotenv()
from langchain.chat_models import ChatOpenAI
import streamlit as st

# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("내가 좋아하는 동물은 ")
# print(result)


chat_model = ChatOpenAI()

st.title("📜 A.I Story Maker")
title = st.text_input("Write your story title")

if st.button("Generate"):
    with st.spinner("A.I generating Stroy..."):
        result = chat_model.predict("Make a very short story about " + title)
        st.write("your story title is", title)
        st.write(result)
