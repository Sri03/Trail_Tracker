# Example nodes data
from src.DB_setup import execute_list_query, create_db_connection


connection = create_db_connection("localhost", "root", "Virs2003!SQL", "Trail_Tracker")

example_nodes = [
    (100.0, -73.95, 40.7),  # Node 1: Altitude=100.0, Longitude=-73.95, Latitude=40.7
    (200.0, -73.96, 40.71),  # Node 2: Altitude=200.0, Longitude=-73.96, Latitude=40.71
    # Add more example nodes as needed
]

# SQL query to insert nodes into the Node table
insert_query = "INSERT INTO Node (altitude, longitude, latitude) VALUES (%s, %s, %s)"

# Execute the INSERT INTO query for each example node
execute_list_query(connection, insert_query, example_nodes)
