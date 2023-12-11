"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


@pytest.fixture()
def make_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture()
def make_mobile():
    browser.config.window_width = 430
    browser.config.window_height = 932

def test_github_desktop(make_desktop):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))



def test_github_mobile(make_mobile):
    browser.open('https://github.com/')
    browser.element('[class="HeaderMenu-toggle-bar rounded my-1"]').click()
    browser.element('[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
