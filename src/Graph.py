import time

from DB_setup import execute_list_query, create_db_connection
from src.phone import Phone


# email: srikapa03@gmail.com
# password: Example123
def add_nodes(phone):
    """
        Collects GPS location data from a phone at 30-second intervals for 15 minutes
        and inserts the collected data into a MySQL database.

        Args:
            phone: An object that has a method `get_location` which returns the current
                   GPS location as a tuple (altitude, longitude, latitude).

        The function performs the following steps:
            1. Initializes an empty list to store the node data.
            2. Collects GPS data every 30 seconds for a total duration of 15 minutes (30 intervals).
            3. Establishes a connection to a MySQL database.
            4. Inserts the collected GPS data into a table named 'Nodes' in the database.
            5. Closes the database connection.
    """
    node_list = []
    # make while loop wait for signal (ie keyboard click)
    for i in range(30):
        time.sleep(30)
        node_list.append(phone.get_location())

    connection = create_db_connection("localhost", "root", "Virs2003!SQL", "Trail_Tracker")
    query = "INSERT INTO Nodes (Altitude, Longitude, Latitude) VALUES (%s, %s, %s)"
    execute_list_query(connection, query, node_list)
    connection.close()


if __name__ == "__main__":
    # username = input("Enter your username: ")
    # password = input("Enter your password: ")
    # credentials = {"username": username,
    #                "password": password}
    email = "srikapa03@icloud.com"
    password = "Virs2003"
    phone = Phone(email, password)
    phone.get_location()
