import streamlit as st
import requests
st.title("AI Article Summarizer")
email = st.text_input("Email")
url = st.text_input("Article URL")
if st.button("Submit"):
    res = requests.post("http://127.0.0.1:8000/submit", json={"email": email, "url": url})
    st.write("Submitted!")