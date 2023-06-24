#!/usr/bin/env python3

import descifer as dsf
import mysql.connector
from mysql.connector import Error
from tkinter import *


# =====================================
# Creating Window with Tkinter
# =====================================

root = Tk()
root.title('User Data')


# =====================================
# Connecting to MySQL
# =====================================

# Creating a table inside the database
#mysql_create_table_query = """CREATE TABLE user_data (program VARCHAR(20), email VARCHAR(40), user VARCHAR(20), pwd VARCHAR(30), other VARCHAR(100));"""


def get_mysql_connection():
	conn = mysql.connector.connect(
 		host='localhost', 
 		database = 'ReadPd', 
 		user = 'root', 
 		password = 'SQLbusta4')
	return conn

def get_df_from_query(cursor, query)




# Ends loop by clicking on the cross
root.mainloop()





