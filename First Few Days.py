import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
from datetime import time, datetime
import time

# Day 22 #####################################################
st.subheader("Forms")
st.write("#### Coffee Machine")

with st.form("my_form"):
    st.write("##### Order your coffee")

    coffee_bean_val = st.selectbox("Coffee bean", ["Arabica", "Robusta"], index=0)
    coffee_roast_val = st.selectbox("Roast", ["Light", "Medium", "Dark"], index=0)
    serving_type_val = st.selectbox("Serving type", ["Hot", "Iced", "Frappe"], index=0)
    milk_val = st.select_slider(
        "Milk intensity", options=["None", "Low", "Medium", "High"], value=None
    )
    owncup_val = st.checkbox("Bring own cup", value=False)

    submitted = st.form_submit_button("Submit")

if submitted:
    st.markdown(
        f"""You have ordered:\n
        - Coffee bean: {coffee_bean_val}\n
        - Coffee Roast: {coffee_roast_val}\n
        - Serving type: {serving_type_val}"""
    )
form = st.form("Object notation", clear_on_submit=False)
selected_val = form.selectbox("something", ["low", "med", "high"], index=None)
slider_val = form.slider("select a val")
form.form_submit_button("submit")
st.write(f"selectbox is {selected_val} and slider value is {slider_val}")

# Day 21 #####################################################
st.divider()
st.subheader("Progress bar")

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)

# Day 19 #####################################################
# st.set_page_config(layout="wide")
st.divider()

st.subheader("Page Layout")

with st.expander("About this app"):
    st.write("Various ways of layout")
    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
        caption="This is some caption",
        width=250,
    )

st.sidebar.header("Input")
user_name = st.sidebar.text_input("What's your name?", placeholder="try")
user_emoji = st.sidebar.selectbox(
    "Choose an emoji:", ["😄", "😆", "😊", "😍", "😴", "😕", "😱"], index=None
)
user_food = st.sidebar.selectbox(
    "Fav food:", ["Tom Yum Kung", "Burrito", "Lasagna", "Hamburger"], index=None
)
st.sidebar.button("Something")

st.write("#### Output")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
tab1.write("The quick brown fox")
tab2.write("jumps over the lazy dog")

with st.popover("Settings"):
    st.checkbox("Something", value=False)

col1, col2, col3 = st.columns(3)

col1.write("This is Col 1!")

with col1:
    if user_name != "":
        st.write(f"Hello {user_name}!")
with col2:
    if user_emoji != "":
        st.write(f"{user_emoji} is your fav emoji!")
    else:
        st.write("Please choose an emoji")

# Day 18 #####################################################
st.divider()
st.subheader("File Uploader")

st.write("#### input csv")
uploaded_file = st.file_uploader("choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("#### DataFrame")
    st.write(df)
    st.write("#### Descriptive stats")
    st.write(df.describe())
else:
    st.info("Upload csv")


# Day 12 #####################################################
st.divider()
st.write("### st.checkbox")

page_names = ["Checkbox", "Button"]
page = st.radio("Navigation", page_names, index=0)
st.write(f"The variable page returns: {page}")
if page == "Checkbox":
    st.write("##### Welcome to checkbox page :smile:")
    check = st.checkbox("Click here", value=False)
    st.write(f"state of checkbox: {check}")
    if check:
        nested_btn = st.button("Button nested in checkbox")
        if nested_btn:
            st.write(":tada:" * 10)

else:
    st.write("##### You're on Button page :wave:")
    result = st.button("Click here")
    st.write(f"state of the button is {result}")
    if result:
        nested_check = st.checkbox("Checkbox nested in button", value=False)
        if nested_check:
            st.write(":heart:" * 10)

st.divider()

check = st.checkbox("Click here!")
st.write("State of the checkbox:", check)
if check:
    st.write(":smile:" * 10)

check2 = st.checkbox("Uncheck to remove cake", value=True)
st.write("State of the checkbox:", check2)
if check2:
    st.write(":cake:" * 10)

st.divider()

st.write("What would you like to order?")
icecream = st.checkbox("Ice Cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write(":icecream:")
if coffee:
    st.write(":coffee:")

# Day 11 #####################################################

st.write("### st.multiselect")
options = st.multiselect(
    "What are your fav colors?", ["R", "G", "B", "C", "M", "Y", "K"]
)
st.write(f"You selected {options}")

# Day 10 #####################################################

st.write("### st.selectbox")
option = st.selectbox("What's your fav color?", ("Blue", "Red", "Green"), index=None)
st.write(f"Your fav color is: {option}")

# Day 9 #####################################################

st.write("### Line Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)


# Day 8 #####################################################

st.subheader("st.slider")

age = st.slider("How old are you?", min_value=0, max_value=100, value=25, step=1)
st.write(f"I'm {age} years old")

st.write("#### Range Slider")
values = st.slider(
    "Select a range of values", min_value=0, max_value=100, value=(25, 75), step=1
)
st.write("Values:", values)

st.write("##### Range Time Slider")
appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)

start_time = st.slider(
    "When do you start?", value=datetime(2025, 1, 1, 9, 30), format="DD/MM/YY - hh:mm"
)
st.write(f"Start time: {start_time}")

# Day 5 #####################################################

st.write("Hello *world* :sunglasses:")
df = pd.read_csv("titanic.csv")
st.write(1234)

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
st.write(df)

df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
st.write(df2)

c = alt.Chart(df2).mark_circle().encode(x="a", y="b", size="c", color="c")
st.write(c)
st.caption("Explanation of the above chart")

# Day 3 #####################################################
st.header("st.button")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

# Day 2
st.title("My first app")
st.write("Hello world!")
