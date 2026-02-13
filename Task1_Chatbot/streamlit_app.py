import streamlit as st
import re 
import datetime

st.title("RahulBot  - Streamlit Version")

user_input = st.text_input("You :")

if user_input:
    user_input = user_input.lower()

    if re.search(r"\b(hi|hello|hey)\b",user_input):
        response = "Hello Rahul "

    elif "time" in user_input:
        response = datetime.datetime.now().strftime("%H:%M:%S")
    elif "your name" in user_input:
        response = "I am RahulBot"
    elif "ai" in user_input:
        response = "Ai stands for artificial Intelligence"
    else:
        response ="Sorry I Dont understand"
    
    st.write("Bot: ",response)