from pyicloud import PyiCloudService

"""
GPS responsible for tracking phone and calculating distance
"""
class GPS:
    def __init__(self, api: PyiCloudService):
        self.api = api
        self.iphone = api.iphone
    # def get_location(self, ):

