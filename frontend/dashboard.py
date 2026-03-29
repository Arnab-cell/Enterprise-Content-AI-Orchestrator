
import streamlit as st
import requests

st.title("Enterprise AI Content Operations")

topic = st.text_input("Content Topic")
audience = st.text_input("Target Audience")

if st.button("Run AI Pipeline"):

    res = requests.post(
        "http://localhost:8000/generate",
        params={"topic": topic, "audience": audience}
    )

    st.json(res.json())
