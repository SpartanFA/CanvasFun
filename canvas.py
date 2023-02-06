from decouple import config

API_KEY = config('API_KEY')

def main():
    print(API_KEY)

main()