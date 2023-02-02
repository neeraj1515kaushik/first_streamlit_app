import streamlit
import pandas as pd
streamlit.title("My family's new happy diner!")
streamlit.header("Breakfast Menu")
streamlit.text("🍜Omega 3 and blueberry oatmeal")
streamlit.text("🍲kale, spinach and rocket smoothie")
streamlit.text("🍳Hard boiled free-range egg")
streamlit.text("🥑Avocado toast")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit))
streamlit.dataframe(my_fruit_list)

