from supabase import create_client, Client
import os

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")


def get_client() -> Client:
    if url is None or key is None:
        raise ValueError(
            "SUPABASE_URL e SUPABASE_KEY devem ser definidos em variáveis de ambiente.")
    return create_client(url, key)
