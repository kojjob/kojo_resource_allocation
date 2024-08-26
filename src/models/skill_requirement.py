from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.project_requirement import ProjectRequirement
    from src.models.skill import Skill


class SkillRequirement(BaseModel):
    """
    Represents the relationship between a project requirement and a required skill in the Resource Allocation System.

    Attributes:
        requirement_id (Mapped[int]): The ID of the project requirement.
        skill_id (Mapped[int]): The ID of the required skill.
        minimum_proficiency (Mapped[int]): The minimum proficiency level required for the skill.
        requirement (Mapped["ProjectRequirement"]): The associated project requirement.
        skill (Mapped["Skill"]): The associated skill.
    """

    __tablename__ = "skill_requirements"

    requirement_id: Mapped[int] = mapped_column(
        ForeignKey("project_requirements.id"), nullable=False
    )
    skill_id: Mapped[int] = mapped_column(ForeignKey("skills.id"), nullable=False)
    minimum_proficiency: Mapped[int] = mapped_column(Integer, nullable=False)

    # Composite unique constraint
    __table_args__ = (
        PrimaryKeyConstraint("id"),  # Primary key on the unique ID
        UniqueConstraint("requirement_id", "skill_id"),  # Composite unique constraint
    )

    requirement: Mapped["ProjectRequirement"] = relationship(
        back_populates="skill_requirements"
    )
    skill: Mapped["Skill"] = relationship(back_populates="skill_requirements")

    def __repr__(self) -> str:
        return f"<SkillRequirement(requirement_id={self.requirement_id}, skill_id={self.skill_id}, minimum_proficiency={self.minimum_proficiency})>"
