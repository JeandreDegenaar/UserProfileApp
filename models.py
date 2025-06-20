"""
/**
 * File: models.py
 *
 * Purpose:
 * Defines the User model for the Flask application using SQLAlchemy ORM.
 * This model maps to a database table to store registered user profiles.
 *
 * Fields:
 * - id: Primary key (auto-incrementing integer)
 * - name: User's name (string, required)
 * - email: User's email address (string, required, unique)
 * - age: User's age (integer, optional)
 *
 * This model is imported and used by the main application to create,
 * update, delete, and query user data.
 */
"""

from app import db

# Define a User model for storing profile info
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)           # Unique identifier
    name = db.Column(db.String(50), nullable=False)        # User's name
    email = db.Column(db.String(100), nullable=False, unique=True)  # Unique email
    age = db.Column(db.Integer)                            # User's age
