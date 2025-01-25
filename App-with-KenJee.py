import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Load data
@st.cache_data
def load_data():
    df_agg = pd.read_csv('/workspaces/30-Days-of-Streamlit/kenjee yt data/Aggregated_Metrics_By_Video.csv').iloc[1:,:] # remove first row

    df_agg_sub = pd.read_csv('/workspaces/30-Days-of-Streamlit/kenjee yt data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')

    df_comments = pd.read_csv('/workspaces/30-Days-of-Streamlit/kenjee yt data/All_Comments_Final.csv')

    df_time = pd.read_csv('/workspaces/30-Days-of-Streamlit/kenjee yt data/Video_Performance_Over_Time.csv')
    
    print(df_agg.columns)    
    
    # df_agg['Video publish time'] = pd.to_datetime(df_agg['Video publish time'], format='%b %d, %Y')

    # df_agg['Average view duration'] = df_agg['Average view duration'].apply(lambda x: datetime.strptime(x, '%H:%M:%S'))

    # df_agg['Average_duration_sec'] = df_agg['Average view duration'].apply(lambda x: x.hour*3600 + x.minute*60 + x.second) 

    # df_agg['Engagement_ratio'] = (df_agg['Comments added'] + df_agg['Shares'] + df_agg['Dislikes'] + df_agg['Likes']) / df_agg['Views']

    # df_agg['Views_by_sub_gained'] = df_agg['Views'] / df_agg['Subscribers gained']

    # df_agg.sort_values(by='Video publish time', ascending=False, inplace=True)

    df_time['Date'] = df_time['Date'].str.replace('Sept', 'Sep')

    df_time['Date'] = pd.to_datetime(df_time['Date'])

    return df_agg, df_agg_sub, df_comments, df_time

# 
df_agg, df_agg_sub, df_comments, df_time = load_data()

add_sidebar = st.sidebar.selectbox('Aggregate or Individual Video', ['Aggregate', 'Individual Video'])


