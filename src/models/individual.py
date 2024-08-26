from datetime import date
from typing import TYPE_CHECKING, List

from sqlalchemy import Date, String
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.assignment import Assignment
    from src.models.availability import Availability
    from src.models.individual_role import IndividualRole
    from src.models.individual_skill import IndividualSkill


class Individual(BaseModel):
    """
    Represents an individual in the Resource Allocation System.

    Attributes:
        individual_id (Mapped[int]): The unique identifier for the individual.
        individual_name (Mapped[str]): The name of the individual.
        email (Mapped[str]): The email address of the individual (unique).
        employment_type (Mapped[str]): Type of employment Full-time or Contract.
        hire_date (Mapped[date]): The date when the individual was hired.
        skills (Mapped[List["IndividualSkill"]]): List of skills associated with this individual.
        assignments (Mapped[List["Assignment"]]): List of assignments for this individual.
        availabilities (Mapped[List["Availability"]]): List of availabilities for this individual.
        roles (Mapped[List["IndividualRole"]]): List of roles associated with this individual.
    """

    __tablename__ = "individuals"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True, index=True
    )
    employment_type: Mapped[str] = mapped_column(
        String(100), nullable=False, index=True
    )
    hire_date: Mapped[date] = mapped_column(Date)

    # role_id: Mapped[int] = mapped_column(ForeignKey("role.id"), nullable=False)
    skills: Mapped[List["IndividualSkill"]] = relationship(back_populates="individual")
    assignments: Mapped[List["Assignment"]] = relationship(back_populates="individual")
    availabilities: Mapped[List["Availability"]] = relationship(
        back_populates="individual"
    )
    roles: Mapped[List["IndividualRole"]] = relationship(back_populates="individual")

    @validates("hire_date")
    def validate_hire_date(self, key, hire_date):
        if hire_date > date.today():
            raise ValueError("Hire date cannot be in the future")
        return hire_date

    @validates("employment_type")
    def validate_employment_type(self, key, employment_type):
        valid_types = ["Full-time", "Part-time", "Contract"]
        if employment_type not in valid_types:
            raise ValueError(
                f"Invalid employment type. Must be one of: {', '.join(valid_types)}"
            )
        return employment_type

    def __repr__(self) -> str:
        return f"<Individual(individual_id={self.individual_id}, name='{self.individual_name}', email='{self.email}')>"
