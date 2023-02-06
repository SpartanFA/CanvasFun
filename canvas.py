from decouple import config
import requests


API_KEY = config('API_KEY')
API_URL = config('API_URL')
API_TOKEN_IDENTIFIER = '?access_token=' # If using OAuth, this should be different.

def main():
    response = execute('GET', '/api/v1/courses', '')

    print()
    #print(response.json())
    # for item in response.json():
    #     for key in item:
    #         if (key == 'name'):
    #             print(key, item[key])

    print(response.json())
                

def test():
        response = requests.get(API_URL + '/api/v1/courses/1424216/permissions?access_token=' + API_KEY)
    #print(response.json())
    # for item in response.json():
    #     for key in item:
    #         if (key == 'name'):
    #             print(key, item[key])

        print(response.json())

def execute(type, url, data):
    if (type == 'GET'):
        response = requests.get(API_URL + url + API_TOKEN_IDENTIFIER + API_KEY)
    elif (type == 'POST'):
        response = requests.post(API_URL + url + API_TOKEN_IDENTIFIER + API_KEY, data)
    elif (type == 'PUT'):
        response = requests.put(API_URL + url + API_TOKEN_IDENTIFIER + API_KEY, data)
    elif (type == 'DELETE'):
        response = requests.delete(API_URL + url + API_TOKEN_IDENTIFIER + API_KEY)
    else:
        print('Invalid request type')
        return None

    return response

main()