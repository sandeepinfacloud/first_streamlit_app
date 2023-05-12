import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Mom\'s New healthy Dinner 🥣 🥗 🐔 🥑🍞')

streamlit.title('Breakfast favourites 🥣 🥗 🐔 🥑🍞')

streamlit.header('Breakfast menu 🥣 🥗 ')

streamlit.text('🐔 idly,wada,sambar')

streamlit.text('🥑🍞Poori,Chutney,sambar')

streamlit.text('🥑Dosa,Chutney,sambar')

streamlit.text('🍞idly')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(fruits_to_show)


def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#new section to displau fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:  
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("please select a fruit to get information")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
        
except URLError as e:
        streamlit.error()
        #streamlit.stop()
    
#import snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)

streamlit.header("View Our Fruit List - Add Your Favorites!:")

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

# Snowflake related funtions

def get_fruit_load_list():

              with my_cnx.cursor() as my_cur:

                           my_cur.execute("SELECT * from fruit_load_list")

                           return my_cur.fetchall()


# Add a button to load the fruit

if streamlit.button('Get Fruit List'):
              my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

              my_data_rows = get_fruit_load_list()

              my_cnx.close()

              streamlit.dataframe(my_data_rows)
              


# allow end user to add a fruit to the list

def insert_row_snowflake(new_fruit):

              with my_cnx.cursor() as my_cur:

                           my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('" + add_my_fruit +"')")

                           return streamlit.write('Thanks for adding ', add_my_fruit)


add_my_fruit = streamlit.text_input('What fruit would you like information about?','jackfruit')

if streamlit.button('Add a Fruit to the List'):

              my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

              back_from_function = insert_row_snowflake(add_my_fruit)

              streamlit.text(back_from_function)

              my_cnx.close()

# streamlit.write('Thanks for adding ', add_my_fruit)

# my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains2:")
# streamlit.dataframe(my_data_rows)

# streamlit.dataframe(fruits_to_show)
