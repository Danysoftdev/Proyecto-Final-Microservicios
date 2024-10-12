""" This module contains the CRUD operations for the user model """

from datetime import datetime
from peewee import DoesNotExist
from config.database import UserModel
from models.user import User
from fastapi import Body, HTTPException


class UserService:
    """
    A service class for the user model
    """

    def get_users(self):
        """
        Get all users

        Returns:
            List: A list of all users
        """
        users = UserModel.select().where(UserModel.id > 0).dicts()
        return list(users)

    def get_user(self, user_id: int):
        """
        Get a single user

        Args:

            user_id (int): The id of the user to retrieve

        Returns:
            Dict: The user data
        """
        try:
            user = UserModel.get(UserModel.id == user_id)
            return user.__data__
        except DoesNotExist:
            return {"error": "User not found"}

    def create_user(self, user: User = Body(...)):
        """
        Create a new user

        Args:
            user (User): The user data to create

        Returns:
            Dict: The user data
        """
        existing_user = UserModel.get_or_none(UserModel.user_email == user.user_email)
        if existing_user:
            raise HTTPException(
                status_code=400, detail="The email address is alredy in use."
            )
        new_user = UserModel.create(
            username=user.username,
            user_email=user.user_email,
            user_password=user.user_password,
            user_pfp=user.user_pfp,
            user_created=datetime.now(),
            user_updated=datetime.now(),
        )
        return new_user.__data__

    def update_user(self, user_id: int, user: User):
        """
        Update a user

        Args:
            user_id (int): The id of the user to update
            user (User): The user data to update

        Returns:
            Dict: The updated user data
        """
        existing_user = UserModel.get_by_id(user_id)

        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found.")

        existing_user.username = user.username
        existing_user.user_email = user.user_email
        existing_user.user_password = user.user_password
        existing_user.user_pfp = user.user_pfp
        existing_user.user_created = user.user_created
        existing_user.user_updated = datetime.now()

        existing_user.save()
        return {
            "message": "User successfully updated",
            "user_data": existing_user
        }

    def delete_user(self, user_id: int):
        """
        Delete a user

        Args:
            user_id (int): The id of the user to delete

        Returns:
            Dict: A message indicating the operation result
        """
        try:
            user = UserModel.get(UserModel.id == user_id)
            user.delete_instance()
            return {"message": "User deleted successfully"}
        except DoesNotExist:
            return {"error": "User not found"}
