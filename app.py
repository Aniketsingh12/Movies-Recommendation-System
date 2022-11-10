import streamlit as st 
import pickle as pl 
import pandas as pd 

st.title('Movies Recommendation System')
movies = pl.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies)
select = st.selectbox('Movies' , movies['title'])

similarity = pl.load(open('similarity.pkl','rb'))

def recommend(movie):
    ind = movies[movies['title']==movie].index[0]
    dis = similarity[ind]
    movie_list = sorted(list(enumerate(dis)),reverse=True , key = lambda x :x[1] )[1:6]
    recom = []
    for i in movie_list:
        id = movies.iloc[i[0]].movie_id
        recom.append(movies.iloc[i[0]].title)
    return recom 

if st.button('Recommend'):
    names = recommend(select)
    for i in range(len(names)):
        st.text(names[i])

    
    
            
        

