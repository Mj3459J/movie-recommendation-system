import streamlit as st
import pandas as pd
import numpy as np
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.poster_fetcher import fetch_poster

# similarity=pickle.load(open("similarity.pkl","rb"))
movies_list=pickle.load(open("movies.pkl","rb"))

@st.cache_data
def create_similarity():
    bow_vectorizer = CountVectorizer(max_features=5000, stop_words='english')
    vectors = bow_vectorizer.fit_transform(movies_list['tags']).toarray()
    similarity = cosine_similarity(vectors)
    return similarity

similarity = create_similarity()

def recommend(movie):
    movie_index=movies_list[movies_list['title']==movie].index[0]
    distances=similarity[movie_index]
    similar_movies=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in similar_movies:
        movie_id=movies_list.iloc[i[0]].movie_id
        # Fetch poster from TMDB API 
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


