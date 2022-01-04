import firebase_admin
from fastapi import FastAPI
from loguru import logger

from app.firestore.auth import create_user_firebase

from .clients import create_client
from .firestore import get_watcher_usuarios
from .security import generate_password

app = FastAPI()


def on_startup():
    firebase_admin.initialize_app()
    get_watcher_usuarios()


def on_shutdown():
    watch_usuarios = get_watcher_usuarios()

    watch_usuarios.unsubscribe()


app.add_event_handler("startup", on_startup)
app.add_event_handler("shutdown", on_shutdown)


@app.get("/")
async def test():
    p = generate_password()
    user_data = {
        "display_name": "testerio",
        "email": "someone@somewhere.land",
        "password": p,
    }

    user = create_user_firebase(user_data)

    logger.debug(f"user: {user}, {p}")

    client_data = {"nombre": "test", "movimientos": [], "actualizar": False}

    client = create_client(client_data, user.uid)
    logger.debug(f"client: {client}")
