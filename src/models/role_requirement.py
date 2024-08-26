from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

if TYPE_CHECKING:
    from src.models.project_requirement import ProjectRequirement
    from src.models.role import Role


class RoleRequirement(BaseModel):
    __tablename__ = "role_requirements"

    # Override the id column in the BoseModel
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Foreign keys to related tables
    requirement_id: Mapped[int] = mapped_column(
        ForeignKey("project_requirements.id"), nullable=False
    )
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)

    # Number of individuals with this role needed for the requirement
    number_needed: Mapped[int] = mapped_column(Integer, nullable=False)

    # Ensure uniqueness of requirement-role combination
    __table_args__ = (
        UniqueConstraint("requirement_id", "role_id", name="uq_role_requirement"),
    )

    # Relationships to related models
    requirement: Mapped["ProjectRequirement"] = relationship(
        back_populates="role_requirements"
    )
    role: Mapped["Role"] = relationship(back_populates="role_requirements")

    def __repr__(self) -> str:
        """String representation of the RoleRequirement instance."""
        return f"<RoleRequirement(id={self.id}, requirement_id={self.requirement_id}, role_id={self.role_id}, number_needed={self.number_needed})>"
