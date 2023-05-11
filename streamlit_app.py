import streamlit
import pandas

streamlit.title('My Mom\'s New healthy Dinner 🥣 🥗 🐔 🥑🍞')

streamlit.title('Breakfast favourites 🥣 🥗 🐔 🥑🍞')

streamlit.header('Breakfast menu 🥣 🥗 ')

streamlit.text('🐔 idly,wada,sambar')

streamlit.text('🥑🍞Poori,Chutney,sambar')

streamlit.text('🥑Dosa,Chutney,sambar')

streamlit.text('🍞idly')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
