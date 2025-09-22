import time

from pyodbc import drivers
from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class His_OP_Billing:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.xpath_for_options_in_home = "//ul[@class='mainList']//li//a"
        self.xpath_for_billing = "(//li//a[normalize-space()='Billing'])[1]"
        self.xpath_for_billing_under_billing = "(//li//a[normalize-space()='Billing'])[2]"
        self.xpath_for_uhid_field_in_billing_page = "//form//span//input[@id='uHid']"
        self.xpath_for_search_doctor_name = "//input[@placeholder='Search Doctor Name']"
        self.xpath_for_op_registration_update_pop_up = "//div[@class='modal-block-new top27']"
        self.xpath_for_op_registration_update_pop_up_close_button = "//div[@class='modal-block-new top27']//div//span//a[@id='btnCloseUpdatePopup']"
        self.xpath_for_company_details_pop_up = "//div[@class='modal-block-new modal-block-new2 w-950']"
        self.xpath_for_company_details_cancel_button = "//div//section//form//div//span//a[@id='cancelinsurance']"
        self.xpath_for_scheme_details_pop_up = "//div[@id='divscheme']"
        self.xpath_for_scheme_details_close_button = "//section//form//div//span//a[@id='schemeclose']"
        self.xpath_for_Referred_by = "//span//input[@id='autocomplete_refby']"
        self.xpath_for_referred_by_pop = "//div[@class='modal-block-new ']"
        self.xpath_for_aig_doc_referred = "//tr//td[text()='AIG DOCTOR  ']"
        self.xpath_for_add_to_bill = "//span//a[@id='add_bill_visit']"
        self.xpath_for_policy_info = "//div[@id='policyInfo']//div[@id='popup400']"
        self.xpath_for_policy_info_yes = "//div[@id='policyInfo']//button[@id='btnyespolicy']"
        self.xpath_for_deposit_pop = "(//div[@id='popup400'])[5]"
        self.xpath_for_deposit_pop_close_button = "//div[@id='modalamount_varification']//div[@id='popup400']//header//span[@class='modal_close']"
        self.xpath_for_discount_check_box = "//span[@id='discountChkbxSpanId']//input[@type='checkbox']"
        self.xpath_for_discount_pop_up = "//div[@id='discount_popup']//div[@class='modal-block-new']"
        self.xpath_for_yes_button_in_discount_pop_up = "(//div[@class='modal-block-new']//footer[@class='popupHeader']//a[text()='Yes'])[4]"
        self.xpath_for_process_discounts = "//div[@id='modal_discounts']//div[@id='popup1000']"
        self.xpath_for_Discount_on_dropdown = "//select[@class='DiscountOn']"
        self.xpath_for_Discount_head_dropdown = "//td[@id='discount_head1']//select[@id='discounthead1']"
        self.xpath_for_Discount_reason = "//select[@id='discountreason1']"
        self.xpath_for_discount_percentage = "//input[@id='discount_percent1']"
        self.xpath_for_calculate_discount = "//a[@id='CalculateDiscount']"
        self.xpath_for_authorised_by = "//select[@id='ddlAuthorised_dis']"
        self.xpath_for_verify = "(//a[@title='Verify'])[2]"
        self.xpath_for_billing = "//div[@class='user_sp_menu']//a[@title='Billing']"
        self.xpath_for_generate_bill_pop = "(//div[@id='popup235'])[2]"
        self.xpath_for_yes_button_in_generate_bill_pop_up = "(//div[@id='popup235'])[2]//a[@id='btnyesbal2']"
        self.xpath_for_process_payment = "//div[@id='modal_process_payment']//div[@id='popup1000']"
        self.xpath_for_save_button = "(//div[@class='popup-icon-top']//span//a[@title='Verify'])[1]"
        self.xpath_for_print_the_bill_pop_up = "//div[@id='modal_report']//div[@id='popup235']"
        self.xpath_for_no_button_in_print_the_bill_pop_up_footer = "//footer[@class='popupHeader']//a[@id='btnnorep']"
        self.xpath_for_refresh_button = "//a[@id='Clear']"
        self.xpath_for_3_bars = "//img[@id='showmenuIcon']"
        self.xpath_for_home_button_after_clicking_3_bars = "//a[normalize-space()='HOME']"
        self.xpath_for_home_button = "//img[@id='showmenuIcon1']"
        self.xpath_for_Amount_in_process_payment = "//td//input[@ctype='amount']"
        self.xpath_for_Authorised_by = "//select[@id='ddlAuthorised']"
        self.xpath_for_remarks = "//span//input[@id='authorisedremarks']"
        self.xpath_for_verify = "//button[@id='authorised_verify']"




    def click_billing_option_under_home(self):
        try:
            options = self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, self.xpath_for_options_in_home)))

            for i in range(len(options)):
                try:
                    options = self.driver.find_elements(By.XPATH, self.xpath_for_options_in_home)  # Re-locate each time
                    option = options[i]
                    if option.text.strip() == 'Billing':
                        option.click()
                        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_billing_under_billing)))
                        billing_option_under_billing = self.driver.find_element(By.XPATH,self.xpath_for_billing_under_billing)
                        billing_option_under_billing.click()
                        break
                except StaleElementReferenceException:
                    print(f"Retrying option {i} due to stale element.")
                    continue
        except Exception as e:
            print(f"Exception in options_under_home_in_billing: {e}")

    def enter_the_uhid(self, due_settlement_uhid):

        uhid_locator = (By.XPATH, self.xpath_for_uhid_field_in_billing_page)
        self.wait.until(expected_conditions.presence_of_element_located(uhid_locator))
        try:
            enter_uhid = self.driver.find_element(*uhid_locator)
            enter_uhid.clear()  # Optional: clear the field first
            enter_uhid.send_keys(due_settlement_uhid, Keys.ENTER)
        except StaleElementReferenceException:
            # Re-locate the element if it's stale
            enter_uhid = self.driver.find_element(*uhid_locator)
            enter_uhid.send_keys(due_settlement_uhid, Keys.ENTER)
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_op_registration_update_pop_up)))
            op_registration_update_pop_up_close_button = self.driver.find_element(By.XPATH, self.xpath_for_op_registration_update_pop_up_close_button)
            op_registration_update_pop_up_close_button.click()
        except TimeoutException as e:
            pass
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_company_details_pop_up)))
            company_details_close_button = self.driver.find_element(By.XPATH, self.xpath_for_company_details_cancel_button)
            company_details_close_button.click()
        except TimeoutException as e:
            pass
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_scheme_details_pop_up)))
            scheme_pop_up = self.driver.find_element(By.XPATH, self.xpath_for_scheme_details_close_button)
            scheme_pop_up.click()
        except TimeoutException as e:
            pass

    def search_for_doctor_name(self, Doctor_name, ):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_search_doctor_name)))
        search_doctor_name = self.driver.find_element(By.XPATH, self.xpath_for_search_doctor_name)
        search_doctor_name.send_keys(Doctor_name)
        xpath_for_search_doctor_in_doctors_table = "//li[contains(text(), 'ANNE UDAY KIRAN  ')]"
        doc_name = self.driver.find_element(By.XPATH, xpath_for_search_doctor_in_doctors_table)
        doc_name.click()

    def refered_by(self, refer):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_Referred_by)))
        refered_by = self.driver.find_element(By.XPATH, self.xpath_for_Referred_by)
        refered_by.send_keys(refer, Keys.ENTER)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_referred_by_pop)))
        refered_doc = self.driver.find_element(By.XPATH, self.xpath_for_aig_doc_referred)
        refered_doc.click()

    def click_add_to_bill(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_add_to_bill)))
        add_to_bill_button = self.driver.find_element(By.XPATH, self.xpath_for_add_to_bill)
        add_to_bill_button.click()
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_policy_info)))
            yes_button = self.driver.find_element(By.XPATH, self.xpath_for_policy_info_yes)
            yes_button.click()
        except TimeoutException as e:
            pass

    def close_the_deposit_pop_up(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_deposit_pop)))
            close_button = self.driver.find_element(By.XPATH, self.xpath_for_deposit_pop_close_button)
            close_button.click()
        except TimeoutException as e:
            pass

    def click_yes_button_in_discount_pop(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_discount_check_box)))
        click_check_box= self.driver.find_element(By.XPATH, self.xpath_for_discount_check_box)
        click_check_box.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_yes_button_in_discount_pop_up)))
        click_yes_button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_discount_pop_up)
        click_yes_button.click()

    def process_discount(self, Discount_on_option, Discount_head, Discount_reason, Discount_percentage, Authorized_By):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_process_discounts)))
        discount_on = self.driver.find_element(By.XPATH, self.xpath_for_Discount_on_dropdown)
        discount_on_dropdown = Select(discount_on)
        for option in discount_on_dropdown.options:
            if option.text == Discount_on_option:
                option.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_Discount_head_dropdown)))
        discount_head = self.driver.find_element(By.XPATH, self.xpath_for_Discount_head_dropdown)
        discount_head_dropdown = Select(discount_head)
        for option in discount_head_dropdown.options:
            if option.text == Discount_head:
                option.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_Discount_reason)))
        discount_reason = self.driver.find_element(By.XPATH, self.xpath_for_Discount_reason)
        discount_reason_dropdown = Select(discount_reason)
        for option in discount_reason_dropdown.options:
            if option.text == Discount_reason:
                option.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_discount_percentage)))
        percentage_of_discount = self.driver.find_element(By.XPATH, self.xpath_for_discount_percentage)
        percentage_of_discount.clear()
        percentage_of_discount.send_keys(Discount_percentage, Keys.ENTER)

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_calculate_discount)))
        calculate_discount = self.driver.find_element(By.XPATH, self.xpath_for_calculate_discount)
        calculate_discount.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_authorised_by)))
        authorised_by = self.driver.find_element(By.XPATH, self.xpath_for_authorised_by)
        authorised_by_dropdown = Select(authorised_by)
        for option in authorised_by_dropdown.options:
            if option.text == Authorized_By:
                option.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_verify)))
        verify_button = self.driver.find_element(By.XPATH,self.xpath_for_verify)
        verify_button.click()

    def click_the_billing_option(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_billing)))
        billing_option  = self.driver.find_element(By.XPATH, self.xpath_for_billing)
        billing_option.click()

    def generate_bill_pop_up(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_generate_bill_pop)))
        yes_button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_generate_bill_pop_up)
        yes_button.click()

    def click_save_button_in_process_payment(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_process_payment)))
        save_button = self.driver.find_element(By.XPATH, self.xpath_for_save_button)
        self.driver.execute_script("argument[0].click();", save_button)

    def print_the_bill(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_print_the_bill_pop_up)))
        no_button = self.driver.find_element(By.XPATH, self.xpath_for_no_button_in_print_the_bill_pop_up_footer)
        no_button.click()
        time.sleep(5)

    def click_refresh_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_refresh_button)))
        refresh_button = self.driver.find_element(By.XPATH, self.xpath_for_refresh_button)
        refresh_button.click()

    def click_home_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_3_bars)))
        three_bars = self.driver.find_element(By.XPATH, self.xpath_for_3_bars)
        three_bars.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_home_button_after_clicking_3_bars)))
        home_button = self.driver.find_element(By.XPATH, self.xpath_for_home_button_after_clicking_3_bars)
        home_button.click()

    ############# Process Payment for Due Settlement #######################
    def amount_field_in_process_payment_Billing(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_process_payment)))
        amount_field = self.driver.find_element(By.XPATH, self.xpath_for_Amount_in_process_payment)
        amount_field.clear()
        amount_field.send_keys("100")

    def select_authorized_by(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_Authorised_by)))
        Authorised_by = self.driver.find_element(By.XPATH, self.xpath_for_Authorised_by)
        authorised_by = Select(Authorised_by)
        for option in authorised_by.options:
            if option.text.strip() == 'CAPRI JALOTA':
               option.click()

    def enter_remarks(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_remarks)))
        remarks = self.driver.find_element(By.XPATH, self.xpath_for_remarks)
        remarks.send_keys('jksbdkfs')

    def click_the_verify_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_verify)))
        verify_button = self.driver.find_element(By.XPATH, self.xpath_for_verify)
        verify_button.click()








