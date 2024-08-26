from datetime import date

import pytest
from sqlalchemy.exc import IntegrityError

from src.models import ProjectRequirement, RoleRequirement


@pytest.fixture
def project_requirement_data():
    """
    Fixture to provide sample project requirement data.
    Returns:
        dict: A dictionary containing the project requirement data.
    """
    return {
        "project_id": 1,
        "description": "Test Project Requirement",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 12, 31),
    }


def test_project_requirement_creation(db_session, project_requirement_data):
    """
    Test that a ProjectRequirement can be created successfully.
    """
    # Create the project requirement
    project_requirement = ProjectRequirement(**project_requirement_data)
    db_session.add(project_requirement)
    db_session.commit()

    # Query the database and verify the project requirement is present
    result = (
        db_session.query(ProjectRequirement)
        .filter_by(project_id=project_requirement_data["project_id"])
        .one()
    )
    assert result is not None
    assert result.project_id == project_requirement_data["project_id"]
    assert result.description == project_requirement_data["description"]

    # Check that the start_date and end_date are as expected
    assert str(result.start_date) in str(project_requirement_data["start_date"])
    assert str(result.end_date) in str(project_requirement_data["end_date"])


def test_project_requirement_creation_without_name(db_session):
    """
    Test that creating a ProjectRequirement without a project_id raises an IntegrityError.
    """
    # Attempt to create a project requirement without a project_id
    project_requirement = ProjectRequirement(description="Missing project_id field")
    db_session.add(project_requirement)

    with pytest.raises(IntegrityError):
        db_session.commit()


def test_project_requirement_update(db_session, project_requirement_data):
    """
    Test that a ProjectRequirement can be updated successfully.
    """
    # Create a project requirement
    project_requirement = ProjectRequirement(**project_requirement_data)
    db_session.add(project_requirement)
    db_session.commit()

    # Update the project requirement
    project_requirement.description = "Updated project requirement description."
    db_session.commit()

    # Query the updated project requirement
    result = (
        db_session.query(ProjectRequirement).filter_by(id=project_requirement.id).one()
    )
    assert result.description == "Updated project requirement description."

    # Check that the start_date and end_date are still the same
    assert str(result.start_date) in str(project_requirement_data["start_date"])
    assert str(result.end_date) in str(project_requirement_data["end_date"])


def test_project_requirement_deletion(db_session, project_requirement_data):
    """
    Test that a ProjectRequirement can be deleted successfully.
    """
    # Create a project requirement
    project_requirement = ProjectRequirement(**project_requirement_data)
    db_session.add(project_requirement)
    db_session.commit()

    # Delete the project requirement
    db_session.delete(project_requirement)
    db_session.commit()

    # Verify the project requirement has been deleted
    result = (
        db_session.query(ProjectRequirement)
        .filter_by(id=project_requirement.id)
        .first()
    )
    assert result is None


def test_project_requirement_relationship_with_role_requirement(
    db_session, project_requirement_data
):
    # Create a project requirement
    project_requirement = ProjectRequirement(**project_requirement_data)
    db_session.add(project_requirement)
    db_session.commit()

    # Create a related role requirement with a value for number_needed
    role_requirement = RoleRequirement(
        requirement_id=project_requirement.id, role_id=1, number_needed=1
    )
    db_session.add(role_requirement)
    db_session.commit()

    # Verify that the role requirement is associated with the project requirement
    result = (
        db_session.query(ProjectRequirement).filter_by(id=project_requirement.id).one()
    )
    assert len(result.role_requirements) == 1
    assert result.role_requirements[0].requirement_id == project_requirement.id
    assert str(result.role_requirements[0].requirement_id) in str(
        project_requirement.id
    )
    assert result.role_requirements[0].number_needed == 1
