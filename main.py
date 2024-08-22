"""
Main script for the Resource Allocation System.

This script initializes the database, creates sample data,
and demonstrates basic CRUD operations with the Client and Project models.
"""

import logging
from datetime import date

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.database import engine, get_db
from src.models import Base, Client, Project

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def create_tables():
    """Create all tables in the database."""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully.")
    except SQLAlchemyError as e:
        logger.error(f"An error occurred while creating database tables: {e}")
        raise


def create_sample_data(db: Session):
    """Create sample data for demonstration purposes."""
    try:
        # Create a sample client
        client = Client(
            name="NHS",
            contact_information="Gill Willson",
        )
        db.add(client)
        db.flush()  # This assigns an id to the client without committing the transaction

        # Create a sample project for the client
        project = Project(
            name="Web Development",
            description="Redesign of NHS main website",
            start_date=date.today(),
            status="In Progress",
            client_id=client.id,
        )
        db.add(project)

        db.commit()
        logger.info(
            f"Sample data created: Client '{client.name}' and Project '{project.name}'"
        )
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"An error occurred while creating sample data: {e}")
        raise


def display_data(db: Session):
    """Display all clients and their projects."""
    try:
        clients = db.query(Client).all()
        for client in clients:
            logger.info(f"Client: {client.name}")
            for project in client.projects:
                logger.info(f"  - Project: {project.name} (Status: {project.status})")
    except SQLAlchemyError as e:
        logger.error(f"An error occurred while displaying data: {e}")
        raise


def main():
    """Main function to run the Resource Allocation System."""
    logger.info("Starting Resource Allocation System...")

    create_tables()

    # Use a context manager to ensure the session is properly closed
    with next(get_db()) as db:
        create_sample_data(db)
        display_data(db)

    logger.info("Resource Allocation System demo completed.")


if __name__ == "__main__":
    main()
