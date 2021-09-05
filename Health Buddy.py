# Importing necessary Modules
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Users\Varun Shrivastava\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import string
import cv2
import wikipedia

# Extracting text from Image and Storing it in a text file
im = cv2.imread("list1.jpg")
text = tess.image_to_string(im)
f = open("Ingrediants.txt", "w")
f.write(text)
f.close()

# Removing punctuations and fetching data for ingrediants
with open("Ingrediants.txt") as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", string.punctuation)
    stripped_words = [w.translate(table) for w in words]

    for word in stripped_words:
        if word.lower() == "ingredients" or word.lower() == "ingredient":
            continue
        try:

            print(wikipedia.summary(word, sentences=3))
        except wikipedia.DisambiguationError as e:
            print("Wasn't able to detect")
f.close()
