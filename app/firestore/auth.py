from typing import Dict

from firebase_admin import auth


def create_user_firebase(user_data: Dict[str, str]):
    return auth.create_user(**user_data)
