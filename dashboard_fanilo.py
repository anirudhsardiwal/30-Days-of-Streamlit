import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px
import plotly.graph_objects as go
import random

st.set_page_config(
    page_title="Dashboard Fanilo", page_icon=":bar_chart:", layout="wide"
)
with st.sidebar:
    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.info("Please upload a file")
    st.stop()

df = pd.read_excel(uploaded_file)

with st.expander("Show dataframe"):
    st.dataframe(df, column_config={"Year": st.column_config.NumberColumn(format="%d")})
    
all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def plot_metric(label, value, prefix="", suffix="", show_graph=False, color_graph=""):
    fig = go.Figure()
    
    fig.add_trace(go.Indicator(value=value, gauge={'axis': {'visible': False}},number={'prefix': prefix, 'suffix': suffix, 'font.size': 28}, title={'text': label, 'font':{'size': 24}))