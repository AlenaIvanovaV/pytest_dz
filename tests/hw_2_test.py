from selene.support.conditions import have
from selene.support.shared import browser


def test_desktop(set_desktop_browser):
       browser.open('https://github.com/')
       browser.element('[href="/login"]').click()
       assert browser.element("[class='auth-form-header p-0']").should(have.text("Sign in to GitHub"))

def test_mobile(set_mobile_browser):
       browser.open('https://github.com/')
       browser.element("[class='Button-label']").click()
       browser.element('[href="/login"]').click()
       assert browser.element("[class='auth-form-header p-0']").should(have.text("Sign in to GitHub"))