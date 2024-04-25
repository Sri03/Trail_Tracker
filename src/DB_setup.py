from pyicloud import PyiCloudService

"""
flow to interact with database: 

1. connect to server with create_server_connection()
2. create database if it doesn't exist with create_database()'
3. connect to database with create_database_connection()
4. create query
5. execute query with execute_query()
"""

import mysql.connector
from mysql.connector import Error
import pandas as pd

pw = "Virs2003!SQL"
db = "school"


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("mysql connection established")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# # 1. create connection
# connection = create_server_connection("localhost", "root", pw)
#
# # 2. create database if doesn't exist
# create_database(connection, "CREATE DATABASE IF NOT EXISTS Trail_Tracker")
#
# # 3. connect to database
# connection = create_db_connection("localhost", "root", "Virs2003!SQL", "Trail_Tracker")
#
# # 4. create query
# create_tables = """
#     CREATE TABLE Node (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     altitude FLOAT,
#     longitude FLOAT,
#     latitude FLOAT
#     );
#     """
#
# # 5. execute query
# execute_query(connection, create_tables)
