# Resource Allocation System

## Overview

This Resource Allocation System is a data persistence solution built with SQLite and SQLAlchemy. It's designed to manage and track resources, projects, and assignments efficiently.

## Features

- SQLite database for lightweight, serverless data storage
- SQLAlchemy ORM for intuitive database interactions
- Modular structure for easy expansion and maintenance
- CRUD operations for all major entities (Clients, Projects, Individuals, etc.)
- Comprehensive test suite using pytest
- Environment variable support for flexible configuration

## Project Structure

```Bash
resource_allocation/
│
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── client.py
│   │   ├── project.py
│   │   ├── individual.py
│   │   ├── skill.py
│   │   ├── role.py
│   │   ├── availability.py
│   │   ├── assignment.py
│   │   └── time_requirement.py
│   │
│   ├── database.py
│   ├── config.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_models.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.10+
- pip (Python package installer)

## Setup and Installation

1. Clone the repository:

   ```Base
   git clone https://github.com/your-username/resource_allocation.git
   cd resource_allocation
   ```

2. Create a virtual environment:

   ```Bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   On macOS and Linux:

   ```Bash
   source venv/bin/activate
   ```

   On Windows:

   ```Base
   .\venv\Scripts\activate
   ```

4. Install dependencies:

   ```Base
   pip install -r requirements.txt
   ```

5. Set up environment variables (optional):
   Create a `.env` file in the root directory and add:

   ```Base
   DATABASE_URL=sqlite:///your_database_name.db
   DEBUG=True
   ```

6. Initialize the database:

   ```Base
   python src/main.py
   ```

## Usage

To run the main application:

```Base
python src/main.py
```

This will create the database (if it doesn't exist) and perform some example operations.

## Running Tests

To run the test suite:

```Base
pytest
```

For more verbose output:

```Base
pytest -v
```

## Development

### Adding a New Model

1. Create a new file in `src/models/`, e.g., `new_model.py`
2. Define your model class, inheriting from `BaseModel`
3. Import your new model in `src/models/__init__.py`
4. Create corresponding test methods in `tests/test_models.py`

### Modifying the Database Schema

If you make changes to the models:

1. Delete the existing database file
2. Run `python src/main.py` to create a new database with the updated schema

## Contributing

We welcome contributions to the Resource Allocation System! Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the existing coding style.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
