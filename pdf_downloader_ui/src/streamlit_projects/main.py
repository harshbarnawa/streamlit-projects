import streamlit as st

st.title("PDF downloader")

if st.button("Download"):
    st.success("Downloaded successfully")

add_theme = st.checkbox("Add Theme")

if add_theme:
    st.write("Theme added")

theme_color = st.radio("Pick a color: ", ["Red", "Blue", "Green"])


st.write(f"Color selected: {theme_color}")

pdf_size = st.selectbox("Choose size: ", ["A4", "Letter", "Legal"])

st.write(f"Size of pdf is {pdf_size}")

text_size = st.slider("Text Size", 0, 10, 4)
st.write(f"Size of text is {text_size}")

st.number_input("How many pages", min_value=1, max_value=10, step=1)

name = st.text_input("Enter pdf name")

if name:
    st.write(f"Your pdf name is {name}.pdf")

dob = st.date_input("Select your birthdate")
st.write(f"Your birthday is {dob}")