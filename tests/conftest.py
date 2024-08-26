import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.base import BaseModel


@pytest.fixture(scope="function")
def engine():
    """Create a new engine for each test function."""
    return create_engine("sqlite:///:memory:")


@pytest.fixture(scope="function")
def tables(engine):
    """Create all tables before a test runs, and drop them after."""
    BaseModel.metadata.create_all(engine)
    yield
    BaseModel.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session():
    """Fixture to create a new database session for each test function."""
    # Create an in-memory SQLite database and initialize it
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        # Ensure rollback of any uncommitted changes
        session.rollback()

        # Close the session
        session.close()
        BaseModel.metadata.drop_all(engine)  # Clean up the database schema
