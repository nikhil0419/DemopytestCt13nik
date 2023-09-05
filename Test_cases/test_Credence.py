import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_credence:
    @pytest.mark.skip
    def test_cred(self):
        driver = webdriver.Firefox()
        driver.get('https://credence.in/')
        offer = driver.find_element(By.XPATH, "//span[@class='text-white b label']").text
        print(offer)
        print(driver.title)


