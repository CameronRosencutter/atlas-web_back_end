#!/usr/bin/env python3
""" 9_insert_school"""

def insert_school(mongo_collection, **kwargs):
    """This wil define the school"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
