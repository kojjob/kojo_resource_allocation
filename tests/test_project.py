from datetime import date, timedelta

import pytest

from src.models import Client, Project


def test_project_creation(db_session):
    client = Client(name="Test Client", contact_information="test@example.com")
    db_session.add(client)
    db_session.flush()

    project = Project(
        client_id=client.id,
        name="Test Project",
        start_date=date.today(),
        end_date=date.today() + timedelta(days=30),
        status="Planning",
    )
    db_session.add(project)
    db_session.commit()

    assert project.id is not None
    assert project.name == "Test Project"
    assert project.client_id == client.id


def test_project_client_relationship(db_session):
    client = Client(name="Test Client", contact_information="test@example.com")
    db_session.add(client)
    db_session.flush()

    project = Project(
        client_id=client.id,
        name="Test Project",
        start_date=date.today(),
        end_date=date.today() + timedelta(days=30),
        status="Planning",
    )
    db_session.add(project)
    db_session.commit()

    assert project in client.projects
    assert project.client == client


def test_project_date_validation(db_session):
    client = Client(name="Test Client", contact_information="test@example.com")
    db_session.add(client)
    db_session.flush()

    with pytest.raises(ValueError):
        Project(
            client_id=client.id,
            name="Invalid Project",
            start_date=date.today(),
            end_date=date.today() - timedelta(days=1),  # End date before start date
            status="Planning",
        )
