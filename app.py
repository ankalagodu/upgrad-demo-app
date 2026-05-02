import streamlit as st
import pandas as pd

# Add atitle
st.title("Hello Streamlit!")

# Add descriptive text
st.write("This is my first Streamlit app.")

# Add a text input field
name = st.text_input("Enter your name:")

# Display a dynamic greeting if a name is entered
if name:
    st.write(f"Hello, {name}!")

# Create a sample DataFrame
data = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"],"Age": [25, 30, 35]})

# Display the DataFrame in Streamlit
st.dataframe(data)