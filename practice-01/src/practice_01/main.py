import streamlit as st

st.title("Movies")

col1, col2 = st.columns(2)

with col1:
    st.header("Hollywood")
    st.image("https://preview.redd.it/you-can-add-one-character-to-the-avengers-doomsday-lineup-v0-ihk6p08uoqoh1.jpeg?width=640&crop=smart&auto=webp&s=3ead4453c951153987c9f3aa78c926d69c410549", width=200)
    vote1 = st.button("vote for hollywood")

with col2:
    st.header("Bollywood")
    st.image("https://cdn.district.in/movies-assets/images/cinema/_Poster-d0d78f60-961a-11f1-8483-eb84b060bac3.jpg", width=200)
    vote2 = st.button("vote for bollywood")

name = st.sidebar.text_input("Enter your name")
movie_type = st.sidebar.selectbox("Choose your interest", ["Comedy", "Horror", "Thriller","Sci-fi"])

selected = ""
if vote1:
    st.success("Thanks for voting hollywood")
    st.write(f"Hello {name}, Your interest in hollywood {movie_type} movies.")
    selected = "hollywood"
elif vote2:
    st.success("Thanks for voting bollywood")
    st.write(f"Hello {name}, Your interest in bollywood {movie_type} movies.")
    selected = "bollywood"




with st.expander(f"Top 3 {selected} movies"):
    if vote1:
        st.write("""
        1. Game of Thrones
        2. Breaking Bad
        3. Chernobyl
        """)
    elif vote2:
        st.write("""
        1. Mirzapur
        2. Family Man
        3. Scam 1992: The Harshad Mehta Story
        """)

st.markdown('### Welcome to movie world')
st.markdown('> Blockquote')