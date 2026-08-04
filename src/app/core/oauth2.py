from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings

oauth_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)