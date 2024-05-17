from pyicloud import PyiCloudService


class Phone:
    def __init__(self, email, password):
        self.api = PyiCloudService(email, password)

    def get_location(self):
        location_dict = self.api.iphone.location()
        altitude = location_dict.altitude
        longitude = location_dict.longitude
        latitude = location_dict.latitude

        return altitude, longitude, latitude
