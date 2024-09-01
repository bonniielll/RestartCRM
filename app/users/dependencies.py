from jose import jwt
from datetime import datetime, timedelta, timezone
from app.config import get_auth_data


def create_acces_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.updae({'exp': expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=['algorithm'])
    return encode_jwt
