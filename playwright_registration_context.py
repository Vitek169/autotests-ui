from playwright.sync_api import sync_playwright

# Открываем страницу при помощи Playwright и менеджера контекста
with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режими с визувлом
    browser = playwright.chromium.launch(headless=False)
    # Создание нового контекста браузера(новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Создаем новую страницу в рамках контекста
    page = context.new_page()
    # переходим по ссылке
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    login_name = page.get_by_test_id('registration-form-username-input').locator('input')
    login_name.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера(куки, LocalStorage) в файл для дальнейшего использования
    context.storage_state(path='browser-state.json')

# Код в который передается файл с данными состояния браузера, для упрощения авторизации
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json') # Указываем путь до файла в котором сохранено состояние браузера
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    page.wait_for_timeout(5000)







