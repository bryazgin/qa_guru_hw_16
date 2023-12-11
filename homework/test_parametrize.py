"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (430,932)])
def browser_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.mark.parametrize("browser_size", [(1920, 1080)], ids=['1920x1080'], indirect=True)
def test_github_desktop(browser_size):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_size", [(430, 932)], indirect=True)
def test_github_mobile(browser_size):
    browser.open('https://github.com/')
    browser.element('[class="HeaderMenu-toggle-bar rounded my-1"]').click()
    browser.element('[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
