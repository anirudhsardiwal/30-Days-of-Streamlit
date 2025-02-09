import streamlit as st
import datetime


# Temperature #############################################
if "celsius" not in st.session_state:
    st.session_state.celsius = 50

st.slider("Temp. in celsius", -100, 100, key="celsius")

st.write(st.session_state.celsius)


# Forms and Callbacks #############################################
st.subheader("Forms and callbacks")
if "count" not in st.session_state:
    st.session_state.count = 0
    st.session_state.last_updated = datetime.time(0, 0)


def update_counter():
    st.session_state.count += st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time


st.session_state.update_time = datetime.datetime.now().time()
st.write(st.session_state.update_time)
with st.form(key="my_form"):
    # st.time_input("Enter time:", datetime.datetime.now().time(), key="update_time")
    st.number_input("Enter a value", 0, step=1, key="increment_value")
    submit = st.form_submit_button("Update", on_click=update_counter)

st.write("Current count:", st.session_state.count)
st.write("Last updated:", st.session_state.last_updated)

# Counter w/ kwargs #############################################
# st.subheader("Counter with kwargs")
# if "count" not in st.session_state:
#     st.session_state.count = 0


# def increment_counter(increment_value=0):
#     st.session_state.count += increment_value


# def decrement_counter(decrement_value=0):
#     st.session_state.count -= decrement_value


# st.button("Increment", on_click=increment_counter, kwargs=dict(increment_value=5))

# st.button("Decrement", on_click=decrement_counter, kwargs=dict(decrement_value=1))

# st.write("Count = ", st.session_state.count)


# Weight Converter #############################################
st.subheader("Callbacks")

"session state object:", st.session_state


def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs / 2.2


def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg * 2.2


col1, buff, col2 = st.columns([2, 1, 2])
with col1:
    pounds = st.number_input("Pounds:", key="lbs", on_change=lbs_to_kg)
with col2:
    kilos = st.number_input("Kilos:", key="kg", on_change=kg_to_lbs)

# Counter #############################################
st.subheader("Counter example")

if "count" not in st.session_state:
    st.session_state.count = 0

increment_value = st.number_input("Enter a value", value=0, step=1)


def increment_counter(increment_value):
    st.session_state.count += increment_value


increment = st.button("Increment", on_click=increment_counter, args=(increment_value,))

st.write("Count = ", st.session_state.count)
