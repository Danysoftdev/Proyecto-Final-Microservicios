"""
This module defines the database models and their relationships
for a food recipe application using SQLAlchemy.

Imports:
    Column, Integer, String, DECIMAL, DateTime, Boolean, Text, Enum, ForeignKey,
    create_engine (from sqlalchemy): SQLAlchemy components for defining
    database columns and relationships.
    DATABASE (from app.config.settings): Contains the database configuration settings.
    declarative_base (from sqlalchemy.ext.declarative): A factory function for creating
    a base class for declarative class definitions.
    datetime (from datetime): Supplies classes for manipulating dates and times.

Classes:
    User (Base): Represents a user in the database.
    Group (Base): Represents a group in the database.
    UserGroup (Base): Represents the relationship between users and groups.
    Recipe (Base): Represents a recipe in the database.
    FoodType (Base): Represents a food type in the database.
    RecipeFoodType (Base): Represents the relationship between recipes and food types.
    Category (Base): Represents a category in the database.
    Ingredient (Base): Represents an ingredient in the database.
    MeasurementUnit (Base): Represents a measurement unit in the database.
    RecipeIngredient (Base): Represents the relationship between recipes and ingredients.
    Menu (Base): Represents a menu in the database.
    MenuRecipe (Base): Represents the relationship between menus and recipes.
    MenuGroup (Base): Represents the relationship between menus and groups.
    ShopListItem (Base): Represents a shopping list item in the database.
    PantryIngredient (Base): Represents the relationship between pantries and ingredients.
    Notification (Base): Represents a notification in the database.

Functions:
    create_tables(): Creates all the defined tables in the database using the provided engine.
"""

from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    DECIMAL,
    DateTime,
    Boolean,
    Text,
    Enum,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.settings import DATABASE

Base = declarative_base()


class User(Base):
    """
    Represents a user in the system.

    Attributes:
        id (int): Primary key for the user.
        username (str): Unique username for the user.
        user_email (str): Unique email address of the user.
        user_password (str): Hashed password of the user.
        user_pfp (str): URL or path to the user's profile picture (optional).
        user_created (datetime): Timestamp when the user was created.
        user_updated (datetime): Timestamp when the user was last updated.
    """

    _tablename_ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    user_email = Column(String(100), unique=True, nullable=False)
    user_password = Column(String(255), nullable=False)
    user_pfp = Column(String(255), nullable=True)
    user_created = Column(DateTime, default=datetime.now)
    user_updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Group(Base):
    """
    Represents a user group.

    Attributes:
        group_id (int): Primary key for the group.
        groups_name (str): Name of the group.
        groups_description (str): Description of the group.
        group_created (datetime): Timestamp of group creation.
        group_updated (datetime): Timestamp of the last group update.
    """

    _tablename_ = "groups"
    group_id = Column(Integer, primary_key=True, index=True)
    groups_name = Column(String(100), nullable=False)
    groups_description = Column(String(255))
    group_created = Column(DateTime, default=datetime.utcnow)
    group_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class UserGroup(Base):
    """
    Represents the relationship between users and groups.

    Attributes:
        user_id (int): Foreign key referencing a user.
        group_id (int): Foreign key referencing a group.
        rol (str): Role of the user in the group ('admin' or 'member').
    """

    _tablename_ = "user_groups"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.group_id"), primary_key=True)
    rol = Column(Enum("admin", "member"), nullable=False)


class Recipe(Base):
    """
    Represents a recipe.

    Attributes:
        recipe_id (int): Primary key for the recipe.
        user_id (int): Foreign key referencing the user who created the recipe.
        recipe_name (str): Name of the recipe.
        recipe_description (str): Description of the recipe.
        recipe_prepare_time (int): Preparation time in minutes.
        recipe_difficulty (str): Difficulty level ('easy', 'medium', 'hard').
        recipe_portions (int): Number of portions the recipe yields.
        recipe_instructions (str): Instructions for preparing the recipe.
        recipe_is_public (bool): Indicates if the recipe is publicly visible.
        recipe_created (datetime): Timestamp when the recipe was created.
        recipe_updated (datetime): Timestamp of the last recipe update.
    """

    _tablename_ = "recipes"
    recipe_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    recipe_name = Column(String(100), nullable=False)
    recipe_description = Column(Text, nullable=False)
    recipe_prepare_time = Column(Integer, nullable=False)
    recipe_difficulty = Column(Enum("easy", "medium", "hard"), nullable=False)
    recipe_portions = Column(
        Integer, nullable=False
    )  # Cambié el tipo a Integer por lógica
    recipe_instructions = Column(Text)
    recipe_is_public = Column(Boolean, default=False, nullable=False)
    recipe_created = Column(DateTime, default=datetime.utcnow)
    recipe_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class FoodType(Base):
    """
    Represents a type of food.

    Attributes:
        food_type_id (int): Primary key for the food type.
        food_type_name (str): Name of the food type.
        food_type_created (datetime): Timestamp when the food type was created.
    """

    _tablename_ = "food_types"
    food_type_id = Column(Integer, primary_key=True, index=True)
    food_type_name = Column(String(50), nullable=False)
    food_type_created = Column(DateTime, default=datetime.utcnow)


class RecipeFoodType(Base):
    """
    Represents the relationship between recipes and food types.

    Attributes:
        recipe_id (int): Foreign key referencing a recipe.
        food_type_id (int): Foreign key referencing a food type.
    """

    _tablename_ = "recipes_food_types"
    recipe_id = Column(Integer, ForeignKey("recipes.recipe_id"), primary_key=True)
    food_type_id = Column(
        Integer, ForeignKey("food_types.food_type_id"), primary_key=True
    )


class Category(Base):
    """
    Represents a category for ingredients.

    Attributes:
        category_id (int): Primary key for the category.
        category_name (str): Name of the category.
        category_created (datetime): Timestamp when the category was created.
    """

    _tablename_ = "categories"
    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(50), nullable=False)
    category_created = Column(DateTime, default=datetime.utcnow)


class Ingredient(Base):
    """
    Represents an ingredient.

    Attributes:
        ingredient_id (int): Primary key for the ingredient.
        ingredient_name (str): Name of the ingredient.
        ingredient_calories_per_unit (decimal): Calories per unit of the ingredient.
        ingredient_price_per_unit (decimal): Price per unit of the ingredient.
        ingredient_created_date (datetime): Date when the ingredient was added.
        ingredient_expiration_date (datetime): Expiration date of the ingredient.
        ingredient_description (str): Description of the ingredient.
        category_id (int): Foreign key referencing the category of the ingredient.
    """

    _tablename_ = "ingredients"
    ingredient_id = Column(Integer, primary_key=True, index=True)
    ingredient_name = Column(String(100), nullable=False)
    ingredient_calories_per_unit = Column(DECIMAL(10, 2), nullable=False)
    ingredient_price_per_unit = Column(DECIMAL(10, 2), nullable=False)
    ingredient_created_date = Column(DateTime, nullable=False)
    ingredient_expiration_date = Column(DateTime, nullable=False)
    ingredient_description = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)


class MeasurementUnit(Base):
    """
    Represents a measurement unit.

    Attributes:
        unit_id (int): Primary key for the measurement unit.
        unit_name (str): Name of the measurement unit.
        unit_abbreviation (str): Abbreviation of the unit (e.g., 'kg').
        unit_type (str): Type of the unit ('mass', 'volume', 'unit').
    """

    _tablename_ = "measurement_units"
    unit_id = Column(Integer, primary_key=True, index=True)
    unit_name = Column(String(50), nullable=False)
    unit_abbreviation = Column(String(10), nullable=False)
    unit_type = Column(Enum("mass", "volume", "unit"), nullable=False)


class RecipeIngredient(Base):
    """
    Represents the relationship between recipes and ingredients.

    Attributes:
        recipe_id (int): Foreign key referencing a recipe.
        ingredient_id (int): Foreign key referencing an ingredient.
        quantity (decimal): Quantity of the ingredient used.
        measurement_unit_id (int): Foreign key referencing a measurement unit.
    """

    _tablename_ = "recipes_ingredients"
    recipe_id = Column(Integer, ForeignKey("recipes.recipe_id"), primary_key=True)
    ingredient_id = Column(
        Integer, ForeignKey("ingredients.ingredient_id"), primary_key=True
    )
    quantity = Column(DECIMAL(10, 2), nullable=False)
    measurement_unit_id = Column(
        Integer, ForeignKey("measurement_units.unit_id"), nullable=False
    )


class Menu(Base):
    """
    Represents a menu.

    Attributes:
        menu_id (int): Primary key for the menu.
        user_id (int): Foreign key referencing the user who created the menu.
        menu_created (datetime): Timestamp when the menu was created.
        menu_updated (datetime): Timestamp of the last menu update.
        menu_type (str): Type of the menu ('Breakfast', 'Lunch', 'Dinner', 'Other').
    """

    _tablename_ = "menus"
    menu_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    menu_created = Column(DateTime, default=datetime.utcnow)
    menu_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    menu_type = Column(Enum("Breakfast", "Lunch", "Dinner", "Other"), nullable=False)


class MenuRecipe(Base):
    """
    Represents the relationship between menus and recipes.

    Attributes:
        menu_id (int): Foreign key referencing a menu.
        recipe_id (int): Foreign key referencing a recipe.
    """

    _tablename_ = "menus_recipes"
    menu_id = Column(Integer, ForeignKey("menus.menu_id"), primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.recipe_id"), primary_key=True)


class MenuGroup(Base):
    """
    Represents the relationship between menus and groups.

    Attributes:
        menu_id (int): Foreign key referencing a menu.
        group_id (int): Foreign key referencing a group.
    """

    _tablename_ = "menus_groups"
    menu_id = Column(Integer, ForeignKey("menus.menu_id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.group_id"), primary_key=True)


class ShopListItem(Base):
    """
    Represents an item in a shopping list.

    Attributes:
        item_id (int): Primary key for the item.
        item_ingredient_id (int): Foreign key referencing an ingredient.
        item_quantity (decimal): Quantity of the ingredient.
        item_total_price (decimal): Total price of the item.
    """

    _tablename_ = "shop_list_items"
    item_id = Column(Integer, primary_key=True, index=True)
    item_ingredient_id = Column(
        Integer, ForeignKey("ingredients.ingredient_id"), nullable=False
    )
    item_quantity = Column(DECIMAL(10, 2), nullable=False)
    item_total_price = Column(DECIMAL(10, 2), nullable=False)


class PantryIngredient(Base):
    """
    Represents an ingredient stored in the pantry.

    Attributes:
        pantries_ingredients_id (int): Primary key for the pantry ingredient.
        ingredient_id (int): Foreign key referencing an ingredient.
        pantry_ingredient_quantity (decimal): Quantity of the ingredient in the pantry.
        pantry_ingredient_expiration_date (datetime): Expiration date of the ingredient.
        user_id (int): Foreign key referencing the user who owns the pantry.
    """

    _tablename_ = "pantries_ingredients"
    pantries_ingredients_id = Column(Integer, primary_key=True, index=True)
    ingredient_id = Column(
        Integer, ForeignKey("ingredients.ingredient_id"), nullable=False
    )
    pantry_ingredient_quantity = Column(DECIMAL(10, 2), nullable=False)
    pantry_ingredient_expiration_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class Notification(Base):
    """
    Represents a notification sent to a user.

    Attributes:
        notification_id (int): Primary key for the notification.
        user_id (int): Foreign key referencing the user receiving the notification.
        notification_type (str): Type of the notification ('Purchase Reminder',
        'Food Preparation', 'Product Expiration').
        notification_message (str): Message content of the notification.
        notification_created_date (datetime): Timestamp when the notification was created.
    """

    _tablename_ = "notifications"
    notification_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    notification_type = Column(
        Enum("Purchase Reminder", "Food Preparation", "Product Expiration"),
        nullable=False,
    )
    notification_message = Column(Text, nullable=False)
    notification_created_date = Column(DateTime, default=datetime.utcnow)


# Configurar la base de datos
DATABASE_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']
}/{DATABASE['name']}"
engine = create_engine(DATABASE_URL)


# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Crear las tablas en la base de datos
# def create_tables():
#     """
#     Create all tables defined in the SQLAlchemy Base metadata.

#     This function uses the SQLAlchemy `create_all` method to create all tables
#     defined in the Base metadata. The tables are created using the provided
#     database engine.

#     Returns:
#         None
#     """
#     Base.metadata.create_all(bind=engine)
