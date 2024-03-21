from selenium.webdriver.common.by import By

from constants import numbers_equals


class Calculator:
    """Калькулятор"""

    def __init__(self, driver):
        self.driver = driver
        self.init_elements()

    def init_elements(self):
        """ Инициализировать элементы калькулятора """
        self.divide = self.driver.find_element(By.XPATH, '//div[@class="card-section"]//div[text()="÷"]')
        self.minus = self.driver.find_element(By.XPATH, '//div[@class="card-section"]//div[text()="−"]')
        self.numbers = self.driver.find_elements(By.XPATH, '//div[@class="card-section"]//div[@class="XRsWPe AOvabd"]')
        self.result = self.driver.find_element(By.XPATH, '//div[@class="card-section"]//span[@class="qv3Wpe"]')
        self.point = self.numbers[-1]
        self.equals = self.driver.find_element(
            By.XPATH, '//div[@class="card-section"]//div[@class="XRsWPe UUhRt" and text()="="]')
        self.clear = self.driver.find_element(
            By.XPATH, '//div[@class="card-section"]//div[@class="XRsWPe MEdqYd" and text()="AC"]')
        self.operations = {
            '/': self.divide
        }
    @staticmethod
    def is_negative(num):
        """ Проверить является ли число отрицательным """
        return str(num)[0] == '-'

    @staticmethod
    def is_float(num):
        """ Проверить является ли число дробным """
        return type(num) is float

    @staticmethod
    def get_float_parts(num):
        """ Получить разделенные части дробного числа """
        return str(num).split('.')

    def enter_num(self, num):
        """ Ввести число в поле калькулятора """
        n = num
        enter = lambda g: self.numbers[numbers_equals[g]].click()
        if self.is_negative(num):
            self.minus.click()
            n = abs(n)

        if self.is_float(n):
            first, second = self.get_float_parts(n)
            for x in [*first]:
                enter(int(x))
            self.point.click()
            for y in [*second]:
                enter(int(y))
        else:
            for x in [*str(n)]:
                enter(int(x))

    def execute_operations(self, first, second, operation):
        """ Выполнить операцию """
        self.enter_num(first)
        self.operations[operation].click()
        self.enter_num(second)
        self.equals.click()
        res = self.result.text
        self.clear.click()
        if first == 0 or second == 0:
            return res
        return float(res) if [*res].__contains__('.') else int(res)
