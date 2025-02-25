import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px
import plotly.graph_objects as go
import random

st.set_page_config(
    page_title="Dashboard Fanilo", page_icon=":bar_chart:", layout="wide"
)
# with st.sidebar:
#     uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is None:
#     st.info("Please upload a file")
#     st.stop()

url = "https://raw.githubusercontent.com/anirudhsardiwal/30-Days-of-Streamlit/main/Financial%20Data%20Clean.xlsx"
df = pd.read_excel(url)

# df['Year'] = df['Year'].replace(',','')

all_months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]


def plot_metric(label, value, prefix="", suffix="", show_graph=False, color_graph=""):
    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            value=value,
            gauge={"axis": {"visible": False}},
            number={"prefix": prefix, "suffix": suffix, "font.size": 28},
            title={"text": label, "font": {"size": 24}},
        )
    )

    if show_graph:
        fig.add_trace(
            go.Scatter(
                y=random.sample(range(0, 101), 30),
                hoverinfo="skip",
                fill="tozeroy",
                fillcolor=color_graph,
                line={"color": color_graph},
            )
        )

    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)
    fig.update_layout(
        margin=dict(t=30, b=0), showlegend=False, plot_bgcolor="white", height=100
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_gauge(
    indicator_number, indicator_color, indicator_suffix, indicator_title, max_bound
):
    fig = go.Figure(
        go.Indicator(
            value=indicator_number,
            mode="gauge+number",
            domain={"x": [0, 1], "y": [0, 1]},
            number={"suffix": indicator_suffix, "font.size": 26},
            gauge={
                "axis": {"range": [0, max_bound], "tickwidth": 1},
                "bar": {"color": indicator_color},
            },
            title={"text": indicator_title, "font": {"size": 28}},
        )
    )

    fig.update_layout(height=200, margin=dict(l=10, r=10, t=50, b=10, pad=8))
    st.plotly_chart(fig, use_container_width=True)


def plot_top_right():
    df["Year"] = pd.to_datetime(df["Year"], format="%Y")

    # Melt the dataframe to convert months to rows
    sales_data = df[(df["Year"] == "2023") & (df["Account"] == "Sales")][
        ["Scenario", "business_unit"] + all_months
    ].melt(
        id_vars=["Scenario", "business_unit"],
        value_vars=all_months,
        var_name="month",
        value_name="sales",
    )

    # Group by scenario and business unit to get total sales
    sales_data = (
        sales_data.groupby(["Scenario", "business_unit"])["sales"].sum().reset_index()
    )

    fig = px.bar(
        sales_data,
        x="business_unit",
        y="sales",
        color="Scenario",
        barmode="group",
        text_auto=".2s",
        title="Sales for year 2023",
        height=400,
    )
    fig.update_traces(
        textfont_size=12, textangle=0, textposition="outside", cliponaxis=False
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_bottom_left():
    df["Year"] = pd.to_datetime(df["Year"], format="%Y")
    df["Year"] = df["Year"].dt.year

    df_filt = df[
        (df["Account"] == "Sales")
        & (df["Year"] == 2023)
        & (df["business_unit"] == "Software")
    ]
    sales_data = df_filt.melt(
        id_vars=["Scenario"],
        value_vars=all_months,
        var_name="month",
        value_name="sales",
    )

    fig = px.line(
        sales_data,
        x="month",
        y="sales",
        color="Scenario",
        markers=True,
        text="sales",
        title="Monthly Budget vs Forecast 2023",
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)


def plot_bottom_right():
    df_actual_filtered = df[(df["Scenario"] == "Actuals") & (df["Account"] != "Sales")]

    for month in all_months:
        df_actual_filtered.loc[:, month] = df_actual_filtered[month].abs()

    df_unpivoted = df_actual_filtered.melt(
        id_vars=["Account", "Year"],
        value_vars=all_months,
        var_name="month",
        value_name="sales",
    )

    sales_data = df_unpivoted.groupby(["Account", "Year"])["sales"].sum().reset_index()

    fig = px.bar(
        sales_data,
        x="Year",
        y="sales",
        color="Account",
        title="Actual Yearly Sales per Account",
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write(sales_data)

    ######################################
    # STREAMLIT LAYOUT
    ######################################


top_left_col, top_right_col = st.columns((2, 1))
bot_left_col, bot_right_col = st.columns(2)

with top_left_col:
    col_1, col_2, col_3, col_4 = st.columns(4)

    with col_1:
        plot_metric(
            "Total Accounts Receivable",
            6621280,
            prefix="$",
            suffix="",
            show_graph=True,
            color_graph="rgba(0, 104, 201, 0.2)",
        )

        plot_gauge(10, "#FF8700", " days", "In Stock", 31)

    with col_2:
        plot_metric(
            "Total Accounts Payable", 1630270, "$", "", True, "rgba(255, 43, 43, 0.2)"
        )

        plot_gauge(1.86, "#0068C9", "%", "Current Ratio", 3)

    with col_3:
        plot_metric("Equity Ratio", 75.38, "", "%", False, "#d1f2eb")

        plot_gauge(7, "#FF2B2B", " days", "Out Stock", 31)

    with col_4:
        plot_metric("Debt Equity", 1.10, prefix="", suffix=" %", show_graph=False)
        plot_gauge(28, "#29B09D", " days", "Delay", 31)

with top_right_col:
    plot_top_right()

with bot_left_col:
    plot_bottom_left()

with bot_right_col:
    plot_bottom_right()
