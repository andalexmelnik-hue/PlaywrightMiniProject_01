from playwright.sync_api import expect

# Test console events
def test_events_1(menu):
    menu.goto("https://coffee-cart.app/?breakable=1")
    for i in range(5):
        menu.get_coffee_item("Espresso").click()

# Test page events
def test_events_2(menu):
    context = menu.get_context()
    with context.expect_page() as new_page_info:
        crt = menu.get_cart()
        crt.click(button="middle")
    page_2 = new_page_info.value
    assert len(context.pages) == 2
    page_2.close()
    assert len(context.pages) == 1
    
def test_events_3(menu):
    nah_button = menu.get_nah_button()
    
    def handler():
        nah_button.click()
    
    menu.page.add_locator_handler(nah_button, handler)
    
    for i in range(10):
        menu.add_coffee("Espresso")
    expect(menu.page.locator('.pay')).to_contain_text("$100")

def test_events_4(menu):
    nah_button = menu.get_nah_button()
    for i in range(3):
        menu.add_coffee("Espresso")
    nah_button.wait_for(state="visible")
    nah_button.click()
    nah_button.wait_for(state="hidden")
    expect(nah_button).to_be_hidden()
    