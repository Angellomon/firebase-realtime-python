import secrets
import string

alphabet = string.ascii_letters + string.digits


def generate_password(length: int = 8):
    return "".join(secrets.choice(alphabet) for i in range(length))
