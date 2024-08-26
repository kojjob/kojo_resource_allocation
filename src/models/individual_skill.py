from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

if TYPE_CHECKING:
    from src.models.individual import Individual
    from src.models.skill import Skill


class IndividualSkill(BaseModel):
    __tablename__ = "individual_skills"
    __table_args__ = (
        UniqueConstraint("individual_id", "skill_id", name="uq_individual_skill"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    individual_id: Mapped[int] = mapped_column(
        ForeignKey("individuals.id"), nullable=False
    )
    skill_id: Mapped[int] = mapped_column(ForeignKey("skills.id"), nullable=False)
    proficiency_level: Mapped[int] = mapped_column(Integer, nullable=False)

    individual: Mapped["Individual"] = relationship(back_populates="skills")
    skill: Mapped["Skill"] = relationship(back_populates="individuals")

    def __repr__(self) -> str:
        return f"<IndividualSkill(id={self.id}, individual_id={self.individual_id}, skill_id={self.skill_id}, proficiency_level={self.proficiency_level})>"
