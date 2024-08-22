from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

# Local application import

# Conditional import to avoid circular dependencies
if TYPE_CHECKING:
    from src.models.client import Client


class Project(BaseModel):
    """
    Represents a project in the Resource Allocation System.

    Attributes:
      name (Mapped[str]): The name of the project. Required, index for faster queries.
      description (Mapped[Optional[str]]): A description of the project. Optional.
      start_date (Mapped[date]): The start date of the project. Required.
      end_date (Mapped[date]): The end date of the project. Optional.
      status (Mapped[str]): The current status of the project. Required.
      client_id (Mapped[int]): The ID of the client associated to this project. Required, foreign key to client table.
      client (Mapped["Client]):  The client associated with this project. This is many-to-one relationship.
    """

    __tablename__ = "projects"  # Specifies the table name for this model

    # Define columns
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(500))
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[Optional[date]] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)

    # Define relationship
    # This creates a many-to-one relationship with the Client model
    # The 'back_populates, parameter creates a bidirectional relationship
    client: Mapped["Client"] = relationship(back_populates="projects")

    def __repr__(self) -> str:
        """
        Returns a string representation of the Project instance.

        Returns:
           str: A string representation of the Project, including its id, name, and status.
        """

        return f"<Projeect(id={self.id}, name='{self.name}', status='{self.status}')>"
