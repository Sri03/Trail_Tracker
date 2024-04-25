from pyicloud import PyiCloudService

# email: srikapa03@gmail.com
# password: Virs2003


if __name__ == "__main__":

    # username = input("Enter your username: ")
    # password = input("Enter your password: ")
    # credentials = {"username": username,
    #                "password": password}
    api = PyiCloudService("srikapa03@gmail.com", "Virs2003")
    print(api.devices)
    location_dict = api.iphone.location()
    print(location_dict['longitude'])
