from functools import lru_cache

from google.cloud import firestore
from loguru import logger

from app.config import get_settings

s = get_settings()


@lru_cache
def get_firestore_db() -> firestore.Client:
    logger.debug(s.GOOGLE_APPLICATION_CREDENTIALS)

    db = firestore.Client()

    return db
