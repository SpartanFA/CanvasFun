from decouple import config
import requests


API_KEY = config('API_KEY')
API_URL = config('API_URL')
API_TOKEN_IDENTIFIER = '?access_token=' # If using OAuth, this should be different.

def listOfClasses():
    response = requests.get(API_URL + '/api/v1/courses' + API_TOKEN_IDENTIFIER + API_KEY + '&per_page=100')
    for item in response.json():
        for key in item:
            if (key == 'name'):
                print("%-50s %4.1d" % (item['name'], item['id'])) # This is just some formatting I found online

def test():
        response = requests.get(API_URL + '/api/v1/courses/1424216/permissions?access_token=' + API_KEY)
    #print(response.json())
    # for item in response.json():
    #     for key in item:
    #         if (key == 'name'):
    #             print(key, item[key])

        print(response.json())


listOfClasses()