from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def utc_now() -> datetime:
    """
    Get the current UTC timestamp.

    Returns:
        datetime: Current UTC datetime.
    """
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    """
    Base class for declarative SQLAlchemy models.

    This class should be used as the base for all ORM models in the project.
    It provides the necessary setup for declarative model definition.
    """

    pass


class BaseModel(Base):
    """
    Base model with common fields for all models.

    This abstract base class provides common fields that should be
    present in all database models, such as id, created_at, and updated_at.
    All other models in the system should inherit from this class.

    Attributes:
        id (Mapped[int]): Primary key for the model.
        created_at (Mapped[datetime]): UTC timestamp of when the record was created.
        updated_at (Mapped[Optional[datetime]]): UTC timestamp of when the record was last updated.
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
        comment="UTC timestamp of when the record was created",
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        comment="UTC timestamp of when the record was last updated",
    )

    def __repr__(self) -> str:
        """
        Return a string representation of the model.

        This method provides a default implementation for all models,
        showing the model's class name and id.

        Returns:
            str: A string representation of the model instance.
        """
        return f"<{self.__class__.__name__}(id={self.id})>"
