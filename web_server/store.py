import requests
import pandas as pd

def get_categories():

    url = input("Insert Url to request: ")
    r = requests.get(url)
    #print(r.status_code)
    #print(r.text)
    #print(type(r.text))

    categories = r.json()

    for category in categories:
        print(category,"\n")
        