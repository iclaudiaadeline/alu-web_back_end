#!/usr/bin/env python3
"""python scripts"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """script that provides some stats about Nginx logs stored in MongoDB"""
    if option:
        print(f"\tmethod {option}: "
              f"{mongo_collection.count_documents({'method': option})}")
        return
    print(f"{mongo_collection.count_documents({})} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(mongo_collection, method)
    print(f"{mongo_collection.count_documents({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    log_stats(MongoClient('mongodb://127.0.0.1:27017').logs.nginx)
