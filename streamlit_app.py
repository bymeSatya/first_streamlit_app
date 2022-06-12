import streamlit
import pandas
import requests

streamlit.title('😎This is My streamlit Application')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_file = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_file = my_file.set_index('Fruit')
fruit_selected=streamlit.multiselect("Pick Some Fruits:",list(my_file.index))
# streamlit.dataframe(my_file)
fruit_to_show=my_file.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)


streamlit.title('Fruityvice Fruit Advice')
fruity_responce=requests.get('https://fruityvice.com/api/fruit/'+"kiwi")
#streamlit.text(fruity_responce.json())
fruity_normalize = pandas.json_normalize(fruity_responce.json())
streamlit.dataframe(fruity_normalize)
