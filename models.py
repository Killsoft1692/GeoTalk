import requests


class ZipToGeo:
    """
    Powered by GOOGLE
    Steps:
    1. Provide zip code
    2. Get country
    3. PROFIT!!
    """

    def __init__(self, zipcode):
        self.zipcode = zipcode

    @property
    def get_country(self):
        data = requests.get(f'http://maps.googleapis.com/maps/api/geocode/json?address={self.zipcode}&sensor=true').json()

        return {
            'zip_code': self.zipcode,
            'country': data['results'][0]['address_components']
        }


class GiveMeBacon:
    """
    Here is going deep magic
    """
    def __init__(self, request):
        self.request = request

    @property
    def get_meat(self):
        return requests.get('https://baconipsum.com/api/?type=meat-and-filler').json()
