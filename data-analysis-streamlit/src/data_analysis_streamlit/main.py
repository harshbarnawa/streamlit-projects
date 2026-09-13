import streamlit as st
import pandas as pd

st.title("Data Analysis Dashboard")

file = st.file_uploader("Uplaod your csv file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    pokemon_type = df["Type1"].unique()
    selected = st.selectbox("Filter by type", pokemon_type)
    filtered_data = df[df["Type1"] == selected]
    st.dataframe(filtered_data)