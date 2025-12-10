import time

import pytest
import pandas as pd
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from page_Objects.Page_Object_HIS_Direct_Receipt import HIS_Direct_receipt
from page_Objects.Page_Object_HIS_Indent_Items import HIS_Indents
from testCases.test_login_page_HIS import TestHIS_Login_Page


class TestIndent(TestHIS_Login_Page):

    ##### """Fixture to read and return Indent_Items data once per class""" #########
    @pytest.fixture(scope='class')
    def indent_data(self, pandas_excel):
        # Load once, reuse
        data_one = pandas_excel('Indent_Items')
        data_two = pandas_excel('Indent_Issue')
        return {'items': data_one, 'issue': data_two}

    @pytest.mark.smoke
    def test_indent_indents(self, indent_data, test_his_login_page):
        driver = test_his_login_page
        option_name = indent_data['items']['option_name'].iloc[0]
        facility_name = indent_data['items']['facility_name'].iloc[0]
        department_name = indent_data['items']['Department_name'].iloc[0]

        indent_items = HIS_Indents(driver)

        self.logger.info("*********Select the Facility*************")
        indent_items.select_facility()
        self.logger.info("*******Click Inventory Option********")
        indent_items.click_inventory_option()
        self.logger.info("*******Select_options_from_inventory_dropdown*******")
        indent_items.select_options_from_inventory_dropdown()
        self.logger.info("*******Indent_options_select*******")
        indent_items.Indent_options_select(option_name)
        self.logger.info("*******select_facility_and_Department*******")
        indent_items.select_facility_and_Department(facility_name, department_name)
        self.logger.info("********search_and_click_indent_items********")
        for index, row in indent_data['items'].iterrows():
            # item_code = str(row['Tabs'])
            search_text = str(row['search_text'])
            value = str(row['value'])
            try:
                indent_items.search_and_click_indent_items(search_text)
                indent_items.enter_quantity(value, index + 1)
            except Exception as e:
                print(e)
                pass
        time.sleep(5)


        self.logger.info("******save_indent_items******")
        indent_items.save_indent_items()
        self.logger.info("*******click_home_button*******")
        indent_items.click_home_button()


    def test_indent_approval(self, indent_data, test_his_login_page):
        driver = test_his_login_page
        indent_approval = (HIS_Indents(driver))
        option_name = indent_data['items']['option_name'].iloc[1]

        self.logger.info("*********Select the Facility*************")
        indent_approval.select_facility()
        self.logger.info("*******Click Inventory Option********")
        indent_approval.click_inventory_option()
        self.logger.info("*******Select_options_from_inventory_dropdown*******")
        indent_approval.select_options_from_inventory_dropdown()
        self.logger.info("***********Indent_options_select************")
        indent_approval.Indent_options_select_indent_approval(option_name)
        self.logger.info("********click_indent_approval********")
        indent_approval.indent_approval()
        self.logger.info("*******click_home_button*******")
        indent_approval.click_home_button()

    # @pytest.mark.smoke
    def test_indent_issue(self, indent_data, test_his_login_page):
        driver = test_his_login_page
        indent_issue = HIS_Indents(driver)
        option_name = indent_data['items']['option_name'].iloc[2]

        self.logger.info("*********Select the Facility*************")
        indent_issue.select_facility()
        self.logger.info("*******Click Inventory Option********")
        indent_issue.click_inventory_option()
        self.logger.info("*******Select_options_from_inventory_dropdown*******")
        indent_issue.select_options_from_inventory_dropdown_indent_issue()
        time.sleep(5)
        self.logger.info("***********Indent_options_select************")
        indent_issue.Indent_options_select_indent_issue(option_name)
        self.logger.info("*******indent_issue*******")
        indent_issue.indent_issue()
        xpath_for_table3_indent_issue = "//table[@id='tbl_IssuedItems']//tbody"
        rows = driver.find_elements(By.XPATH, xpath_for_table3_indent_issue)

        for index, row in indent_data['issue'].iterrows():
            item_name = str(row['Item_name']).strip()
            batch_number = str(row['Batch']).strip()
            quantity_to_be_filled = str(row['Quantity']).strip()

            xpath_for_indiv_row = f"""
                //table[@id='tbl_IssuedItems']//tbody/tr[
                    td[normalize-space(text())='{item_name}']
                    and 
                    td[normalize-space(text())='{batch_number}']
                ]//td[@ctype='dueqty']//input
            """

            try:
                qty_input = driver.find_element(By.XPATH, xpath_for_indiv_row)
                qty_input.clear()
                qty_input.send_keys(quantity_to_be_filled)
                qty_input.send_keys(Keys.TAB)
                print(f"✅ Filled {quantity_to_be_filled} for {item_name}, batch {batch_number}")
            except Exception as e:
                print(f"❌ Could not find row for {item_name}, batch {batch_number}: {e}")

        time.sleep(60)
        xpath_for_save_button = "//i[@class='fa fa-save']/parent::a"
        save_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_for_save_button)))
        save_button.click()
        time.sleep(2)

        xpath_for_save_this_record_pop = '//div[@id="popup_Conforim"]//div[@id="popup280"]'
        yes_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "btnYes")))
        yes_button.click()
        time.sleep(2)

        self.logger.info("*******click_home_button*******")
        indent_issue.click_home_button()
        time.sleep(20)

    # @pytest.mark.smoke
    def test_indent_item_receipt(self, indent_data, test_his_login_page):
        driver = test_his_login_page
        indent_item_receipt = (HIS_Indents(driver))
        self.logger.info("*********Select the Facility*************")
        indent_item_receipt.select_facility()
        self.logger.info("*******indent_item_receipt*******")
        indent_item_receipt.indent_item_receipt()
        self.logger.info("*******click_home_button*******")
        indent_item_receipt.click_home_button()
        time.sleep(20)

    # @pytest.mark.smoke
    def test_direct_receipt(self, indent_data, test_his_login_page):
        driver = test_his_login_page
        direct_receipt_object = (HIS_Direct_receipt(driver))
        self.logger.info("*********Select the Facility*************")
        direct_receipt_object.select_facility()
        self.logger.info("*******indent_item_receipt*******")
        direct_receipt_object.click_inventory_option()
        self.logger.info("*******click_home_button*******")
        direct_receipt_object.select_options_from_inventory_dropdown()
        time.sleep(20)


