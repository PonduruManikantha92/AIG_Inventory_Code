import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.customLogger import LogGen
from page_Objects.Page_Object_HIS_Indent_Items import HIS_Indents
from page_Objects.Page_Objects_HIS_Login_Page import His_Login_Page


class TestHIS_Login_Page:
    logger = LogGen.loggen()
    results = []

    @pytest.fixture(scope= 'class')
    def test_his_login_page(self, pandas_excel, browser_setup):
        data = pandas_excel('LoginData')
        url = data['Inputs'].iloc[0]
        username = data['Inputs'].iloc[1]  # Manikantha
        password = data['Inputs'].iloc[2]
        print(url)
        driver = browser_setup
        login_page_object = His_Login_Page(driver)

        # Create a list for storing credentials and expected responses

        ###################### Logging and saving URL status ###############################
        self.logger.info("*********URL is invoked in the Browser*************")
        driver.get(url)

        if url:
            url_status = 'URL Loaded Successfully'
        else:
            url_status = 'URL Not Found or Empty'
        self.results.append(f'Expected Response: {url_status}')

        ###################### Logging and saving username status ###############################
        self.logger.info("*********Logging and saving username status*************")
        wait = WebDriverWait(driver, 30)
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, login_page_object.xpath_for_his_LoginPage_UserName)))
        login_page_object.Enter_His_LoginPage_UserName(username)

        if username:
            username_status = 'Username entered Successfully'
        else:
            username_status = 'Failed to enter the Username'
        self.results.append(f'Expected Response: {username_status}')
        ###################### Logging and saving password status ###############################
        self.logger.info("*********Logging and saving password status*************")
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, login_page_object.xpath_for_his_LoginPage_Password)))
        login_page_object.Enter_His_LoginPage_Password(password)
        print(password)

        if password:
            password_status = 'Password entered Successfully'
        else:
            password_status = 'Failed to enter the Password'
        self.results.append(f'Expected Response: {password_status}')

        ###################### Clicking submit button ###############################
        self.logger.info("*********Clicking submit button*************")
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, login_page_object.xpath_for_his_LoginPage_SubmitButton)))
        login_page_object.Click_His_LoginPage_Submit_button()

        ###################### Clicking Yes button in Pop up###############################
        self.logger.info("*************Click Yes Button in the POP UP*******************")
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, login_page_object.xpath_for_pop_up)))
        login_page_object.Click_yes_button_in_Pop_up()

        return browser_setup

