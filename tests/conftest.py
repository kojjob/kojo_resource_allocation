import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models import Base  # Base should be the declarative base used for your models


# Define the in-memory SQLite database for testing
@pytest.fixture(scope="session")
def engine():
    return create_engine("sqlite:///:memory:")


@pytest.fixture(scope="session")
def tables(engine):
    # Create all tables based on the models defined
    Base.metadata.create_all(engine)
    yield
    # Drop all tables after tests complete
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(engine, tables):
    """Create a new database session for a test."""
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()
