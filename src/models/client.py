# Future imports for Python 2/3 compatibility
from __future__ import annotations

# Standard library import
from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local application import
from src.models.base import BaseModel

# Conditional import to avoid circular dependencies
if TYPE_CHECKING:
    from src.models.project import Project


class Client(BaseModel):
    """
    Represents a client in the Resource Allocation System.

    This class inherit from BaseModel, which provides common fields like id, created_at, and updated_at.

    Attributes:
      Name (Mapped[str]): The name of the client.
      contact_information (Mapped[str]): The contact information of the client.
    """

    __tablename__ = "clients"

    name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    contact_information: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relationship with Project model
    projects: Mapped[List["Project"]] = relationship(back_populates="client")

    def __repr__(self) -> str:
        """
        Return a string representation of the Client instance.

        This method is useful for debugging and logging

        Returns:
          str: A string representation of the client, including its id, name, and contact_information
        """
        return f"<Client(id={self.id}, name'{self.name}', email='{self.contact_informatiom}')>"
