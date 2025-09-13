import pytest # Импорт pytest
from playwright.sync_api import  Page, Playwright



@pytest.fixture # Объявляем фикстуру, по умолчанию scop=function, то что нам и нужно
def chromium_page(playwright:Playwright) -> Page: # Аннотируем возвращаемое фикстурой значение
    # Запуск браузера
    browser = playwright.chromium.launch(headless=False)
    # Передаем страницу для использования в тесте, после теста она автоматически закроется
    yield browser.new_page()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Создаем новую страницу в рамках контекста
    page = context.new_page()
    try:
        # переходим по ссылке
        page.goto(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        # Вводим регистрационные данные
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        login_name = page.get_by_test_id('registration-form-username-input').locator('input')
        login_name.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняем состояние браузера(куки, LocalStorage) в файл для дальнейшего использования
        context.storage_state(path='browser-context.json')
        context.storage_state(path='/Users/katerinamatuizo/QA/autotests-ui/browser-state.json')
    finally:
        browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        storage_state='/Users/katerinamatuizo/QA/autotests-ui/browser-state.json')  # Указываем путь до файла в котором сохранено состояние браузера
    page = context.new_page()
    yield page
    browser.close()




