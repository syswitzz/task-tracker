from datetime import datetime, UTC
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey

from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=True, default=None)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    # ForeignKey links Tasks to user, but Why index=True here? ans: faster lookups
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default = lambda: datetime.now(UTC),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default= lambda: datetime.now(UTC),
        onupdate= lambda: datetime.now(UTC)
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(200), nullable=False)
    
    tasks: Mapped[list[Task]] = relationship(cascade="all, delete-orphan")  # cascade deletes users task