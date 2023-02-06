

# Python Packages:
pip install python-decouple
pip install requests

# Adding Your API Key
To add your API_KEY to the script, make a new .env file in the same directory as canvas.py, then set the API_KEY variable to your API key. 
Here is a tutorial to get a canvas token: https://www.youtube.com/watch?v=cZ5cn8stjM0

For example, if your API key is 123456789, then your .env file should look like this:

```API_KEY = 123456789```

# Adding The Canvas API_LINK
To add your API_LINK to the script, in the .env file you made add the following entry:

```API_URL = 'https://webcourses.ucf.edu'``` 

The idea here is we can try different links.

# Helpful links:

Canvas Documentation: https://canvas.instructure.com/doc/api/