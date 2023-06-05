from pymongo import MongoClient
import os
from dotenv import load_dotenv
import random

load_dotenv()

client = MongoClient(os.getenv('MONGO_URL'))
db = client[os.getenv('MONGO_DB')]
collection = db[os.getenv('MONGO_COLLECTION')]
url_length = int(os.getenv('URL_LENGTH'))
site_url = os.getenv('SITE_URL')


def create_shortened_url(url, defined_shortened_url=None):
    if defined_shortened_url is not None:
        shortened_url = defined_shortened_url
    else:
        shortened_url = generate_random_string()
    document = {
        "url": url,
        "shortened_url": shortened_url
    }
    if check_if_shortened_url_exists(document["shortened_url"]):
        document["shortened_url"] = generate_random_string()
    if check_if_original_url_exists(url):
        exist_data = collection.find_one({"url": url})
        return exist_data["shortened_url"]
    else:
        collection.insert_one(document)
        return document["shortened_url"]

def generate_random_string():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(letters) for i in range(url_length))

def check_if_original_url_exists(url):
    if collection.find_one({"url": url}) is None:
        return False
    else:
        return True

def check_if_shortened_url_exists(random_string):
    if collection.find_one({"shortened_url": random_string}) is None:
        return False
    else:
        return True

def get_original_url(shortened_url):
    if check_if_shortened_url_exists(shortened_url):
        exist_data = collection.find_one({"shortened_url": shortened_url})
        return exist_data["url"]
    else:
        return None