from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import decode_accesstoken
from app.db.database import get_db
from app.models.enums import Role
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from app.core.oauth2 import oauth_scheme


def get_user_repository(
    db: AsyncSession = Depends(get_db),
) -> UserRepository:
    return UserRepository(db)


def get_user_service(
    repository: UserRepository = Depends(get_user_repository),
    db: AsyncSession = Depends(get_db),
) -> UserService:
    return UserService(db, repository)

def get_auth_service(
    repository: UserRepository = Depends(get_user_repository),
    db: AsyncSession = Depends(get_db),
) -> AuthService:
    return AuthService(
        repository=repository,
        db=db,
    )
    
async def get_current_user(
        token: str = Depends(oauth_scheme),
        repository: UserRepository = Depends(get_user_repository),
    ):
        payload = decode_accesstoken(token)

        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )

        subject = payload.get("sub")

        if subject is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )

        user = await repository.get_by_id(int(subject))

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )

        return user
    
    
def permission_check(role: Role):
    async def checker(current_user: User = Depends(get_current_user)):
        if current_user.role != role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You dont have permission"
            )
        return current_user
    return checker
    