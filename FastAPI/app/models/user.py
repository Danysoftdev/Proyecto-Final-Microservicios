"""
user.py

This module defines the User model using Pydantic's BaseModel.

Classes:
    User (BaseModel): Represents a user entity.

Attributes:
    Datetime: The datetime module supplies classes for manipulating dates and times.
    BaseModel (class): Pydantic's base class for creating data models.
"""

from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    """
    User model representing a user entity.

    Attributes:
        id (int): Unique identifier for the user.
        username (str): The user's username.
        user_email (str): The user's email.
        user_password (str): The user's password.
        user_pfp (str): The user's profile picture.
        user_created (datetime): The date and time the user was created.
        user_updated (datetime): The date and time the user was last updated.
    """

    id: int
    username: str
    user_email: str
    user_password: str
    user_pfp: str
    user_created: datetime
    user_updated: datetime
