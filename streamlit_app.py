import streamlit
import pandas
streamlit.title('😎This is My streamlit Application')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_file = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_file = my_file.set_index('Fruit')
fruit_selected=streamlit.multiselect("Pick Some Fruits:",list(my_file.index),['Avocado','Strawberries'])
fruit_to_show=my_file.loc[fruit_selected]
#streamlit.multiselect("Pick Some Fruits:",list(my_file.Fruit))
streamlit.dataframe(fruit_to_show)
