"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (1280, 720), (430, 932), (393, 852)])
def browser_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


def test_github_desktop(browser_size):
    if browser.config.window_width < 1000:
        pytest.skip(reason='Не запускаем мобильные')
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_size):
    if browser.config.window_width > 1000:
        pytest.skip(reason='Не запускаем десктопные')
    browser.open('https://github.com/')
    browser.element('[class="HeaderMenu-toggle-bar rounded my-1"]').click()
    browser.element('[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
