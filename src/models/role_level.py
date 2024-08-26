from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.role import Role


class RoleLevel(BaseModel):
    """
    Represents a role level in the Resource Allocation System.

    Attributes:
        id (Mapped[int]): The unique identifier for the role level.
        name (Mapped[str]): The name of the role level.
        roles (Mapped[List["Role"]]): List of roles associated with this level.
    """

    __tablename__ = "role_levels"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    roles: Mapped[List["Role"]] = relationship(back_populates="role_level")

    def __repr__(self) -> str:
        return f"<RoleLevel(id={self.id}, name='{self.name}')>"
