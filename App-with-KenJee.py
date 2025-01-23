import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Load data
df_agg = pd.read_csv('/workspaces/30-Days-of-Streamlit/kenjee yt data/Aggregated_Metrics_By_Video.csv').iloc[1:,:] # remove first row

df_agg_sub = pd.read_csv('/workspaces/30-Days-of-Streamlit/kenjee yt data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')

df_comments = pd.read_csv('/workspaces/30-Days-of-Streamlit/kenjee yt data/All_Comments_Final.csv')

df_time = pd.read_csv('/workspaces/30-Days-of-Streamlit/kenjee yt data/Video_Performance_Over_Time.csv')


# Data cleaning
df_agg.columns = ['Video','Video title','Video publish time','Comments added','Shares','Dislikes','Likes','Subscribers lost','Subscribers gained','RPM(USD)','CPM(USD)','Average % viewed','Average view duration','Views','Watch time (hours)','Subscribers','Your estimated revenue (USD)','Impressions','Impressions ctr(%)']

df_agg['Video publish time'] = pd.to_datetime(df_agg['Video publish time'], format='%b %d, %Y')

df_agg['Average view duration'] = df_agg['Average view duration'].apply(lambda x: datetime.strptime(x, '%H:%M:%S'))

df_agg['Average_duration_sec'] = df_agg['Average view duration'].apply(lambda x: x.hour*3600 + x.minute*60 + x.second) 