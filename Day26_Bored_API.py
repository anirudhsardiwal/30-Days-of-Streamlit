import streamlit as st
import requests


st.title("Bored API App")

st.sidebar.header("Input")

selected_type = st.sidebar.selectbox(
    "Select an activity",
    [
        "education",
        "recreational",
        "social",
        "diy",
        "charity",
        "cooking",
        "relaxation",
        "music",
        "busywork",
    ],
)
