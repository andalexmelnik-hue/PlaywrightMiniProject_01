from playwright.sync_api import expect, Page, Browser, BrowserContext
from pytest import mark
from pytest import fixture
import os

config = "circus_auth.json"

@fixture(scope="session", autouse=True)
def circus(browser: Browser):
    # Simulate user login via UI
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://circus.qamania.org/")
    page.get_by_placeholder("Login").fill("a")
    page.get_by_placeholder("Password").fill("a")
    with page.expect_navigation(url='**', wait_until="networkidle"):
        page.get_by_role("button", name="Login").click()
    context.storage_state(path=config)
    page.close()
    yield context
    if os.path.exists(config):
        os.remove(config)
        
def test_api_1(circus):
    api_context = circus.request
    response = api_context.get("https://circus.qamania.org/ws/performances")
    expect(response).to_be_ok()

def test_api_2(circus):
    api_context = circus.request
    response = api_context.get("https://circus.qamania.org/ws/performances")
    expect(response).to_be_ok()
    
@mark.browser_context_args(storage_state=config)
def test_api_3(context: BrowserContext):
    api_context = context.request
    response = api_context.get("https://circus.qamania.org/ws/performances")
    expect(response).to_be_ok()    