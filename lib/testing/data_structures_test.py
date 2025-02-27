# lib/testing/test_data_structures.py
from lib.data_structures import (
    get_names,
    get_spiciest_foods,
    print_spicy_foods,
    get_spicy_food_by_cuisine,
    print_spiciest_foods,
    average_heat_level,
    create_spicy_food,
)

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def test_get_names():
    assert get_names(spicy_foods) == ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

def test_get_spiciest_foods():
    expected = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
    ]
    assert get_spiciest_foods(spicy_foods) == expected

def test_print_spicy_foods(capfd):
    print_spicy_foods(spicy_foods)
    captured = capfd.readouterr()
    assert "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶" in captured.out
    assert "Buffalo Wings (American) | Heat Level: 🌶🌶🌶" in captured.out
    assert "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶" in captured.out

def test_get_spicy_food_by_cuisine():
    assert get_spicy_food_by_cuisine(spicy_foods, "American") == {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    }
    assert get_spicy_food_by_cuisine(spicy_foods, "Thai") == {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    }
    assert get_spicy_food_by_cuisine(spicy_foods, "Indian") is None

def test_print_spiciest_foods(capfd):
    print_spiciest_foods(spicy_foods)
    captured = capfd.readouterr()
    assert "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶" in captured.out
    assert "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶" in captured.out
    assert "Buffalo Wings (American) | Heat Level: 🌶🌶🌶" not in captured.out

def test_average_heat_level():
    assert average_heat_level(spicy_foods) == 6

def test_create_spicy_food():
   new_food = {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}
   updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
   assert len(updated_spicy_foods) == 4
   assert updated_spicy_foods[-1] == new_food