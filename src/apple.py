from pyicloud import PyiCloudService


# email: srikapa03@gmail.com
# password: Example123
class Phone:
    def __init__(self, email, password):
        self.api = PyiCloudService(email, password)

    def get_location(self):
        location_dict = self.api.iphone.location()
        print(location_dict)
        return location_dict


if __name__ == "__main__":
    # username = input("Enter your username: ")
    # password = input("Enter your password: ")
    # credentials = {"username": username,
    #                "password": password}
    email = "srikapa03@icloud.com"
    password = "Virs2003"
    phone = Phone(email, password)
    phone.get_location()

