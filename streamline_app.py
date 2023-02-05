import streamlit
import pandas as pd
import requests
streamlit.title("My family's new happy diner!")
streamlit.header("Breakfast Menu")
streamlit.text("🍜Omega 3 and blueberry oatmeal")
streamlit.text("🍲kale, spinach and rocket smoothie")
streamlit.text("🍳Hard boiled free-range egg")
streamlit.text("🥑Avocado toast")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# converting into dataframe
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
