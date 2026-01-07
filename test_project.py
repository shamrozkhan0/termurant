from project import Restaurant
import pytest

def test_validate_and_distribute():
    rest = Restaurant()
    rest.menu={"burger": 7}
    assert rest.validate_and_distribute("burger x 2") == ("burger", 2)

def test_validate_and_distribute_without_spacing():
    rest = Restaurant()
    rest.menu = {"pizza": 7}
    assert rest.validate_and_distribute("pizzax2") == ("pizza", 2)

def test_validate_and_distribute_case_insensitive():
    rest = Restaurant()
    rest.menu = {"taco": 7}
    assert rest.validate_and_distribute("TaCo x 2") == ('taco', 2)

def test_validate_and_distribute_invalid():
    rest = Restaurant()
    rest.menu = {"burger": 7}
    with pytest.raises(ValueError):
        rest.validate_and_distribute("burger  2")

menu = {
        'burger': 7,
        'pizza': 10,
        'taco': 5,
        'fries': 3
    }

def test_order_total():
    rest = Restaurant()
    rest.menu = menu
    rest.order = {'burger': 3}
    assert rest.order_total() == 21

def test_order_total_multiple_item():
    rest2 = Restaurant()
    rest2.menu = menu
    rest2.order = {
        'burger': 3,
        'pizza': 2
    }
    assert rest2.order_total() == 41

