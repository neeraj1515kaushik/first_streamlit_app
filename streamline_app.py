import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError
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
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#fruityvice_normalized = fruityvice_response.json()
streamlit.text(fruityvice_response.json())
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_juice(fruit_choice)
        streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()
  
  streamlit.write('The user entered ', fruit_choice)

# converting into dataframe


#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchall()

#streamlit.text("The loaded fruit list items are:")
#streamlit.dataframe(my_data_row)

#fruit_choice = streamlit.text_input('What fruit would you like to add?')
#streamlit.text("Thanks for adding " + fruit_choice)
