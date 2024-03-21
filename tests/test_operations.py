import pytest
from selenium import webdriver
from constants import BASE_URL, Operation
from helper import open_page, get_error_message
from pages.Calculator import Calculator


class TestOperations:
    """Тест основных операций калькулятора"""

    def setup_class(self):
        self.driver = webdriver.Chrome()
        open_page(self.driver, BASE_URL)
        self.calculator = Calculator(self.driver)

    @pytest.mark.parametrize(
        'first, second, operation, test_result',
        [pytest.param(-5, 2, Operation.divide.value, -2.5, id='positive_negative_divide'),
         pytest.param(-6, -3, Operation.divide.value, 2, id='negative_negative_divide'),
         pytest.param(8, 2.2, Operation.divide.value, 3.63636363636, id='int_float_divide'),
         pytest.param(11, 0, Operation.divide.value, 'Infinity', id='int_zero_divide'),
         pytest.param(5.5, 3.2, Operation.divide.value, 1.71875, id='float_float_divide'),
         pytest.param(0, 7, Operation.divide.value, 0, id='zero_int_divide')]
    )
    def test_divide(self, first, second, operation, test_result):
        res = self.calculator.execute_operations(first, second, Operation.divide.value)
        assert res == test_result, get_error_message(
            'Результат выполнения операции не соответствует тестовому значению', res, test_result)
