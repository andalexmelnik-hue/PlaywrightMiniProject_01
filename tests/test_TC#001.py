from playwright.sync_api import expect
from page_objects.menu import Menu
import pytest

coffee_data = [
    ("Espresso", "$10.00"),
    ("Cappuccino", "$19.00"),
    ("Cafe Latte", "$16.00"),
    ("Mocha", "$8.00"),
    ("Americano", "$7.00")
]

@pytest.mark.smoke
@pytest.mark.parametrize("coffee_name, expected_price", coffee_data)
# Add Espresso to the cart from the menu and check price'
def test_add_one_coffee(menu: Menu, coffee_name, expected_price):   
    menu.add_coffee(coffee_name)

    assert menu.get_price() == f'Total: {expected_price}'
    expect(menu.get_cart()).to_contain_text("cart (1)")

modified_coffe_names = [(coffee_data[i][0], coffee_data[j][0], 
                         coffee_data[i][1], coffee_data[j][1]) 
                        for i in range(len(coffee_data)) 
                        for j in range(i + 1, len(coffee_data))]

@pytest.mark.smoke
@pytest.mark.parametrize("coffee1, coffee2, price1, price2", 
                         modified_coffe_names)
def test_add_two_coffees(menu: Menu, coffee1, coffee2, price1, price2):
    menu.add_coffee(coffee1)
    menu.add_coffee(coffee2)

    expected_price = (float(price1.replace("$", "")) + float(price2.replace("$", "")))
    assert menu.get_price() == f'Total: ${expected_price:.2f}'
    expect(menu.get_cart()).to_contain_text("cart (2)")

