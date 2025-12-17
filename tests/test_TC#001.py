from playwright.sync_api import expect
from page_objects.menu import Menu

# Add Espresso to the cart from the menu and check price'
def test_add_one_coffee(menu: Menu):
    menu.add_coffee("Espresso")
    expected_price = menu.get_coffee_price("Espresso")  
    
    assert menu.get_price() == f'Total: ${expected_price:.2f}'
    expect(menu.get_cart()).to_contain_text("cart (1)")
    

def test_add_two_coffees(menu: Menu):
    menu.add_coffee("Mocha")
    menu.add_coffee("Cafe Latte")
    expected_price = menu.get_coffee_price("Mocha") + menu.get_coffee_price("Cafe Latte")
    
    assert menu.get_price() == f'Total: ${expected_price:.2f}'
    expect(menu.get_cart()).to_contain_text("cart (2)")
    
# TO DO: Add more tests to cover Menu page functionalities