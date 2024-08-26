from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.role import Role


class RoleType(BaseModel):
    """
    Represents a role type in the Resource Allocation System.

    Attributes:
        id (Mapped[int]): The unique identifier for the role type.
        name (Mapped[str]): The name of the role type.
        roles (Mapped[List["Role"]]): List of roles associated with this role type.
    """

    __tablename__ = "role_types"

    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    roles: Mapped[List["Role"]] = relationship(back_populates="role_type")

    def __repr__(self) -> str:
        return f"<RoleType(id={self.id}, name='{self.name}')>"
