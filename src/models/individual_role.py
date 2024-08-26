from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel

if TYPE_CHECKING:
    from src.models.individual import Individual
    from src.models.role import Role


class IndividualRole(BaseModel):
    __tablename__ = "individual_roles"

    # Override the id column to make it nullable and autoincrement
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=True)

    individual_id: Mapped[int] = mapped_column(
        ForeignKey("individuals.id"), nullable=False
    )
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)

    individual: Mapped["Individual"] = relationship(back_populates="roles")
    role: Mapped["Role"] = relationship(back_populates="individuals")

    def __repr__(self) -> str:
        return f"<IndividualRole(id={self.id}, individual_id={self.individual_id}, role_id={self.role_id}, start_date={self.start_date})>"
