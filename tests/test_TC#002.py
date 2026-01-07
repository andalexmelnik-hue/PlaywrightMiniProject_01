from playwright.sync_api import expect

def test_intercept_200(menu):
    with menu.intercept(status=200):
        menu.page.goto("/")
    #menu.page.pause()
    expect(menu.page.get_by_role("heading", name="Espresso 1")).to_have_text("Espresso 1 $11.00")

def test_intercept_500(menu):
    with menu.intercept(status=500):
        menu.page.goto("/")
    #menu.page.pause()
    expect(menu.page.get_by_text("Coffee API Error")).to_be_visible()
    