"""
This module provides database-related functionalities and enumerations
for a food recipe application.

Imports:
    datetime (module): Supplies classes for manipulating dates and times.
    enum (module): Provides support for enumerations.
    peewee (module): An ORM (Object Relational Mapping) library for Python.
    app.config.settings (module): Contains the database configuration settings.

Classes:
    RoleEnum (Enum): Enumeration for user roles.
    DifficultyEnum (Enum): Enumeration for difficulty levels.
    UnitTypeEnum (Enum): Enumeration for unit types.
    MenuTypeEnum (Enum): Enumeration for menu types.
    NotificationTypeEnum (Enum): Enumeration for notification types.
    UserModel (Model): Represents a user in the database.
    GroupModel (Model): Represents a group in the database.
    UserGroupModel (Model): Represents the relationship between users and groups.
    RecipeModel (Model): Represents a recipe in the database.
    FoodTypeModel (Model): Represents a food type in the database.
    RecipeFoodTypeModel (Model): Represents the relationship between recipes and food types.
    CategoryModel (Model): Represents a category in the database.
    IngredientModel (Model): Represents an ingredient in the database.
    MeasurementUnitModel (Model): Represents a measurement unit in the database.
    RecipeIngredientModel (Model): Represents the relationship between recipes and ingredients.
    MenuModel (Model): Represents a menu in the database.
    MenuRecipeModel (Model): Represents the relationship between menus and recipes.
    MenuGroupModel (Model): Represents the relationship between menus and groups.
    ShopListItemModel (Model): Represents a shopping list item in the database.
    PantriesIngredientModel (Model): Represents the relationship between pantries and ingredients.
    NotificationModel (Model): Represents a notification in the database.
"""

from datetime import datetime
from enum import Enum
from peewee import (
    Model,
    AutoField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    TextField,
    BooleanField,
    DateField,
    DecimalField,
    TimeField,
    MySQLDatabase,
)
from app.config.settings import DATABASE

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)


class RoleEnum(Enum):
    """
    Enumeration for user roles.

    Attributes:
        ADMIN (str): Represents an admin user.
        MEMBER (str): Represents a member user.
    """

    ADMIN = "admin"
    MEMBER = "member"


class DifficultyEnum(Enum):
    """
    Enumeration for difficulty levels.

    Attributes:
        EASY (str): Represents an easy difficulty level.
        MEDIUM (str): Represents a medium difficulty level.
        HARD (str): Represents a hard difficulty level.
    """

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class UnitTypeEnum(Enum):
    """
    Enumeration for unit types.

    Attributes:
        MASS (str): Represents mass unit type.
        VOLUME (str): Represents volume unit type.
        UNIT (str): Represents unit type.
    """

    MASS = "mass"
    VOLUME = "volume"
    UNIT = "unit"


class MenuTypeEnum(Enum):
    """
    Enumeration for menu types.

    Attributes:
        BREAKFAST (str): Represents breakfast menu type.
        LUNCH (str): Represents lunch menu type.
        DINNER (str): Represents dinner menu type.
        OTHER (str): Represents other menu types.
    """

    BREAKFAST = "Breakfast"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    OTHER = "Other"


class NotificationTypeEnum(Enum):
    """
    Enumeration for notification types.

    Attributes:
        PURCHASE_REMINDER (str): Represents a purchase reminder notification.
        FOOD_PREPARATION (str): Represents a food preparation notification.
        PRODUCT_EXPIRATION (str): Represents a product expiration notification.
    """

    PURCHASE_REMINDER = "Purchase Reminder"
    FOOD_PREPARATION = "Food Preparation"
    PRODUCT_EXPIRATION = "Product Expiration"


class UserModel(Model):
    """
    Represents a user in the database.

    Attributes:
        id (AutoField): The primary key for the user.
        username (CharField): The username of the user, with a maximum length of 100 characters.
        user_email (CharField): The email of the user, with a maximum length of 100 characters
        and must be unique.
        user_password (CharField): The password of the user, with a maximum length of 255 characters
        user_pfp (CharField): The profile picture URL of the user, with a maximum
        length of 255 characters. This field is optional.
        user_created (DateTimeField): The timestamp when the user was created.
        Defaults to the current date and time.
        user_updated (DateTimeField): The timestamp when the user was last updated.
        Defaults to the current date and time.
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
        Meta:
        table_name (str): The name of the database table for this model.

        """

        table_name = "users"


class GroupModel(Model):
    """
    Represents a group in the database.

    Attributes:
        group_id (AutoField): The primary key for the group.
        groups_name (CharField): The name of the group, with a maximum length of 100 characters.
        groups_description (CharField): The description of the group,
        with a maximum length of 255 characters.
        This field is optional.
        group_created (DateTimeField): The timestamp when the group was created.
        Defaults to the current date and time.
        group_updated (DateTimeField): The timestamp when the group was last updated.
        Defaults to the current date and time.
    """

    group_id = AutoField(primary_key=True)
    groups_name = CharField(max_length=100)
    groups_description = CharField(max_length=255, null=True)
    group_created = DateTimeField(default=datetime.now)
    group_updated = DateTimeField(default=datetime.now)

    class Meta:
        """
        Meta:
        table_name (str): The name of the database table for this model.
        """

        table_name = "groups"


class UserGroupModel(Model):
    """
    Represents the relationship between users and groups in the database.

    Attributes:
        user_id (ForeignKeyField): A foreign key to the UserModel, representing the user.
        group_id (ForeignKeyField): A foreign key to the GroupModel, representing the group.
        rol (CharField): The role of the user within the group, with choices defined by RoleEnum.

    Meta:
        table_name (str): The name of the database table for this model.
        primary_key (bool): Indicates that this model does not have a single primary key.
    """

    user_id = ForeignKeyField(UserModel, backref="user_groups", on_delete="CASCADE")
    group_id = ForeignKeyField(GroupModel, backref="group_users", on_delete="CASCADE")
    rol = CharField(choices=[(role.value, role.name) for role in RoleEnum])

    class Meta:
        """
        Meta:
        table_name (str): The name of the database table for this model.
        primary_key (bool): Indicates that this model does not have a single primary key.
        """

        table_name = "user_groups"
        primary_key = False


class RecipeModel(Model):
    """
    Represents a recipe in the database.

    Attributes:
        recipe_id (AutoField): The primary key for the recipe.
        user_id (ForeignKeyField): A foreign key to the UserModel,
        representing the user who created the recipe.
        recipe_name (CharField): The name of the recipe, with a maximum length of 100 characters.
        recipe_description (TextField): A detailed description of the recipe.
        recipe_prepare_time (IntegerField): The preparation time for the recipe, in minutes.
        recipe_difficulty (CharField): The difficulty level of the recipe,
        with choices defined by DifficultyEnum.
        recipe_portions (TimeField): The number of portions the recipe yields.
        recipe_instructions (TextField): The instructions for preparing the recipe.
        This field is optional.
        recipe_is_public (BooleanField): Indicates whether the recipe is public. Defaults to False.
        recipe_created (DateTimeField): The timestamp when the recipe was created.
        Defaults to the current date and time.
        recipe_updated (DateTimeField): The timestamp when the recipe was last updated.
        Defaults to the current date and time.
    """

    recipe_id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref="recipes", on_delete="CASCADE")
    recipe_name = CharField(max_length=100)
    recipe_description = TextField()
    recipe_prepare_time = IntegerField()
    recipe_difficulty = CharField(
        choices=[(difficulty.value, difficulty.name) for difficulty in DifficultyEnum]
    )
    recipe_portions = TimeField()
    recipe_instructions = TextField(null=True)
    recipe_is_public = BooleanField(default=False)
    recipe_created = DateTimeField(default=datetime.now)
    recipe_updated = DateTimeField(default=datetime.now)

    class Meta:
        """
        Meta:
        table_name (str): The name of the database table for this model.
        """

        table_name = "recipes"


class FoodTypeModel(Model):
    """
    FoodTypeModel is a model class representing the 'food_types' table in the database.
    Attributes:
        food_type_id (AutoField): The primary key for the food type.
        food_type_name (CharField): The name of the food type, with a maximum length of 50 character
        food_type_created (DateTimeField): The timestamp when the food type was created,
        defaults to the current datetime.
    """

    food_type_id = AutoField(primary_key=True)
    food_type_name = CharField(max_length=50)
    food_type_created = DateTimeField(default=datetime.now)

    class Meta:
        """
        Meta:
        table_name (str): The name of the table in the database.
        """

        table_name = "food_types"


class RecipeFoodTypeModel(Model):
    """
    Represents the many-to-many relationship between recipes and food types.

    Attributes:
        recipe_id (int): Foreign key referencing a specific recipe.
        food_type_id (int): Foreign key referencing a specific food type.

    """

    recipe_id = ForeignKeyField(RecipeModel, backref="food_types", on_delete="CASCADE")
    food_type_id = ForeignKeyField(
        FoodTypeModel, backref="recipes", on_delete="CASCADE"
    )

    class Meta:
        """
        Meta:
        table_name (str): Name of the database table ("recipes_food_types").
        primary_key (bool): No single primary key, using a composite key instead.
        """

        table_name = "recipes_food_types"
        primary_key = False


class CategoryModel(Model):
    """
    Represents a category that groups related ingredients.

    Attributes:
        category_id (int): Primary key for the category.
        category_name (str): Name of the category (e.g., "Dairy", "Vegetables").
        category_created (datetime): Timestamp of when the category was created.


    """

    category_id = AutoField(primary_key=True)
    category_name = CharField(max_length=50)
    category_created = DateTimeField(default=datetime.now)

    class Meta:
        """
        Meta:
        table_name (str): Name of the database table ("categories").
        """

        table_name = "categories"


class IngredientModel(Model):
    """
    Represents an ingredient used in recipes.

    Attributes:
        ingredient_id (int): Primary key for the ingredient.
        ingredient_name (str): Name of the ingredient (e.g., "Tomato").
        ingredient_calories_per_unit (float): Caloric value per unit of the ingredient.
        ingredient_price_per_unit (float): Price per unit of the ingredient.
        ingredient_created_date (date): Date when the ingredient record was created.
        ingredient_expiration_date (date): Expiration date of the ingredient.
        ingredient_description (str): Additional details or notes about the ingredient.
        category_id (int): Foreign key referencing the category to which the ingredient belongs.


    """

    ingredient_id = AutoField(primary_key=True)
    ingredient_name = CharField(max_length=100)
    ingredient_calories_per_unit = DecimalField(max_digits=10, decimal_places=2)
    ingredient_price_per_unit = DecimalField(max_digits=10, decimal_places=2)
    ingredient_created_date = DateField()
    ingredient_expiration_date = DateField()
    ingredient_description = TextField()
    category_id = ForeignKeyField(
        CategoryModel, backref="ingredients", on_delete="CASCADE"
    )

    class Meta:
        """
        Meta:
        table_name (str): Name of the database table ("ingredients").
        """

        table_name = "ingredients"


class MeasurementUnitModel(Model):
    """
    Represents a measurement unit used for ingredients, such as mass, volume, or units.

    Attributes:
        unit_id (int): Primary key for the measurement unit.
        unit_name (str): Full name of the measurement unit (e.g., "Kilogram").
        unit_abbreviation (str): Abbreviation of the unit (e.g., "kg").
        unit_type (str): Type of the unit, restricted to 'mass', 'volume', or 'unit'.


    """

    unit_id = AutoField(primary_key=True)
    unit_name = CharField(max_length=50)
    unit_abbreviation = CharField(max_length=10)
    unit_type = CharField(choices=[(unit.value, unit.name) for unit in UnitTypeEnum])

    class Meta:
        """
         Meta:
        table_name (str): The name of the table in the database ("measurement_units").
        """

        table_name = "measurement_units"


class RecipeIngredientModel(Model):
    """
    Represents the relationship between recipes and ingredients.

    Attributes:
        recipe_id (int): Foreign key to the recipe.
        ingredient_id (int): Foreign key to the ingredient.
        quantity (float): Quantity of the ingredient used in the recipe.
        measurement_unit_id (int): Foreign key to the measurement unit used for the quantity.


    """

    recipe_id = ForeignKeyField(RecipeModel, backref="ingredients", on_delete="CASCADE")
    ingredient_id = ForeignKeyField(
        IngredientModel, backref="recipes", on_delete="CASCADE"
    )
    quantity = DecimalField(max_digits=10, decimal_places=2)
    measurement_unit_id = ForeignKeyField(
        MeasurementUnitModel, backref="recipe_ingredients", on_delete="CASCADE"
    )

    class Meta:
        """
        Meta:
        table_name (str): The name of the table ("recipes_ingredients").
        primary_key (bool): This table does not use a single primary key, but rather a composite key
        """

        table_name = "recipes_ingredients"
        primary_key = False


class MenuModel(Model):
    """
    Represents a menu created by a user, containing various recipes.

    Attributes:
        menu_id (int): Primary key for the menu.
        user_id (int): Foreign key to the user who created the menu.
        menu_created (datetime): Timestamp of when the menu was created.
        menu_updated (datetime): Timestamp of the last update.
        menu_type (str): Type of the menu (e.g., 'Breakfast', 'Lunch', etc.).


    """

    menu_id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref="menus", on_delete="CASCADE")
    menu_created = DateTimeField(default=datetime.now)
    menu_updated = DateTimeField(default=datetime.now)
    menu_type = CharField(choices=[(menu.value, menu.name) for menu in MenuTypeEnum])

    class Meta:
        """
        Meta:
        table_name (str): The name of the table ("menus").
        """

        table_name = "menus"


class MenuRecipeModel(Model):
    """
    Represents the relationship between menus and recipes.

    Attributes:
        menu_id (int): Foreign key to the menu.
        recipe_id (int): Foreign key to the recipe.


    """

    menu_id = ForeignKeyField(MenuModel, backref="recipes", on_delete="CASCADE")
    recipe_id = ForeignKeyField(RecipeModel, backref="menus", on_delete="CASCADE")

    class Meta:
        """
        Meta:
        table_name (str): The name of the table ("menus_recipes").
        primary_key (bool): This table does not use a single primary key but a composite key.
        """

        table_name = "menus_recipes"
        primary_key = False


class MenuGroupModel(Model):
    """
    Represents the relationship between menus and groups.

    Attributes:
        menu_id (int): Foreign key to the menu.
        group_id (int): Foreign key to the group.


    """

    menu_id = ForeignKeyField(MenuModel, backref="groups", on_delete="CASCADE")
    group_id = ForeignKeyField(GroupModel, backref="menus", on_delete="CASCADE")

    class Meta:
        """
        Meta:
        table_name (str): The name of the table ("menus_groups").
        primary_key (bool): This table does not use a single primary key but a composite key.
        """

        table_name = "menus_groups"
        primary_key = False


class ShopListItemModel(Model):
    """
    Represents an item in a shopping list.

    Attributes:
        item_id (int): Primary key for the shopping list item.
        item_ingredient_id (int): Foreign key to the ingredient.
        item_quantity (float): Quantity of the ingredient to be purchased.
        item_total_price (float): Total price for the quantity of the ingredient.


    """

    item_id = AutoField(primary_key=True)
    item_ingredient_id = ForeignKeyField(
        IngredientModel, backref="shop_list_items", on_delete="CASCADE"
    )
    item_quantity = DecimalField(max_digits=10, decimal_places=2)
    item_total_price = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """
        Meta:
        table_name (str): The name of the table ("shop_list_items").
        """

        table_name = "shop_list_items"


class PantriesIngredientModel(Model):
    """
    Represents an ingredient stored in a user's pantry.

    Attributes:
        pantries_ingredients_id (int): Primary key for the pantry ingredient entry.
        ingredient_id (int): Foreign key to the ingredient.
        pantry_ingredient_quantity (float): Quantity of the ingredient in the pantry.
        pantry_ingredient_expiration_date (date): Expiration date of the ingredient.
        user_id (int): Foreign key to the user who owns the pantry.


    """

    pantries_ingredients_id = AutoField(primary_key=True)
    ingredient_id = ForeignKeyField(
        IngredientModel, backref="pantries", on_delete="CASCADE"
    )
    pantry_ingredient_quantity = DecimalField(max_digits=10, decimal_places=2)
    pantry_ingredient_expiration_date = DateField()
    user_id = ForeignKeyField(
        UserModel, backref="pantries_ingredients", on_delete="CASCADE"
    )

    class Meta:
        """
        Meta:
        table_name (str): The name of the table ("pantries_ingredients").
        """

        table_name = "pantries_ingredients"


class NotificationModel(Model):
    """
    Represents a notification sent to a user.

    Attributes:
        notification_id (int): Primary key for the notification.
        user_id (int): Foreign key to the user receiving the notification.
        notification_message (str): Content of the notification.
        notification_type (str): Type of the notification (e.g., 'Purchase Reminder').
        notification_created_date (datetime): Timestamp of when the notification was created.
    """

    notification_id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref="notifications", on_delete="CASCADE")
    notification_message = TextField()
    notification_type = CharField(
        choices=[
            (notification.value, notification.name)
            for notification in NotificationTypeEnum
        ]
    )
    notification_created_date = DateTimeField(default=datetime.now)

    class Meta:
        """
        Meta:
        table_name (str): The name of the table ("notifications").
        """

        table_name = "notifications"
