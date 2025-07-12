import pytest # Импорт pytest
from playwright.sync_api import sync_playwright, \
    Page # импортируем класс страницы, для использования его как аннотацию типов

from playwright_authorization import browser


@pytest.fixture # Объявляем фикстуру, по умолчанию scop=function, то что нам и нужно
def chromium_page() -> Page: # Аннотируем возвращаемое фикстурой значение
    # Ниже идет инициализация и открытие новой страницы
    with sync_playwright() as playwright:
        # Запуск браузера
        browser = playwright.chromium.launch(headless=False)

    # Передаем страницу для использования в тесте, после теста она автоматически закроется
        yield browser.new_page()
