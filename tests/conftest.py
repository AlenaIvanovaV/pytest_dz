from selene.support.shared import browser
import pytest


@pytest.fixture()
def set_desktop_browser():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()


@pytest.fixture()
def set_mobile_browser():
    browser.config.window_height = 844
    browser.config.window_width = 390
    yield
    browser.quit()

@pytest.fixture(params=["desktop", "mobile"])
def set_website_window_orientation(request):
    if request.param == "desktop":
        browser.config.window_height = 1080
        browser.config.window_width = 1920
    elif request.param == "mobile":
        browser.config.window_height = 844
        browser.config.window_width = 390

    return request.param