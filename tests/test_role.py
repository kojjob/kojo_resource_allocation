from src.models import Role, RoleLevel, RoleType


def test_role_creation(db_session):
    # Create RoleLevel and RoleType for foreign key references
    role_level = RoleLevel(name="Senior")
    role_type = RoleType(name="Developer")

    db_session.add_all([role_level, role_type])
    db_session.commit()

    # Create a Role with valid references
    role = Role(
        name="Senior Developer",
        description="Experienced developer",
        role_level_id=role_level.id,
        role_type_id=role_type.id,
    )

    db_session.add(role)
    db_session.commit()

    # Test if Role is created correctly
    fetched_role = db_session.query(Role).filter_by(name="Senior Developer").one()
    assert fetched_role is not None
    assert fetched_role.role_level_id == role_level.id
    assert fetched_role.role_type_id == role_type.id

    # Test relationships
    assert fetched_role.role_level == role_level
    assert fetched_role.role_type == role_type


def test_individual_role_relationship(db_session):
    # Create necessary related objects
    role_level = RoleLevel(name="Test Level")
    role_type = RoleType(name="Test Type")
    db_session.add(role_level)
    db_session.add(role_type)
    db_session.commit()

    # Now create the Role with valid foreign keys
    role = Role(
        name="Test Role",
        description="Test Description",
        role_level_id=role_level.id,
        role_type_id=role_type.id,
    )
    db_session.add(role)
    db_session.commit()

    # Rest of your test code...
