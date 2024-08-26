from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.individual import Individual
    from src.models.project_requirement import ProjectRequirement


class Assignment(BaseModel):
    """
    Represents an assignment of an individual to a project requirement in the Resource Allocation System.

    Attributes:
        id (Mapped[int]): The unique identifier for the assignment.
        individual_id (Mapped[int]): The ID of the assigned individual.
        requirement_id (Mapped[int]): The ID of the project requirement.
        start_date (Mapped[date]): The start date of the assignment.
        end_date (Mapped[date]): The end date of the assignment.
        status (Mapped[str]): The status of the assignment.
        individual (Mapped["Individual"]): The assigned individual.
        requirement (Mapped["ProjectRequirement"]): The associated project requirement.
    """

    __tablename__ = "assignments"

    individual_id: Mapped[int] = mapped_column(
        ForeignKey("individuals.id"), nullable=False, index=True
    )
    requirement_id: Mapped[int] = mapped_column(
        ForeignKey("project_requirements.id"), nullable=False, index=True
    )
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String(20))

    individual: Mapped["Individual"] = relationship(back_populates="assignments")
    requirement: Mapped["ProjectRequirement"] = relationship(
        back_populates="assignments"
    )

    def __repr__(self) -> str:
        return f"<Assignment(id={self.id}, individual_id={self.individual_id}, requirement_id={self.requirement_id}, status='{self.status}')>"
