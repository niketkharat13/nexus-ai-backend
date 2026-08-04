
from sqlalchemy import DateTime, Integer, String, func, Enum
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base
from app.models.enums import Role


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    role = mapped_column(Enum(Role), nullable=False, default=Role.USER)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(), nullable=False
    )