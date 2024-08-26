"""
Database configuration and session management for the Resource Allocation System.

This module provides functions and utilities for database operations,
including initialization, session management, and engine access.
"""

import logging
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

import config

# Make sure this imports your Base from the models
from src.models import BaseModel

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create the SQLAlchemy engine
engine = create_engine(config.DATABASE_URL, echo=config.DEBUG)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """
    Context manager to handle the database session.

    This function creates a new database session and ensures it's closed after use,
    even if an exception occurs.

    Yields:
        Session: The database session.

    Raises:
        SQLAlchemyError: If there's an error during database operations.
    """
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        logger.error(f"Database error occurred: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()


def init_db() -> None:
    """
    Initialize the database by creating all tables.

    This function should be called once when setting up the application.
    It creates all tables defined in the models.

    Raises:
        SQLAlchemyError: If there's an error creating the tables.
    """
    try:
        # Import all models here to ensure they're registered with Base

        BaseModel.metadata.create_all(bind=engine)
        logger.info("Database initialized successfully.")
    except SQLAlchemyError as e:
        logger.error(f"Error initializing database: {str(e)}")
        raise


def get_engine() -> Engine:
    """
    Get the SQLAlchemy engine.

    Returns:
        Engine: The SQLAlchemy engine instance.
    """
    return engine


def verify_tables() -> None:
    """
    Verify that all expected tables have been created in the database.
    """
    from sqlalchemy import inspect

    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    expected_tables = [table.__tablename__ for table in BaseModel.__subclasses__()]

    for table in expected_tables:
        if table in existing_tables:
            logger.info(f"Table '{table}' exists in the database.")
        else:
            logger.warning(f"Table '{table}' does not exist in the database!")

    unexpected_tables = set(existing_tables) - set(expected_tables)
    if unexpected_tables:
        logger.warning(f"Unexpected tables found in the database: {unexpected_tables}")


# You can add more utility functions here as needed
