"""
Main script for the Resource Allocation System.

This script demonstrates the usage of all models in the system,
including creating sample data and performing basic operations.
"""

import logging
from datetime import date, timedelta

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.database import get_db, init_db, verify_tables
from src.models import (
    Assignment,
    Availability,
    Client,
    Individual,
    IndividualRole,
    IndividualSkill,
    Project,
    ProjectRequirement,
    Role,
    RoleLevel,
    RoleRequirement,
    RoleType,
    Skill,
    SkillRequirement,
    TimeRequirement,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def create_sample_data(db: Session):
    """Create sample data for all models in the system."""
    try:
        # Create a client
        client = Client(name="NHS", contact_information="contact@nhs.co.uk")
        db.add(client)
        db.flush()
        logger.info(f"Created client: {client.name}")

        # Create a project
        project = Project(
            client_id=client.id,
            name="Website Redesign",
            description="Redesign of NHS's main website",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=90),
            status="In Progress",
        )
        db.add(project)
        db.flush()
        logger.info(f"Created project: {project.name}")

        # Create an individual
        individual = Individual(
            name="John Doe",
            email="john@example.com",
            employment_type="Full-time",
            hire_date=date.today() - timedelta(days=365),
        )
        db.add(individual)
        db.flush()
        logger.info(f"Created individual: {individual.name}")

        # Create skills
        skill1 = Skill(name="Python", description="Python programming")
        skill2 = Skill(
            name="Project Management", description="Project management skills"
        )
        db.add_all([skill1, skill2])
        db.flush()
        logger.info("Created skills: Python, Project Management")

        # Create role types and levels
        role_type = RoleType(name="Developer")
        role_level = RoleLevel(name="Senior")
        db.add_all([role_type, role_level])
        db.flush()

        # Create a role
        role = Role(
            role_type_id=role_type.id,
            role_level_id=role_level.id,
            name="Senior Python Developer",
            description="Experienced Python developer for web applications",
        )
        db.add(role)
        db.flush()
        logger.info(f"Created role: {role.name}")

        # Create a project requirement
        project_req = ProjectRequirement(
            project_id=project.id,
            description="Develop new homepage",
            start_date=date.today() + timedelta(days=7),
            end_date=date.today() + timedelta(days=37),
        )
        db.add(project_req)
        db.flush()

        # Create time requirement
        time_req = TimeRequirement(
            requirement_id=project_req.id, hours_per_week=40, total_hours=160
        )
        db.add(time_req)

        # Create skill requirement
        skill_req = SkillRequirement(
            requirement_id=project_req.id, skill_id=skill1.id, minimum_proficiency=4
        )
        db.add(skill_req)

        # Create role requirement
        role_req = RoleRequirement(
            requirement_id=project_req.id, role_id=role.id, number_needed=1
        )
        db.add(role_req)

        # Create an assignment
        assignment = Assignment(
            individual_id=individual.id,
            requirement_id=project_req.id,
            start_date=project_req.start_date,
            end_date=project_req.end_date,
            status="Assigned",
        )
        db.add(assignment)

        # Associate skills with individual
        individual_skill = IndividualSkill(
            individual_id=individual.id, skill_id=skill1.id, proficiency_level=4
        )
        db.add(individual_skill)

        # Associate role with individual
        individual_role = IndividualRole(
            individual_id=individual.id, role_id=role.id, start_date=date.today()
        )
        db.add(individual_role)
        db.flush()

        # Create availability for individual
        availability = Availability(
            individual_id=individual.id,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=30),
            hours_per_week=40,
        )
        db.add(availability)
        logger.info(f"Created availability for {individual.name}")

        db.commit()
        logger.info("All sample data committed to database")

    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"An error occurred while creating sample data: {str(e)}")
        raise


def query_data(db: Session):
    """Perform sample queries to demonstrate relationships between models."""
    try:
        # Query projects for a client
        client = db.query(Client).first()
        logger.info(f"Projects for client {client.name}:")
        for project in client.projects:
            logger.info(f"  - {project.name} (Status: {project.status})")

        # Query skills for an individual
        individual = db.query(Individual).first()
        logger.info(f"Skills for individual {individual.name}:")
        for individual_skill in individual.skills:
            logger.info(
                f"  - {individual_skill.skill.name} (Proficiency: {individual_skill.proficiency_level})"
            )

        # Query assignments for a project
        project = db.query(Project).first()
        logger.info(f"Assignments for project {project.name}:")
        for requirement in project.requirements:
            for assignment in requirement.assignments:
                logger.info(
                    f"  - {assignment.individual.name} assigned to {requirement.description}"
                )

        # Query roles for an individual
        logger.info(f"Roles for individual {individual.name}:")
        for individual_role in individual.roles:
            logger.info(
                f"  - {individual_role.role.name} (Start Date: {individual_role.start_date})"
            )

        # Query availabilities for an individual
        logger.info(f"Availabilities for individual {individual.name}:")
        for availability in individual.availabilities:
            logger.info(
                f"  - From {availability.start_date} to {availability.end_date}: {availability.hours_per_week} hours/week"
            )

    except SQLAlchemyError as e:
        logger.error(f"An error occurred while querying data: {str(e)}")
        raise


def main():
    """Main function to run the Resource Allocation System demonstration."""
    logger.info("Starting Resource Allocation System demonstration...")

    try:
        init_db()
        logger.info("Database initialized.")

        verify_tables()
        logger.info("Database tables verified.")

        # Use a context manager to ensure the session is properly closed
        with get_db() as db:
            create_sample_data(db)
            query_data(db)

    except SQLAlchemyError as e:
        logger.error(f"A database error occurred: {str(e)}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
    else:
        logger.info("Resource Allocation System demonstration completed successfully.")


if __name__ == "__main__":
    main()
