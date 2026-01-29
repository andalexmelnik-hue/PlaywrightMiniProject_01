from playwright.sync_api import expect, Page
config = "circus_auth.json"

def test_api_positive(menu):
    api_context = menu.page.context.request
    response = api_context.get("/list.json")
    expect(response).to_be_ok()
    assert len(response.json()) == 10

def test_api_negative(menu):
    data = {"invalid": "data"}
    api_context = menu.page.context.request
    response = api_context.post("/list.json", data=data)
    expect(response).not_to_be_ok() # expecting failure due to invalid data 
#test comment
