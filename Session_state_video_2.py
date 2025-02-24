import streamlit as st

st.subheader("Session state video")
"session state object:", st.session_state

number = st.slider("A number", 1, 10, key="slider")

st.write(st.session_state)

col1, buff, col2 = st.columns([1, 0.5, 3])

option_names = ["a", "b", "c"]

next_choice = st.button("Next option")

if next_choice:
    if st.session_state["radio_option"] == "a":
        st.session_state.radio_option = "b"
    elif st.session_state["radio_option"] == "b":
        st.session_state.radio_option = "c"
    else:
        st.session_state.radio_option = "a"


option = col1.radio("Pick an option:", option_names, key="radio_option")
st.session_state

if option == "a":
    col2.write("You picked 'a'")
elif option == "b":
    col2.write("You picked 'b'")
else:
    col2.write("You picked 'c'")
