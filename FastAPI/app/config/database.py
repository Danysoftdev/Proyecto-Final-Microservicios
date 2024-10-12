from datetime import datetime
from peewee import *
from app.config.settings import DATABASE

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)


class RoleEnum(Enum):
    ADMIN = 'admin'
    MEMBER = 'member'

class DifficultyEnum(Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'

class UnitTypeEnum(Enum):
    MASS = 'mass'
    VOLUME = 'volume'
    UNIT = 'unit'

class MenuTypeEnum(Enum):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    OTHER = 'Other'

class NotificationTypeEnum(Enum):
    PURCHASE_REMINDER = 'Purchase Reminder'
    FOOD_PREPARATION = 'Food Preparation'
    PRODUCT_EXPIRATION = 'Product Expiration'

class UserModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=100)
    user_email = CharField(max_length=100, unique=True)
    user_password = CharField(max_length=255)
    user_pfp = CharField(max_length=255, null=True)
    user_created = DateTimeField(default=datetime.now)
    user_updated = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "users"

class GroupModel(Model):
    group_id = AutoField(primary_key=True)
    groups_name = CharField(max_length=100)
    groups_description = CharField(max_length=255, null=True)
    group_created = DateTimeField(default=datetime.now)
    group_updated = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "groups"

class UserGroupModel(Model):
    user_id = ForeignKeyField(UserModel, backref="user_groups", on_delete="CASCADE")
    group_id = ForeignKeyField(GroupModel, backref="group_users", on_delete="CASCADE")
    # rol = EnumField(choices=['admin', 'member'])
    rol = CharField(
        choices=[(role.value, role.name) for role in RoleEnum]
    )

    class Meta:
        table_name = "user_groups"
        primary_key = False

class RecipeModel(Model):
    recipe_id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref="recipes", on_delete="CASCADE")
    recipe_name = CharField(max_length=100)
    recipe_description = TextField()
    recipe_prepare_time = IntegerField()
    # recipe_difficulty = EnumField(choices=['easy', 'medium', 'hard'])
    recipe_difficulty = CharField(
        choices=[(difficulty.value, difficulty.name) for difficulty in DifficultyEnum]
    )
    recipe_portions = TimeField()
    recipe_instructions = TextField(null=True)
    recipe_is_public = BooleanField(default=False)
    recipe_created = DateTimeField(default=datetime.now)
    recipe_updated = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "recipes"

class FoodTypeModel(Model):
    food_type_id = AutoField(primary_key=True)
    food_type_name = CharField(max_length=50)
    food_type_created = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "food_types"

class RecipeFoodTypeModel(Model):
    recipe_id = ForeignKeyField(RecipeModel, backref="food_types", on_delete="CASCADE")
    food_type_id = ForeignKeyField(FoodTypeModel, backref="recipes", on_delete="CASCADE")

    class Meta:
        table_name = "recipes_food_types"
        primary_key = False

class CategoryModel(Model):
    category_id = AutoField(primary_key=True)
    category_name = CharField(max_length=50)
    category_created = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "categories"

class IngredientModel(Model):
    ingredient_id = AutoField(primary_key=True)
    ingredient_name = CharField(max_length=100)
    ingredient_calories_per_unit = DecimalField(max_digits=10, decimal_places=2)
    ingredient_price_per_unit = DecimalField(max_digits=10, decimal_places=2)
    ingredient_created_date = DateField()
    ingredient_expiration_date = DateField()
    ingredient_description = TextField()
    category_id = ForeignKeyField(CategoryModel, backref="ingredients", on_delete="CASCADE")

    class Meta:
        table_name = "ingredients"

class MeasurementUnitModel(Model):
    unit_id = AutoField(primary_key=True)
    unit_name = CharField(max_length=50)
    unit_abbreviation = CharField(max_length=10)
    unit_type = EnumField(choices=['mass', 'volume', 'unit'])

    class Meta:
        table_name = "measurement_units"

class RecipeIngredientModel(Model):
    recipe_id = ForeignKeyField(RecipeModel, backref="ingredients", on_delete="CASCADE")
    ingredient_id = ForeignKeyField(IngredientModel, backref="recipes", on_delete="CASCADE")
    quantity = DecimalField(max_digits=10, decimal_places=2)
    measurement_unit_id = ForeignKeyField(MeasurementUnitModel, backref="recipe_ingredients", on_delete="CASCADE")

    class Meta:
        table_name = "recipes_ingredients"
        primary_key = False

class MenuModel(Model):
    menu_id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref="menus", on_delete="CASCADE")
    menu_created = DateTimeField(default=datetime.now)
    menu_updated = DateTimeField(default=datetime.now)
    menu_type = CharField(
        choices=[(menu.value, menu.name) for menu in MenuTypeEnum]
    )
    class Meta:
        table_name = "menus"

class MenuRecipeModel(Model):
    menu_id = ForeignKeyField(MenuModel, backref="recipes", on_delete="CASCADE")
    recipe_id = ForeignKeyField(RecipeModel, backref="menus", on_delete="CASCADE")

    class Meta:
        table_name = "menus_recipes"
        primary_key = False

class MenuGroupModel(Model):
    menu_id = ForeignKeyField(MenuModel, backref="groups", on_delete="CASCADE")
    group_id = ForeignKeyField(GroupModel, backref="menus", on_delete="CASCADE")

    class Meta:
        table_name = "menus_groups"
        primary_key = False

class ShopListItemModel(Model):
    item_id = AutoField(primary_key=True)
    item_ingredient_id = ForeignKeyField(IngredientModel, backref="shop_list_items", on_delete="CASCADE")
    item_quantity = DecimalField(max_digits=10, decimal_places=2)
    item_total_price = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        table_name = "shop_list_items"

class PantriesIngredientModel(Model):
    pantries_ingredients_id = AutoField(primary_key=True)
    ingredient_id = ForeignKeyField(IngredientModel, backref="pantries", on_delete="CASCADE")
    pantry_ingredient_quantity = DecimalField(max_digits=10, decimal_places=2)
    pantry_ingredient_expiration_date = DateField()
    user_id = ForeignKeyField(UserModel, backref="pantries_ingredients", on_delete="CASCADE")

    class Meta:
        table_name = "pantries_ingredients"

class NotificationModel(Model):
    notification_id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref="notifications", on_delete="CASCADE")
    notification_message = TextField()
    notification_type = CharField(
        choices=[(notification.value, notification.name) for notification in NotificationTypeEnum]
    )
    notification_created_date = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "notifications"