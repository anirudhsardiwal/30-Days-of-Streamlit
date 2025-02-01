import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import matplotlib.pyplot as plt

def style_negative(v, props=""):
    try:
        return props if v < 0 else None
    except:
        pass


def style_positive(v, props=""):
    try:
        return props if v > 0 else None
    except:
        pass

def audience_simple(country):
    if country == 'US':
        return 'USA'
    elif country == 'IN':
        return 'India'
    else:
        return 'Other'

# Load data
@st.cache_data
def load_data():
    df_agg = pd.read_csv(
        "/Users/Sardiwal_Anirudh/Documents/App Deployment/30-Days-of-Streamlit/kenjee yt data/Aggregated_Metrics_By_Video.csv"
    ).iloc[1:, :]  # remove first row

    df_agg_sub = pd.read_csv(
        "/Users/Sardiwal_Anirudh/Documents/App Deployment/30-Days-of-Streamlit/kenjee yt data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv"
    )

    df_comments = pd.read_csv(
        "/Users/Sardiwal_Anirudh/Documents/App Deployment/30-Days-of-Streamlit/kenjee yt data/All_Comments_Final.csv"
    )

    df_time = pd.read_csv(
        "/Users/Sardiwal_Anirudh/Documents/App Deployment/30-Days-of-Streamlit/kenjee yt data/Video_Performance_Over_Time.csv"
    )

    dfs = [df_agg, df_agg_sub, df_comments, df_time]

    for df in dfs:
        df.columns = df.columns.str.replace("\xad", "")

    df_agg["Video publish time"] = pd.to_datetime(
        df_agg["Video publish time"], format="%b %d, %Y"
    )

    df_agg["Average view duration"] = df_agg["Average view duration"].apply(
        lambda x: datetime.strptime(x, "%H:%M:%S")
    )

    df_agg["Average_duration_sec"] = df_agg["Average view duration"].apply(
        lambda x: x.hour * 3600 + x.minute * 60 + x.second
    )

    df_agg["Engagement_ratio"] = (
        df_agg["Comments added"]
        + df_agg["Shares"]
        + df_agg["Dislikes"]
        + df_agg["Likes"]
    ) / df_agg["Views"]

    df_agg["Views_by_sub_gained"] = df_agg["Views"] / df_agg["Subscribers gained"]

    df_agg.sort_values(by="Video publish time", ascending=False, inplace=True)

    df_time["Date"] = df_time["Date"].str.replace("Sept", "Sep")

    df_time["Date"] = pd.to_datetime(df_time["Date"])

    return df_agg, df_agg_sub, df_comments, df_time


load_data()

df_agg, df_agg_sub, df_comments, df_time = load_data()

# for i in df_agg.columns:

add_sidebar = st.sidebar.selectbox(
    "Aggregate or Individual Video", ["Aggregate", "Individual Video"]
)

df_agg["Video publish time"] = pd.to_datetime(
    df_agg["Video publish time"], format="%b %d, %Y"
)

df_agg_diff = df_agg.copy()
metric_date_12mo = df_agg_diff["Video publish time"].max() - pd.DateOffset(months=12)

numeric_cols = df_agg.select_dtypes(include=[np.number]).columns.tolist()

median_agg = df_agg_diff[df_agg_diff["Video publish time"] >= metric_date_12mo][
    numeric_cols
].median()

df_agg_diff[numeric_cols] = (df_agg_diff[numeric_cols] - median_agg).div(median_agg)

if add_sidebar == "Aggregate":
    df_agg_metrics = df_agg[
        [
            "Views",
            "Likes",
            "Subscribers",
            "Comments added",
            "Shares",
            "RPM (USD)",
            "Average percentage viewed (%)",
            "Average view duration",
            "Engagement_ratio",
            "Views_by_sub_gained",
        ]
    ]

    metric_date_6mo = df_agg["Video publish time"].max() - pd.DateOffset(months=6)
    metric_date_12mo = df_agg["Video publish time"].max() - pd.DateOffset(months=12)
    metric_median_6mo = df_agg[df_agg["Video publish time"] >= metric_date_6mo][
        numeric_cols
    ].median()
    metric_median_12mo = df_agg[df_agg["Video publish time"] >= metric_date_12mo][
        numeric_cols
    ].median()

    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]

    cols_metrics = [
        "Views",
        "Likes",
        "Subscribers",
        "Comments added",
        "Shares",
        "RPM (USD)",
        "Average percentage viewed (%)",
        "Average_duration_sec",
        "Engagement_ratio",
        "Views_by_sub_gained",
    ]

    count = 0
    for col in cols_metrics:
        with columns[count]:
            delta = (metric_median_6mo[col] - metric_median_12mo[col]) / metric_median_12mo[
                col
            ]
            st.metric(
                label=col,
                value=round(metric_median_6mo[col], 1),
                delta=f"{delta:.2%}",
            )
            count += 1
            if count >= 5:
                count = 0


    df_agg_diff["Publish_date"] = df_agg_diff["Video publish time"].apply(
        lambda x: x.date()
    )

    df_agg_diff_final = df_agg_diff[
        [
            "Video title",
            "Publish_date",
            "Views",
            "Likes",
            "Subscribers",
            "Average_duration_sec",
            "Engagement_ratio",
            "Views_by_sub_gained",
        ]
    ]


    df_agg_numeric_list = df_agg_metrics.median().index.tolist()

    df_agg_numeric_list = [
        "Average_duration_sec" if x == "Average view duration" else x
        for x in df_agg_numeric_list
    ]

    df_to_pct = {}

    for i in df_agg_numeric_list:
        df_to_pct[i] = "{:.1%}".format

    st.dataframe(
        df_agg_diff_final.style.hide()
        .applymap(style_negative, props="color:red;")
        .applymap(style_positive, props="color:green;")
        .format(df_to_pct)
    )

if add_sidebar == "Individual Video":
    videos = tuple(df_agg["Video title"].unique())
    video_select = st.selectbox("Pick a Video:",videos)
    agg_filtered = df_agg[df_agg["Video title"] == video_select]
    agg_sub_filtered = df_agg_sub[df_agg_sub['Video Title'] == video_select]
    agg_sub_filtered['Country'] = agg_sub_filtered['Country Code'].apply(audience_simple)
    agg_sub_filtered.sort_values('Is Subscribed', inplace=True)
    fig = px.bar(agg_sub_filtered, x = 'Views', y='Is Subscribed', color='Country', orientation = 'h')
    st.plotly_chart(fig)
    