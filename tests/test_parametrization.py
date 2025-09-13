import pytest

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
# В данном случае в качестве данных используются спиок с кортежами внутри
def test_several_numbers(number: int, expected: int):
    # Возводим число  number в квадрат и проверяем, что оно равно ожидаемому
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"]) # Параметризируем по операционной системе
@pytest.mark.parametrize("browser", ["chromium", "webkit", "fierfox"]) # Парамитризируем по браузеру
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0 # Проверка указана для примера

