from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    # Переходим на страницу
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    # Находим ссылку Registration
    registration_button =  page.get_by_test_id('registration-page-registration-button')

    # Через блок try-except проверяем что кнопка Registration выключена, если она включена, выйдет соответствующее сообщение
    try:
        expect(registration_button).to_be_disabled()
        print('Button is Disabled')
    except AssertionError:
        print('Кнопка должна быть не видна')

    # Заполняем поля регистрации
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    login_name = page.get_by_test_id('registration-form-username-input').locator('input')
    login_name.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    page.wait_for_timeout(3000)

    # Через блок try-except проверяем что кнопка Registration включена, если она выключена, выйдет соответствующее сообщение
    try:
        expect(registration_button).to_be_enabled()
        print('Button is Enabled')
    except AssertionError:
        print('Кнопка должна быть видна')

    page.wait_for_timeout(3000)