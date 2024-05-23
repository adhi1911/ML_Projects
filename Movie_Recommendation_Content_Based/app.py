import streamlit as st
import pickle
import requests

movie_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movie_list['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=3958fb98c4daf06b7cd1df927a674850".format(movie_id))

    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommend_list = sorted(list(enumerate(distances)),reverse = True , key = lambda x:x[1])[1:11]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in recommend_list:
        movie_id = movie_list.iloc[i[0]]['movie_id']
        recommended_movies.append(movie_list.iloc[i[0]]['title'])
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies , recommended_movies_posters

st.title('Movie Recommendation System')

option = st.selectbox('Select a movie:', movies_list)

st.write('You selected:', option)
if st.button('Recommend'):
    name , posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6 , col7 , col8 , col9 , col10 = st.columns(5)
    with col1:
        st.write(name[0])
        st.image(posters[0])
    with col2:
        st.write(name[1])
        st.image(posters[1])
    with col3:
        st.write(name[2])
        st.image(posters[2])
    with col4:
        st.write(name[3])
        st.image(posters[3])
    with col5:
        st.write(name[4])
        st.image(posters[4])
    with col6:
        st.write(name[5])
        st.image(posters[5])
    with col7:
        st.write(name[6])
        st.image(posters[6])
    with col8:
        st.write(name[7])
        st.image(posters[7])
    with col9:
        st.write(name[8])
        st.image(posters[8])
    with col10:
        st.write(name[9])
        st.image(posters[9])
        

