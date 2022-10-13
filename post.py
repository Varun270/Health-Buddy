import pymongo
import os
from Health_Buddy import extract_words, fetch_data
from dotenv import load_dotenv

load_dotenv()
Ingredients_list = extract_words()


def insert_data(client, db):
    """

    :param client: client for mongodb database
    :param db: database in which the data is to be added
    :return: None
    """
    for word in Ingredients_list:
        collection.insert_one(fetch_data(word))

    print("Collection Creation Success!!!")


if __name__ == '__main__':
    client = pymongo.MongoClient(os.getenv("connection_string"))
    db = client["MajorP"]
    collection = db["IngredientsDetails"]
    # print(client)
    insert_data(client, db)
