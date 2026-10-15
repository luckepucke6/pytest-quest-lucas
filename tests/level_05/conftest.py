import pytest
from dungeon.hero import Hero
from dungeon.inventory import Inventory, Item
from dungeon.shop import Listing, Shop

@pytest.fixture
def hero():
    hero = Hero("Ada")
    return hero

@pytest.fixture
def backpack():
    backpack = Inventory(20)
    return backpack

@pytest.fixture
def sword():
    sword = Item(name='sword', weight=0.8, value=15)
    return sword

@pytest.fixture
def shop(sword):
    listing = Shop([Listing(item=sword, price=12, stock=5)])
    return listing

@pytest.fixture
def rich_hero():
    rich_hero = Hero(name="Rich", gold=100)
    return rich_hero

@pytest.fixture
def tiny_backpack():
    tiny_backpack = Inventory(0.5)
    return tiny_backpack