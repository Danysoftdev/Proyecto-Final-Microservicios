"""
Database module for the FastAPI application.

This module defines the UserModel class representing a user entity.

Classes:

    UserModel (Model): A class representing a user entity.
"""
# pylint: disable=too-few-public-methods
from datetime import datetime
from config.settings import DATABASE
from peewee import Model, MySQLDatabase, AutoField, CharField, DateTimeField

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)

class UserModel(Model):
    """
    UserModel class representing a user entity.
    
    Attributes:
        id (int): Unique identifier for the user.
        username (str): The user's username.
        user_email (str): The user's email.
        user_password (str): The user's password.
        user_pfp (str): The user's profile picture.
        user_created (datetime): The date and time the user was created.
        user_updated (datetime): The date and time the user was last updated
    """
    id = AutoField(primary_key=True)
    username = CharField(max_length=100)
    user_email = CharField(max_length=100, unique=True)
    user_password = CharField(max_length=255)
    user_pfp = CharField(max_length=255, null=True)
    user_created = DateTimeField(default=datetime.now)
    user_updated = DateTimeField(default=datetime.now)

    class Meta:
        """
        Meta class for the UserModel.
        
        Attributes:
        
            database (MySQLDatabase): The database to connect to.
            table_name (str): The name of the table in the database.
        """
        database = database
        table_name = "users"
