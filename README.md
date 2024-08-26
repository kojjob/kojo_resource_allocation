# Resource Allocation System

## Overview

The Resource Allocation System is a comprehensive data management solution designed to efficiently track and allocate resources, manage projects, and handle assignments. Built with SQLite and SQLAlchemy, it offers a lightweight yet powerful platform for resource management.

## Key Features

- **SQLite Database**: Serverless, file-based data storage for easy deployment and maintenance.
- **SQLAlchemy ORM**: Intuitive database interactions with full Python integration.
- **Modular Architecture**: Easily expandable and maintainable codebase.
- **Comprehensive CRUD Operations**: Full support for Create, Read, Update, and Delete operations on all major entities.
- **Extensive Test Suite**: Thorough testing using pytest to ensure reliability.
- **Flexible Configuration**: Environment variable support for versatile setup options.

## Project Structure

```
workproj/
│
├── .pytest_cache/
├── env/
│   ├── bin/
│   ├── include/
│   └── lib/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── assignment.py
│   │   ├── availability.py
│   │   ├── base.py
│   │   ├── client.py
│   │   ├── individual_role.py
│   │   ├── individual_skill.py
│   │   ├── individual.py
│   │   ├── project_requirement.py
│   │   ├── project.py
│   │   ├── role_level.py
│   │   ├── role_requirement.py
│   │   ├── role_type.py
│   │   ├── role.py
│   │   ├── skill_requirement.py
│   │   ├── skill.py
│   │   └── time_requirement.py
│   ├── __init__.py
│   └── database.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_client.py
│   ├── test_individual.py
│   ├── test_project_requirement.py
│   ├── test_project.py
│   └── test_role.py
├── venv/
├── README.md
├── config.py
├── main.py
├── requirements.txt
└── resource_allocation.db
```

## Prerequisites

- Python 3.9+
- pip (Python package installer)

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com:kojjob/kojo_resource_allocation.git
   cd workproj
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables (optional):**

   Create a `.env` file in the root directory with the following content:

   ```
   DATABASE_URL=sqlite:///resource_allocation.db
   DEBUG=True
   ```

6. **Initialize the database:**

   ```bash
   python main.py
   ```

## Usage

To run the main application:

```bash
python main.py
```

This command creates the database (if it doesn't exist) and performs example operations.

## Running Tests

Execute the test suite:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

## Development Guide

### Adding a New Model

1. Create a new file in `src/models/`, e.g., `new_model.py`
2. Define your model class, inheriting from `BaseModel`
3. Import your new model in `src/models/__init__.py`
4. Create a corresponding test file in `tests/`, e.g., `test_new_model.py`

### Modifying the Database Schema

If you make changes to the models:

1. Delete the existing `resource_allocation.db` file
2. Run `python main.py` to create a new database with the updated schema

## Contributing

We welcome contributions to the Resource Allocation System! Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure that you update tests as appropriate and adhere to the existing coding style.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have any questions, please open an issue on the GitHub repository.

## Acknowledgements

- SQLAlchemy team for their excellent ORM library
- Python community for continuous support and inspiration

---

Happy coding! 🚀