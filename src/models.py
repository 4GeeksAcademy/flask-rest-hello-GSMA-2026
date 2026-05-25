from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone

db = SQLAlchemy()

class User(db.Model):
    _tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80),unique=True,nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))
    


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey('user.id'))
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))
    user = relationship("User")

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(250),nullable=False)
    user_id : Mapped[int] = mapped_column(ForeignKey('user.id'))
    post_id : Mapped[int] = mapped_column(ForeignKey('post.id'))
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))
    user = relationship("User")
    post = relationship("Post")


class Followers(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    follower_id : Mapped[int] = mapped_column(ForeignKey('user.id'))
    following_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))
    follower = relationship( "User",foreign_keys=[follower_id])
    following = relationship("User",foreign_keys=[following_id])


def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
