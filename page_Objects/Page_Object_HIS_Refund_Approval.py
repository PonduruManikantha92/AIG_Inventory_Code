import time

from pyodbc import drivers
from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class His_OP_Refund_Approval:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.xpath_for_options_in_home = "//ul[@class='mainList']//li//a"
        self.xpath_for_refund_approval = "//ul//li//a[normalize-space()='Approve Refunds']"
        self.xpath_for_search_button = "//a[@id='search_data']"
        self.xpath_for_item_table_approve_refunds = "(//div[@class='ApproveData'])[1]"
        self.xpath_for_Approve_button = "//table[@id='apid']//tbody/tr[1]//a[text()='Approve']"
        self.xpath_for_approve_pop_up = "//div[@id='_ApprovePopUp']//div[@id='popup400']"
        self.xpath_for_yes_button = "//footer[@class='popupHeader']//a[@id='_ApproveYes']"
        self.xpath_for_3_bars = "//img[@id='showmenuIcon']"
        self.xpath_for_home_button_after_clicking_3_bars = "//a[normalize-space()='HOME']"
        self.xpath_for_home_button = "//img[@id='showmenuIcon1']"

    def click_refund_approval_under_billing(self):
        try:
            options = self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, self.xpath_for_options_in_home)))

            for i in range(len(options)):
                try:
                    options = self.driver.find_elements(By.XPATH, self.xpath_for_options_in_home)  # Re-locate each time
                    option = options[i]
                    if option.text.strip() == 'Billing':
                        option.click()
                        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_refund_approval)))
                        approve_refund = self.driver.find_element(By.XPATH, self.xpath_for_refund_approval)
                        approve_refund.click()
                        break
                except StaleElementReferenceException:
                    print(f"Retrying option {i} due to stale element.")
                    continue
        except Exception as e:
            print(f"Exception in options_under_home_in_billing: {e}")

    def click_the_search_icon(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_search_button)))
        search_button = self.driver.find_element(By.XPATH, self.xpath_for_search_button)
        search_button.click()

    def click_the_approve_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_item_table_approve_refunds)))
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_Approve_button)))
        approve_button = self.driver.find_element(By.XPATH, self.xpath_for_Approve_button)
        approve_button.click()

    def click_yes_button_in_approve_pop_up(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_approve_pop_up)))
        yes_button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button)
        yes_button.click()

    def click_home_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_3_bars)))
        three_bars = self.driver.find_element(By.XPATH, self.xpath_for_3_bars)
        three_bars.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_home_button_after_clicking_3_bars)))
        home_button = self.driver.find_element(By.XPATH, self.xpath_for_home_button_after_clicking_3_bars)
        home_button.click()