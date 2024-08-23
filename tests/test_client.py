from src.models.client import Client


# Test to verify the creation of a client and its persistence in the database
def test_create_client(db_session):
    # Create a new client object
    client = Client(name="Test Client", contact_information="test@example.com")

    # Add the client to the database session and commit it
    db_session.add(client)
    db_session.commit()

    # Assert that the client has an id (meaning it was successfully created)
    assert client.id is not None

    # Assert that the client's attributes were correctly set
    assert client.name == "Test Client"
    assert client.contact_information == "test@example.com"


# Test to verify that a client can be retrieved from the database
def test_retrieve_client(db_session):
    # Create and persist a new client
    client = Client(name="Test Client", contact_information="test@example.com")
    db_session.add(client)
    db_session.commit()

    # Query the database to retrieve the client by name
    retrieved_client = db_session.query(Client).filter_by(name="Test Client").first()

    # Assert that the client was successfully retrieved
    assert retrieved_client is not None

    # Assert that the retrieved client's attributes match the expected values
    assert retrieved_client.contact_information == "test@example.com"
