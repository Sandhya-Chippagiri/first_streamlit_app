import streamlit


streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast menu')
streamlit.text('🥣omega 3 and Blueberry oatmeal')
streamlit.text('🥗 Kaale, Spinach and rocket smoothie')
streamlit.text('🐔 Hard boiled free range egg')
streamlit.text(' 🥑🍞 Avacado toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
