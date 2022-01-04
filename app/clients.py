from typing import Dict

from .firestore import get_firestore_db


def create_client(client_data: Dict[str, str], user_id: str):
    db = get_firestore_db()

    client_ref = db.collection("usuarios").document(user_id)
    client_ref.set(client_data)

    return client_ref
