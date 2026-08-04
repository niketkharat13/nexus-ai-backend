from datetime import datetime, timedelta, UTC

from jose import jwt

from app.core.config import settings

ALGORITHM = "HS256"


def create_access_token(
    subject: str,
    expires_in_minutes: int = 30,
) -> str:
    expire = datetime.now(UTC) + timedelta(minutes=expires_in_minutes)

    payload = {
        "sub": subject,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )
    
