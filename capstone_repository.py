from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["capstone_repository"]
collection = db["capstones"]

def validate_capstone(doc):
    required_fields = [
        "title",
        "abstract",
        "specialization",
        "year",
        "keywords",
        "recommendations_text",
        "summary_conclusion",
        "vectors"
    ]

    for field in required_fields:
        if field not in doc:
            raise ValueError(f"Missing field: {field}")
        
    if doc["specialization"] not in ["web", "database", "network"]:

        raise ValueError("Invalid specialization")

validate_capstone(capstone)
collection.insert_one(capstone)
