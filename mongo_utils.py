import pymongo
from config import app_config


# Generic functions
def get_db_client():
    """Returns MongoDB client object, connect to MongoDB Atlas instances if required"""
    try:
        if app_config.mongo_client == None:
            client = pymongo.MongoClient(app_config.MONGO_CONN_STR)
            app_config.mongo_client = client
    except Exception as e:
        print(e)
    return app_config.mongo_client


def fetch_document(client, db, collection):
    """Get a single document from the provided db and collection"""
    try:
        document = client[db][collection].find_one()
    except Exception as e:
        print(e)
    return document


def update_document(client, db, collection, key, value):
    """Update the passed key in the document for provided db and collection"""
    try:
        document = fetch_document(client, db, collection)
        client[db][collection].update_one(
            {"_id": document["_id"]},
            {"$set": {key: value}},
        )
    except Exception as e:
        print(e)


# Use case specific functions
def fetch_curr_access_count():
    client = get_db_client()
    curr_count = fetch_document(
        client=client, db=app_config.db, collection=app_config.collection
    )[app_config.key]
    app_config.openai_curr_access_count = curr_count


def increment_curr_access_count():
    client = get_db_client()
    updated_count = app_config.openai_curr_access_count + 1
    update_document(
        client=client,
        db=app_config.db,
        collection=app_config.collection,
        key=app_config.key,
        value=updated_count,
    )
    app_config.openai_curr_access_count = updated_count
