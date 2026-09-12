import streamlit as st
from datetime import date

st.title("Age Calculator")

dob = st.date_input(
    "Select your birthdate",
    value=date(2004, 5, 24),
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

if st.button("Calculate Age"):
    age = date.today().year - dob.year

    st.success(f"Your age is {age} years old")