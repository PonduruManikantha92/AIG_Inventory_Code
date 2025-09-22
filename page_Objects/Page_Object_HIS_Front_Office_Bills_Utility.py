import time

from pyodbc import drivers
from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class His_OP_Bills_Utility:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.xpath_for_search_field = "//input[@type='search']"
        self.xpath_for_options_in_home = "//ul[@class='mainList']//li//a"
        self.xpath_for_billing = "(//li//a[normalize-space()='Billing'])[1]"
        self.xpath_for_bills_utility_under_billing = "//li//a[normalize-space(text())='Bills Utility']"
        self.xpath_for_uhid_field = "//span//input[@id='uHid']"
        self.xpath_for_3_bars = "//img[@id='showmenuIcon']"
        self.xpath_for_home_button_after_clicking_3_bars = "//a[normalize-space()='HOME']"
        self.xpath_for_home_button = "//img[@id='showmenuIcon1']"
        self.xpath_for_select_refund = "//a[@id='refund']"
        self.xpath_for_Refund_pop_up = "//div[@id='modal_refund']//div[@class='modal-block-new']"
        self.xpath_for_check_all_option = "(//div[@class='modal-block-new']//section//form//input[@type='checkbox'])[1]"
        self.xpath_for_refund_approval_reason = "//select[@id='ReasonForRefund']"
        self.xpath_for_remarks = "//input[@name='remarks']"
        self.xpath_for_send_approval_request = "//div//button[@id='btnsendReqApproval']"

        ###### Refund the Confirmed Approval Request ###########################
        self.xpath_for_confirm_refund_pop_up = "//div[@id='popup300']"
        self.xpath_for_yes_button_in_confirm_refund_pop_up = "//a[@id='btnyesupdateapproval']"
        self.xpath_for_mode_of_payment = "//select[@id='paymentMode']"
        self.xpath_for_save_button = "//div[@id='userfunction']//a[@title='Save']"
        self.xpath_for_refund_by_cash_pop_up = "(//div[@class='modal-block-new 280 top40'])[4]"
        # self.xpath_for_yes_button_in_refund_by_cash =

        ###### Due Settlement ###########################
        self. xpath_for_options_under_home_Billing = "//li[@id='FOBillingMenu']"
        self.xpath_for_options_under_Billing_option = "//ul[@class='collapse']//li"
        self.xpath_for_due_settlement_option = "//a[@title='Dues Settlement']"
        self.xpath_for_plus_button = "//a[@id='addpaymentmode']//i[@class='fa fa-plus']"
        self.xpath_for_make_receipt_button = "//a[@title='Make Receipt']"
        self.xpath_for_save_pop_up = "//div[@id='duepayment']//div[@id='popup350']"
        self.xpath_for_yes_button_in_save_pop_up = "//a[@id='duepaymentyes']"


    def click_bills_utility_under_home(self):
        try:
            # Wait for the Billing menu to appear and click
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_search_field)))
            search_field = self.driver.find_element(By.XPATH, self.xpath_for_search_field)
            search_field.send_keys("Bills Utility")

            self.wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, self.xpath_for_bills_utility_under_billing)))
            Bills_Utility_option = self.driver.find_element(By.XPATH, self.xpath_for_bills_utility_under_billing)
            Bills_Utility_option.click()
        except Exception as e:
            print(f"Error in clicking Bills Utility: {e}")

    def enter_the_uhid_in_bills_utility(self, due_settlement_uhid):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_uhid_field)))
        uhid_field = self.driver.find_element(By.XPATH, self.xpath_for_uhid_field)
        uhid_field.clear()
        uhid_field.send_keys(due_settlement_uhid, Keys.ENTER)

    def click_the_select_refund_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_select_refund)))
        refund_button = self.driver.find_element(By.XPATH, self.xpath_for_select_refund)
        refund_button.click()

    def select_all_options_in_pop_up(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_Refund_pop_up)))
        check_all_option = self.driver.find_element(By.XPATH, self.xpath_for_check_all_option)
        check_all_option.click()

    def select_reason_for_approval_request_and_remarks(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_refund_approval_reason)))
        check_all_options = self.driver.find_element(By.XPATH, self.xpath_for_refund_approval_reason)
        check_option = Select(check_all_options)
        for option in check_option.options:
            if option.text.strip() == "Incorrect Payment Mode selected":
                option.click()
                break
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_remarks)))
        remarks = self.driver.find_element(By.XPATH, self.xpath_for_remarks)
        remarks.send_keys("sdvfsd")

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_send_approval_request)))
        send_approval_request = self.driver.find_element(By.XPATH, self.xpath_for_send_approval_request)
        send_approval_request.click()

    def click_home_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_3_bars)))
        three_bars = self.driver.find_element(By.XPATH, self.xpath_for_3_bars)
        three_bars.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_home_button_after_clicking_3_bars)))
        home_button = self.driver.find_element(By.XPATH, self.xpath_for_home_button_after_clicking_3_bars)
        home_button.click()

    ############# Refund the Approved Refund ##############################
    def click_yes_button_in_confirm_refund_pop_up(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_confirm_refund_pop_up)))
        yes_button_in_confirm_refund = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_confirm_refund_pop_up)
        yes_button_in_confirm_refund.click()

    def select_the_mode_of_payment(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_mode_of_payment)))
        mode_of_pay = self.driver.find_element(By.XPATH, self.xpath_for_mode_of_payment)
        m_o_p = Select(mode_of_pay)
        for option in m_o_p.options:
            if option.text.strip() == 'Cash':
                option.click()

    def click_save_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_save_button)))
        save = self.driver.find_element(By.XPATH, self.xpath_for_save_button)
        save.click()

    def click_yes_button_in_refund_by_cash_pop_up(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_refund_by_cash_pop_up)))
        yes_button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_refund_by_cash)
        yes_button.click()


    ############# Due Settlement of OP Bill ##############################
    def click_due_settlement(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_due_settlement_option)))
        settlement_option = self.driver.find_element(By.XPATH, self.xpath_for_due_settlement_option)
        settlement_option.click()

    def click_plus_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_plus_button)))
        plus_button = self.driver.find_element(By.XPATH, self.xpath_for_plus_button)
        plus_button.click()

    def click_make_receipt_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_make_receipt_button)))
        receipt_button = self.driver.find_element(By.XPATH, self.xpath_for_make_receipt_button)
        receipt_button.click()

    def click_yes_in_save_pop_up(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_save_pop_up)))
        yes_button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_save_pop_up)
        yes_button.click()



