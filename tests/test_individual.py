from datetime import date, timedelta

import pytest
from sqlalchemy.exc import IntegrityError

from src.models import Individual, IndividualSkill, Skill


def test_individual_creation(db_session):
    individual = Individual(
        name="John Doe",
        email="john@example.com",
        employment_type="Full-time",
        hire_date=date.today(),
    )
    db_session.add(individual)
    db_session.commit()

    assert individual.id is not None
    assert individual.name == "John Doe"
    assert individual.email == "john@example.com"
    assert individual.employment_type == "Full-time"
    assert individual.hire_date == date.today()


def test_individual_unique_email(db_session):
    individual1 = Individual(
        name="John Doe",
        email="john@example.com",
        employment_type="Full-time",
        hire_date=date.today(),
    )
    db_session.add(individual1)
    db_session.commit()

    individual2 = Individual(
        name="Jane Doe",
        email="john@example.com",  # Same email as individual1
        employment_type="Part-time",
        hire_date=date.today(),
    )
    db_session.add(individual2)

    with pytest.raises(IntegrityError):
        db_session.commit()


def test_individual_skill_relationship(db_session):
    individual = Individual(
        name="John Doe",
        email="john@example.com",
        employment_type="Full-time",
        hire_date=date.today(),
    )
    skill = Skill(name="Python", description="Python programming language")
    individual_skill = IndividualSkill(
        individual=individual, skill=skill, proficiency_level=4
    )

    db_session.add_all([individual, skill, individual_skill])
    db_session.commit()

    assert len(individual.skills) == 1
    assert individual.skills[0].skill == skill
    assert individual.skills[0].proficiency_level == 4


def test_individual_hire_date_validation(db_session):
    future_date = date.today() + timedelta(days=1)
    with pytest.raises(ValueError):
        Individual(
            name="John Doe",
            email="john@example.com",
            employment_type="Full-time",
            hire_date=future_date,  # Future date should not be allowed
        )


def test_individual_employment_type_validation(db_session):
    with pytest.raises(ValueError):
        Individual(
            name="John Doe",
            email="john@example.com",
            employment_type="Invalid",  # Invalid employment type
            hire_date=date.today(),
        )
