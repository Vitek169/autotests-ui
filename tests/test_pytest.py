import pytest


def test_first_try():
    print('Hello, World!')

def test_greeting():
    greeting = 'Hello, World!'
    assert greeting == 'Hi, World!'

def test_equal():
    assert 1 == 1  # Проверка на равенство

def test_no_equal():
    assert 1 != 2, "1 не равно 2" # Проверка на неравенство

def test_in_list():
    assert 3 in [1, 2, 3, 4]  # Проверка на вхождение

def test_boolean():
    is_authenticated =  True
    assert  is_authenticated  # Проверка булевого значения

def test_zero_division():
    with pytest.raises(ZeroDivisionError):  #  Проверка исключения
        1/0

def test_sum():
    assert  1 + 1 == 3, "Сумма 1 + 1 равна 2"  # Проверка равенства с указанием ошибки

def test_lists():
    assert [1, 2, 3] == [1, 2, 4]  # Сравнение списков


def test_assert_positive_case():  # Новый тест, которые проверяет положительный кейс
    assert (2 + 2) == 4  # Ожидается, что тест пройдет


def test_assert_negative_case():  # Новый тест, которые проверяет негативный кейс
    assert (2 + 2) == 5  # Тут должна быть ошибка