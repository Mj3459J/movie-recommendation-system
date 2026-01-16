import streamlit as st
import pickle
import pandas as pd
import numpy as np
from utils.recommend import recommend

movies_list=pickle.load(open("movies.pkl","rb"))
movies_list=movies_list['title'].values

st.title('Movie Recommender System')
selected_movie_name=st.selectbox(
    "Select the movie",
    movies_list 
)

if st.button("Recommend"):
    st.write(f"Movies related to {selected_movie_name}: ")
    names,posters=recommend(selected_movie_name)
    
    # col1,col2,col3,col4,col5=st.columns(5)
    
    # with col1:
    #     st.image(posters[0])
    #     st.write(names[0])
    # with col2:
    #     st.image(posters[1])
    #     st.write(names[1])
    # with col3:
    #     st.image(posters[2])
    #     st.write(names[2])
    # with col4:
    #     st.image(posters[3])
    #     st.write(names[3])
    # with col5:
    #     st.image(posters[4])
    #     st.write(names[4])
    cols=st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.write(names[i])
