from pymongo import MongoClient

client = MongoClient(f"mongodb://admin:password123@mongodb:27017/?authSource=admin")
db = client["cartelera"]
collection = db["peliculas"]

