from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreateRequest

class UserService:
    def __init__(self, db: AsyncSession, repository: UserRepository):
        self.repository = repository
        self.db = db
        
    async def create_user(self, request: UserCreateRequest):
        existing_user = await self.repository.get_by_email(email=request.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists.",
            )
        user = User(
            name=request.name,
            email=request.email,
            age = request.age,
            password_hash = hash_password(request.password)
        )
        try:
            created_user = await self.repository.create(user)
            await self.db.commit()
            return created_user
        except Exception:
            await self.db.rollback()
            raise

    