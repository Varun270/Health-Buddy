# Importing necessary Modules

import pytesseract as tess
import json
import os
import re
import requests
tess.pytesseract.tesseract_cmd = r'C:\Users\Varun Shrivastava\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import string
import cv2

improved_str = []
# Extracting text from Image and Storing it in a text file
im = cv2.imread("list1.jpg")

text = tess.image_to_string(im)
f = open("Ingrediants.txt", "w")
f.write(text)
f.close()


# Removing punctuations and fetching data for ingrediants
with open("Ingrediants.txt") as f:
    text = f.read()
    words = text.split(",")
    table = str.maketrans("", "", string.punctuation)
    stripped_words = [w.translate(table) for w in words]

    for word in stripped_words:
        if word[:11].lower() == "ingredients":
            improved_str.append(word[11:].replace('\n', '').replace('\x0c', ''))

        else:
            improved_str.append(word.replace('\n', '').replace('\x0c', ''))


    print(list(set(improved_str)))
    for word in list(set(improved_str)):
        url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

        querystring = {"ingr": word}

        headers = {
            "X-RapidAPI-Key": "fd93ec0010msh8fc5131067ae223p1c8310jsn02a3f8bb78fd",
            "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        # url = "https://food-ingredients-by-pti.p.rapidapi.com/api/1.0/FoodIngredients/GetIngredientDetails"
        #
        # querystring = {"ingredientName": word}
        #
        # headers = {
        #     "Content-Type": "application/json",
        #     "X-RapidAPI-Key": "fd93ec0010msh8fc5131067ae223p1c8310jsn02a3f8bb78fd",
        #     "X-RapidAPI-Host": "food-ingredients-by-pti.p.rapidapi.com"
        # }
        #
        # response = requests.request("GET", url, headers=headers, params=querystring)



        file = open("fetched_data.json", 'w')
        json.dump(response.json(), file)
    file.close()




f.close()
