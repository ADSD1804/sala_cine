import os
import libsql_client
from dotenv import load_dotenv

load_dotenv()

_client = None


def get_client():
    global _client

    if _client is None:
        database_url = os.getenv("DATABASE_URL")
        api_key = os.getenv("API_KEY")

        if not database_url:
            raise RuntimeError(
                "No se encontró DATABASE_URL en el archivo .env"
            )

        if not api_key:
            raise RuntimeError(
                "No se encontró API_KEY en el archivo .env"
            )

        _client = libsql_client.create_client_sync(
            url=database_url,
            auth_token=api_key
        )

    return _client


def test_connection():
    client = get_client()

    try:
        client.execute("SELECT 1")
        return True

    except Exception as error:
        print(error)
        return False