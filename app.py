import streamlit as st
import pandas as pd
import numpy as np
import pickle


book_pivot = pickle.load(open('book_pivot.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def recommend_book(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestions = model.kneighbors(
        book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)
    return suggestions



# py -m streamlit run app.py
st.title('Book Recomender System')

selected_book_name = st.selectbox(
    'Select your Book',
    (book_pivot.index)

)

if st.button('Recommend'):
    st.write('Books similar to ', selected_book_name, ' are :')
    suggestions = recommend_book(
        selected_book_name)
    
    for i in range(len(suggestions)):
        print('Recomendatoin for : ', (book_pivot.index[suggestions[i][0]]))
        for j in range(5):
            j += 1
            st.text(book_pivot.index[suggestions[i][j]])
    