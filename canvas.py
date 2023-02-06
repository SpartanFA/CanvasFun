from decouple import config

#
# To add your API_KEY to the script, make a new .env file in the same directory as canvas.py, then set the API_KEY variable to your API key. 
# Here is a tutorial to get a canvas token: https://www.youtube.com/watch?v=cZ5cn8stjM0
# For example, if your API key is 123456789, then your .env file should look like this:
# API_KEY = 123456789
#

API_KEY = config('API_KEY')

def main():
    print(API_KEY)

main()