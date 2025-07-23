import streamlit as st
import pickle
import pandas as pd

similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(options):
    val = movies[movies['title'] == options].index[0]
    distances = similarity[val]
    recommended_movies=[]
    result = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in result:
        recommended_movies.append(movies.loc[i[0],'title'])
    return recommended_movies

movies_dict = pickle.load(open('movies.dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender System')

options = st.selectbox('Enter your choice',movies['title'].values)

if(st.button('recommend')):
    recommendations = recommend(options)
    for i in recommendations:
        st.write(i)
