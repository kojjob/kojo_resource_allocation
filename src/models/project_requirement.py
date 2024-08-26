"""
ProjectRequirement model for the Resource Allocation System.
This module defines the ProjectRequirement class, representing requirements for projects.
"""

from datetime import date
from typing import TYPE_CHECKING, List

from sqlalchemy import Date, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.assignment import Assignment
    from src.models.project import Project
    from src.models.role_requirement import RoleRequirement
    from src.models.skill_requirement import SkillRequirement
    from src.models.time_requirement import TimeRequirement


class ProjectRequirement(BaseModel):
    """
    Represents a requirement for a project in the Resource Allocation System.
    Attributes:
    id (Mapped[int]): The unique identifier for the requirement.
    project_id (Mapped[int]): The ID of the associated project.
    description (Mapped[str]): The description of the requirement.
    start_date (Mapped[date]): The start date of the requirement.
    end_date (Mapped[date]): The end date of the requirement.
    project (Mapped["Project"]): The associated project.
    assignments (Mapped[List["Assignment"]]): List of assignments for this requirement.
    skill_requirements (Mapped[List["SkillRequirement"]]): List of skill requirements for this requirement.
    role_requirements (Mapped[List["RoleRequirement"]]): List of role requirements for this requirement.
    time_requirement (Mapped["TimeRequirement"]): The time requirement for this project requirement.
    """

    __tablename__ = "project_requirements"

    # The ID of the associated project
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"), nullable=False, index=True
    )

    # The description of the requirement
    description: Mapped[str] = mapped_column(Text)

    # The start date of the requirement
    start_date: Mapped[date] = mapped_column(Date, index=True)

    # The end date of the requirement
    end_date: Mapped[date] = mapped_column(Date, index=True)

    # The associated project
    project: Mapped["Project"] = relationship(back_populates="requirements")

    # List of assignments for this requirement
    assignments: Mapped[List["Assignment"]] = relationship(back_populates="requirement")

    # List of skill requirements for this requirement
    skill_requirements: Mapped[List["SkillRequirement"]] = relationship(
        back_populates="requirement"
    )

    # List of role requirements for this requirement
    role_requirements: Mapped[List["RoleRequirement"]] = relationship(
        back_populates="requirement"
    )

    # The time requirement for this project requirement
    time_requirement: Mapped["TimeRequirement"] = relationship(
        back_populates="project_requirement", uselist=False
    )

    def __repr__(self) -> str:
        return f"<ProjectRequirement(id={self.id}, project_id={self.project_id}, start_date='{self.start_date}')>"
