import numpy as np
import pandas as pd
import streamlit as st

# Day 2
st.title('My first app')
st.write('Hello world!')

# Day 3
st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')