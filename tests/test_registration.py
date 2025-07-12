import pytest
from playwright.sync_api import sync_playwright, expect, Page

#@pytest.mark.ui # Добавляем маркировку ui
#@pytest.mark.regression # Добавляем маркировку regression
@pytest.mark.smoke # Добавляем маркировку smoke
@pytest.mark.registration # Добавляем маркировку registration
def test_successful_registration(chromium_page: Page):
        # переходим по ссылке
        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        login_name = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        login_name.fill('username')

        password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняем состояние браузера(куки, LocalStorage) в файл для дальнейшего использования
        # context.storage_state(path='/Users/katerinamatuizo/QA/autotests-ui/browser-state.json')
        #
        # Код в который передается файл с данными состояния браузера, для упрощения авторизации
        # with sync_playwright() as playwright:
        # browser = playwright.chromium.launch(headless=False)
        # context = browser.new_context(
        #     storage_state='/Users/katerinamatuizo/QA/autotests-ui/browser-state.json')  # Указываем путь до файла в котором сохранено состояние браузера
        # page = context.new_page()
        # page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        # page.wait_for_timeout(5000)


