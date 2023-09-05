import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_credence2:
    @pytest.mark.skip
    def test_cred2(self):
        driver = webdriver.Firefox()
        driver.get('https://credence.in/')
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        L = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
        list1 = []
        for r in range(1, L+1):
            contact =driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
            # print(contact)
            list1.append(contact)

        if '+91 9091929355' in list1:
            assert True
        else:
            assert False
                # assert False #assertion error bcoz it's finding 1st contact & then in next step it's showing ass.error