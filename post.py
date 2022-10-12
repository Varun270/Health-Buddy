import pymongo
from Health_Buddy import extract_words, fetch_data

Ingredients_list = extract_words()


if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["MajorP"]
    collection = db["IngredientsDetails"]
    for word in Ingredients_list:
        collection.insert_one(fetch_data(word))



