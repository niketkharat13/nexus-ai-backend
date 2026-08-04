from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.jwt import create_access_token
from app.core.security import hash_password, verify_password
from app.models.enums import Role
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse


class AuthService:
    def __init__(
        self,
        repository: UserRepository,
        db: AsyncSession,
    ):
        self.repository = repository
        self.db = db

    async def register(self, request: RegisterRequest) -> User:
        existing_user = await self.repository.get_by_email(request.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists.",
            )

        user = User(
            name=request.name,
            email=request.email,
            password_hash=hash_password(request.password),
            age=request.age,
            role=Role.USER
        )

        try:
            created_user = await self.repository.create(user)

            await self.db.commit()

            return created_user

        except Exception:
            await self.db.rollback()
            raise
        
    async def login(self, email: str, password: str) -> User:
        user = await self.repository.get_by_email(email)
        if not user:
           raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )
        if not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )
        token = create_access_token(subject=str(user.id))
        return TokenResponse(access_token=token)
            
        