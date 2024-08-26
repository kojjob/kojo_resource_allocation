from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.project_requirement import ProjectRequirement


class TimeRequirement(BaseModel):
    """
    Represents a time requirement for a project requirement in the Resource Allocation System.

    Attributes:
        id (Mapped[int]): The unique identifier for the time requirement.
        requirement_id (Mapped[int]): The ID of the associated project requirement.
        hours_per_week (Mapped[int]): The number of hours required per week.
        total_hours (Mapped[int]): The total number of hours required.
        project_requirement (Mapped["ProjectRequirement"]): The associated project requirement.
    """

    __tablename__ = "time_requirements"

    requirement_id: Mapped[int] = mapped_column(
        ForeignKey("project_requirements.id"), unique=True, nullable=False
    )
    hours_per_week: Mapped[int] = mapped_column(Integer, nullable=False)
    total_hours: Mapped[int] = mapped_column(Integer, nullable=False)

    project_requirement: Mapped["ProjectRequirement"] = relationship(
        back_populates="time_requirement"
    )

    def __repr__(self) -> str:
        return f"<TimeRequirement(id={self.id}, requirement_id={self.requirement_id}, hours_per_week={self.hours_per_week}, total_hours={self.total_hours})>"
