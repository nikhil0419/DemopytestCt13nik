from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class Test_01:
    # @pytest.mark.xfail
    # @pytest.mark.skip
    def test_sum_01(self):
        a = 3
        b = 5
        sum = a + b
        print(sum)

        if sum == 8:
            print('Test case is Passed')
            assert True
        else:
            print('Test case is Failed')
            assert False

    # @pytest.mark.skip
    def test_mul_02(self):
        a = 3
        b = 5
        mul = a * b
        print(mul)

        if mul == 16:
            print('Test case is Passed')
            assert True
        else:
            print('Test case is Failed')
            assert False
    # @pytest.mark.skip
    def Sum_02(self):
        a = 3
        b = 5
        Sum = a + b
        print(Sum)

        if Sum == 16:
            print('Test case is Passed')
            assert True
        else:
            print('Test case is Failed')
            assert False

    # @pytest.mark.Sanity
    @pytest.mark.skip
    def test_Google_Logo_03(self):

        driver = webdriver.Firefox()
        driver.get('https://www.google.com/')
        logo = driver.find_element(By.XPATH, "//img[@alt='Google']").is_displayed()
        print(logo)


        if logo == True:
            driver.close()
            assert True
        else:
            driver.close()
            assert False
