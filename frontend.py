import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("FastAPI + Streamlit")

if st.button("Get Users"):
    response = requests.get(f"{API_URL}/users/")
    st.write(response.json())

user_name = st.text_input("User Name")
if st.button("Create User"):
    response = requests.post(f"{API_URL}/users/", json={"name": user_name})
    st.write(response.json())
