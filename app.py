from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
import streamlit as st
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response
st.set_page_config("QQ&A Chatbot")
st.header("Conversational Chatbot")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
input=st.text_input("Input: ", key="input")
submit=st.button("Send")
if input and submit:
    response=get_gemini_response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response: ")
    for chunk in response: 
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Response", chunk.text))
st.subheader("Chat history: ")
for role, response in st.session_state['chat_history']:
    st.write(f"{role}: {response}")
