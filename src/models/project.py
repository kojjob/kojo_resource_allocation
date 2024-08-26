from datetime import date
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.client import Client
    from src.models.project_requirement import ProjectRequirement


class Project(BaseModel):
    """
    Represents a project in the Resource Allocation System.

    Attributes:
        id (Mapped[int]): The unique identifier for the project.
        client_id (Mapped[int]): The ID of the associated client.
        name (Mapped[str]): The name of the project.
        desription (Mapped[srt]): A description of the project. Type text.
        start_date (Mapped[date]): The start date of the project.
        end_date (Mapped[date]): The end date of the project.
        status (Mapped[str]): The current status of the project.
        client (Mapped["Client"]): The associated client.
        requirements (Mapped[List["ProjectRequirement"]]): List of requirements for this project.
    """

    __tablename__ = "projects"

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String(100))

    client: Mapped["Client"] = relationship(back_populates="projects")
    requirements: Mapped[List["ProjectRequirement"]] = relationship(
        back_populates="project"
    )

    @validates("end_date")
    def validate_end_date(self, key, end_date):
        """
        Validate that the end_date is after the start_date.

        Args:
            key (str): The name of the attribute being validated.
            end_date (date): The end date to validate.

        Returns:
            date: The validated end date.

        Raises:
            ValueError: If the end_date is before or equal to the start_date.
        """
        if end_date and self.start_date and end_date <= self.start_date:
            raise ValueError("End date must be after the start date")
        return end_date

    def __repr__(self) -> str:
        """Return a string representation of the Project instance."""
        return f"<Project(id={self.id}, name='{self.name}', status='{self.status}')>"
