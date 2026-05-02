import streamlit as st
import requests

# Access secret values
api_key = st.secrets["API_KEY"]

st.title("Secure API Access Demo")

# Example API request
url = "https://api.example.com/data"
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    st.write("API Response:", response.json())
else:
    st.error(f"Error: {response.status_code}")