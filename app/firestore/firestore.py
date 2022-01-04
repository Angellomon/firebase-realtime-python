from functools import lru_cache

from app.config import get_settings
from loguru import logger

from .db import get_firestore_db

s = get_settings()


def on_snapshot(doc_snapshot, changes, read_time):
    logger.debug(
        f"doc_snapshot: {type(doc_snapshot)}, changes: {type(changes)}, read_time: {type(read_time)}"
    )

    db = get_firestore_db()

    for doc in doc_snapshot:
        logger.debug(f"doc_id: {doc.id}, data: {doc.to_dict()}")
        d = db.collection("usuarios").document(doc.id)

        if d is None:
            continue

        ...

        d.update({"actualizar": False})


@lru_cache
def get_watcher_usuarios():
    db = get_firestore_db()

    usuarios_col = db.collection("usuarios").where("actualizar", "==", True)

    watch_usuarios = usuarios_col.on_snapshot(on_snapshot)

    logger.debug(watch_usuarios)

    return watch_usuarios
