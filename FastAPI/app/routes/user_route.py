""" This module contains the routes for the user service. """
from services.user_service import UserService
from models.user import User
from fastapi import APIRouter, Body

user_route = APIRouter()
user_service = UserService()

@user_route.get("/users/")
def get_users():
    """
    Get all users
    
    Returns:
        List: A list of all users
    """
    return user_service.get_users()

@user_route.get("/users/{user_id}")
def get_user(user_id: int):
    """
    Get a single user
    
    Args:
        user_id (int): The id of the user to retrieve
        
    Returns:
        Dict: The user data
    """
    return user_service.get_user(user_id)

@user_route.post("/users")
def create_user(user: User):
    """
    Create a new user
    
    Args:
        user (User): The user data to create
        
    Returns:
        Dict: The user data
    """
    return user_service.create_user(user)

@user_route.put("/users/{user_id}")
def update_user(user_id: int, user_data: User = Body(...)):
    """
    Update a user
    
    Args:
        user_id (int): The id of the user to update
        user_data (dict): The data to update
        
    Returns:
        Dict: The user data
    """
    return user_service.update_user(user_id, user_data)

@user_route.delete("/users/{user_id}")
def delete_user(user_id: int):
    """
    Delete a user
    
    Args:
        user_id (int): The id of the user to delete
        
    Returns:
        Dict: The user data
    """
    return user_service.delete_user(user_id)
