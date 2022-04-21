import streamlit as st
import pandas as pd
import numpy as np
import pickle


book_pivot = pickle.load(open('book_pivot.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))



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
    