import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text(':bowl_with_spoon:  Omega 3 & Blueberry Oatmeal')
streamlit.text(':green_salad: Kale ,Spinach & Rocket Smoothy')
streamlit.text(':hamburger: Burger, Pizza & pastas')
streamlit.text(':avocado::bread: Avocado Toast')
streamlit.header(':banana::mango: Build Your Own Fruit Smoothie :kiwifruit::grapes:')
#adding the table
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#multiselect function
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#a function for repeatly running the code
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
#TO GET FUTIVICE API RESPONSE I.E BY REQUESTS
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
streamlit.header("The Fruitload List Contains:")
#Snowflake related function
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT* FROM FRUIT_LOAD_LIST")
      return my_cur.fetchall()
if streamlit.button('Get fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)
#
#End user to add the fruit
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values('" +new_fruit + "')")
      return "Thanks for adding " +  new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
