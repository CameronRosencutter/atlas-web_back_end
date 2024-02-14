#!/usr/bin/env python3
'''8-all.py'''

import pymongo

def list_all(mongo_collection):
    """this will define all"""
    # Find all documents in the collection
    documents = mongo_collection.find({})
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate through the documents and append them to the result list
    for doc in documents:
        result.append(doc)
    
    return result
