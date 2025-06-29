from django.core.cache import cache
from uuid import uuid4


def create_login_token(user) -> str:
    token = str(uuid4())
    cache.set(f"login:{token}", user.phone, timeout=120)
    return token


def check_login_token(user_query, token):
    user = cache.get(f"login:{token}")
    if user is None or user != user_query.phone:
        return False
    return True


def delete_login_token(token):
    return cache.delete(f"login:{token}")
