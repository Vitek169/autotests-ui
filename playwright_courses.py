from playwright.sync_api import sync_playwright, expect


# Открываем страницу при помощи Playwright и менеджера контекста
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    # Создание нового контекста браузера(новая сессия, которая изолирована от других, вместо browser будем создавать новую страницу через context)
    context = browser.new_context()
    # Создаем новую страницу в рамках контекста
    page = context.new_page()
    # переходим по ссылке
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
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

# Код в который передается файл с данными состояния браузера, для упрощения авторизации
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    # Указываем путь до файла в котором сохранено состояние браузера
    context = browser.new_context(storage_state='browser-context.json')
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    #Проверяем наличие элементов текста
    courses_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_text).to_have_text('Courses')

    result_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_text).to_have_text('There is no results')

    result_from_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(result_from_text).to_have_text('Results from the load test pipeline will be displayed here')

    # Проверка на видимость иконки папки
    folder_image = page.get_by_test_id('courses-list-empty-view-icon')
    expect(folder_image).to_be_visible()






