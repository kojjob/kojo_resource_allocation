import os

"""
Configuration settings for the Resource Allocation System.
"""
# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///resource_allocation.db")

# Debug mode
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
