import streamlit
import pandas

streamlit.title("My parents' new healthy diner!") #Title of page

streamlit.header("Breakfast favourites") #Header

streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") #creating a data frame from our csv file
my_fruit_list = my_fruit_list.set_index('Fruit') # Choosing fruit name column as index

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado' , 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Displaying the table
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!") # New section to display fruityvice api response
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Takes json version of the response and normalizes it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Outputs to the screen as table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#Allowing user to add fruit of his/her choice
add_my_fruit = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
