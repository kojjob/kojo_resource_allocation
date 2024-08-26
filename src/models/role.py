from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.individual_role import IndividualRole
    from src.models.role_level import RoleLevel
    from src.models.role_requirement import RoleRequirement
    from src.models.role_type import RoleType


class Role(BaseModel):
    """
    Represents a role in the Resource Allocation System.

    Attributes:
        id (Mapped[int]): The unique identifier for the role.
        name (Mapped[str]): The name of the role.
        description (Mapped[str]): A description of the role.
        role_type_id (Mapped[int]): The ID of the associated role type.
        role_level_id (Mapped[int]): The ID of the associated role level.
        role_type (Mapped["RoleType"]): The associated role type.
        role_level (Mapped["RoleLevel"]): The associated role level.
        individuals (Mapped[List["IndividualRole"]]): List of individuals assigned this role.
        role_requirements (Mapped[List["RoleRequirement"]]): List of project requirements needing this role.
    """

    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    role_level_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("role_levels.id"), nullable=False
    )
    role_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("role_types.id"), nullable=False
    )

    # Foreign keys for RoleLevel and RoleType
    role_level: Mapped["RoleLevel"] = relationship(back_populates="roles")
    role_type: Mapped["RoleType"] = relationship(back_populates="roles")

    # Relationship
    role_requirements: Mapped[List["RoleRequirement"]] = relationship(
        back_populates="role"
    )
    individuals: Mapped[List["IndividualRole"]] = relationship(back_populates="role")

    def __repr__(self) -> str:
        return f"<Role(id={self.id}, name='{self.name}')>"
