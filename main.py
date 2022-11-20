import streamlit as st
import numpy as np

st.title('Aplikasi Web Data Mining')
st.write("""
# Menggunakan beberapa algoritma dengan dataset yang sama
""")

nama_dataset = st.sidebar.selectbox(
    'Nama Dataset',
    ('Data Cryotherapy', 'Data Immunotherapy')
)

nama_algoritma = st.sidebar.selectbox(
    'Pilih Metode Algoritma',
    ('K-nearest Neighbors', 'Gaussian Naive Bayes', )
)
