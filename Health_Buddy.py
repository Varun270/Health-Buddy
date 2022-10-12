# Importing necessary Modules

import pytesseract as tess
import json
import os
import re
import requests
from dotenv import load_dotenv
load_dotenv()
tess.pytesseract.tesseract_cmd = r'C:\Users\Varun Shrivastava\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import string
import cv2

improved_str = []

im = cv2.imread("list1.jpg")

text = tess.image_to_string(im)
f = open("Ingrediants.txt", "w")
f.write(text)
f.close()



def extract_words(filename="Ingrediants.txt"):
    """
    :param filename: Extracted ingredients will be saved here.
    :return: List of Ingredients
    """
    with open(filename) as f:
        text = f.read()
        words = text.split(",")
        table = str.maketrans("", "", string.punctuation)
        stripped_words = [w.translate(table) for w in words]

        for word in stripped_words:
            if word[:11].lower() == "ingredients":
                improved_str.append(word[11:].replace('\n', '').replace('\x0c', ''))

            else:
                improved_str.append(word.replace('\n', '').replace('\x0c', ''))
    f.close()
    return list(set(improved_str))

def fetch_data(word):
    """

    :param word: Ingredient for which API sends a GET Request
    :return: JSON Object consisting information about ingredient
    """
    url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

    querystring = {"ingr": word}
    headers = {
        "X-RapidAPI-Key": os.getenv("API_KEY"),
        "X-RapidAPI-Host": os.getenv("Host")
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()












