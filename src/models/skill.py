from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.individual_skill import IndividualSkill
    from src.models.skill_requirement import SkillRequirement


class Skill(BaseModel):
    """
    Represents a skill in the Resource Allocation System.

    Attributes:
        id (Mapped[int]): The unique identifier for the skill.
        name (Mapped[str]): The name of the skill.
        description (Mapped[str]): A description of the skill.
        individuals (Mapped[List["IndividualSkill"]]): List of individuals possessing this skill.
        skill_requirements (Mapped[List["SkillRequirement"]]): List of project requirements needing this skill.
    """

    __tablename__ = "skills"

    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: Mapped[Optional[str]] = mapped_column(Text)

    individuals: Mapped[List["IndividualSkill"]] = relationship(back_populates="skill")
    skill_requirements: Mapped[List["SkillRequirement"]] = relationship(
        back_populates="skill"
    )

    def __repr__(self) -> str:
        return f"<Skill(id={self.id}, name='{self.name}', category='{self.category}')>"
