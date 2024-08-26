from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.individual import Individual


class Availability(BaseModel):
    """
    Represents an individual's availability in the Resource Allocation System.

    Attributes:
        individual_id (Mapped[int]): The ID of the associated individual.
        start_date (Mapped[date]): The start date of the availability period.
        end_date (Mapped[date]): The end date of the availability period.
        hours_per_week (Mapped[int]): The number of available hours per week.
        individual (Mapped["Individual"]): The associated individual.
    """

    __tablename__ = "availabilities"

    individual_id: Mapped[int] = mapped_column(
        ForeignKey("individuals.id"), nullable=False, index=True
    )
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    hours_per_week: Mapped[int] = mapped_column(Integer, nullable=False)

    individual: Mapped["Individual"] = relationship(back_populates="availabilities")

    def __repr__(self) -> str:
        return f"<Availability(id={self.id}, individual_id={self.individual_id}, start_date='{self.start_date}', end_date='{self.end_date}')>"
