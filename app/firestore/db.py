from functools import lru_cache

from firebase_admin import firestore


@lru_cache
def get_firestore_db() -> firestore.Client:
    db = firestore.Client()

    return db
