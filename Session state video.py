import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
from datetime import time, datetime
import time


st.subheader("Session State Video")

"session state object: ", st.session_state

if "a_counter" not in st.session_state:
    st.session_state["a_counter"] = 0

if "boolean" not in st.session_state:
    st.session_state.boolean = False

st.write("Counter is:", st.session_state["a_counter"])
st.write("Boolean is:", st.session_state.boolean)

for the_key in st.session_state.keys():
    st.write(the_key)

for the_values in st.session_state.values():
    st.write(the_values)

for item in st.session_state.items():
    item

button = st.button("Update State")
"before pressing button", st.session_state
if button:
    st.session_state["a_counter"] += 1
    st.session_state.boolean = not st.session_state.boolean
"after pressing button", st.session_state

for key in st.session_state.keys():
    del st.session_state[key]

st.session_state
