import threading

from fastapi import FastAPI
from loguru import logger

from .firestore import get_firestore_db

usuarios_done = threading.Event()


def test_print_doc():
    db = get_firestore_db()

    doc = db.collection("usuarios").document("1cVZmKPpbzLiGdQthnqT")

    logger.debug(doc.get().to_dict())


def on_snapshot(doc_snapshot, changes, read_time):
    logger.debug(
        f"doc_snapshot: {type(doc_snapshot)}, changes: {type(changes)}, read_time: {type(read_time)}"
    )
    for doc in doc_snapshot:
        logger.debug(f"doc_id: {doc.id}, data: {doc.to_dict()}")

    usuarios_done.set()


def test_on_snapshot():
    db = get_firestore_db()

    usuarios_col = db.collection("usuarios")

    watch_usuarios = usuarios_col.on_snapshot(on_snapshot)

    logger.debug(watch_usuarios)

    usuarios_done.wait()


def main():

    test_print_doc()
    test_on_snapshot()


if __name__ == "__main__":
    main()
