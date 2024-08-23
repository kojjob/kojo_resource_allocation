from datetime import date, timedelta

from src.models import Client, Project


def test_project_creation(db_session):
    # Arrange: Create a unique client first
    client = Client(name="Project Client 1", contact_information="client1@example.com")
    db_session.add(client)
    db_session.commit()

    # Act: Create a new project associated with the client
    project = Project(
        client_id=client.id,
        name="New Project 1",
        description="Test description",
        start_date=date.today(),
        end_date=date.today() + timedelta(days=30),
        status="Planning",
    )
    db_session.add(project)
    db_session.commit()

    # Assert: Check that the project is successfully created
    assert project.id is not None, "Project ID should not be None after commit."
    assert project.name == "New Project 1", "Project name does not match."
    assert project.client_id == client.id, "Client ID on the project does not match."


def test_project_client_relationship(db_session):
    # Arrange: Create a unique client and associated project
    client = Client(name="Project Client 2", contact_information="client2@example.com")
    db_session.add(client)
    db_session.commit()

    project = Project(
        client_id=client.id,
        name="New Project 2",
        description="Test project",
        start_date=date.today(),
        end_date=date.today() + timedelta(days=30),
        status="In Progress",
    )
    db_session.add(project)
    db_session.commit()

    # Assert: Check that the relationship between project and client is maintained
    assert project.client == client, "Project's client relationship is incorrect."
    assert project in client.projects, "Project should be in the client's project list."
