import os

from dotenv import load_dotenv

"""
Configuration settings for the Resource Allocation System.
"""

# Load environment variables from .env file
load_dotenv()


# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///resource_allocation.db")

# Debug mode
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
