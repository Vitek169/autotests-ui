import pytest
from playwright.sync_api import Page, expect

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state

    # переходим по ссылке

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    # Проверяем наличие элементов текста
    courses_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_text).to_have_text('Courses')

    result_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_text).to_have_text('There is no results')

    result_from_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(result_from_text).to_have_text('Results from the load test pipeline will be displayed here')

    # Проверка на видимость иконки папки
    folder_image = page.get_by_test_id('courses-list-empty-view-icon')
    expect(folder_image).to_be_visible()


