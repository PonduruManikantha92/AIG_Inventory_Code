import time

from pyodbc import drivers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class HIS_Adjustments:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.xpath_for_facility_dropdown = "//select[@id='Facility']"
        self.xpath_for_facility_option = "//option[text()='AIG Hospitals, Gachibowli']"
        self.xpath_for_inventory_option = "//li[.//div/span[normalize-space(text())='Inventory']]"
        self.xpath_for_inventory_pop_up = "//div[@id='popup280']"
        self.xpath_for_inventory_option_dropdown = "//select[@id='Department']"
        self.xpath_for_yes_button_in_inventory_pop_up = "//a[@id='btn_yes_desh']"

        self.xpath_for_expired_item_pop_up = "//div[@id='checkalert']//div[@id='popup280']"
        self.xpath_for_yes_button = "//div[@id='checkalert']//div[@id='popup280']//footer//a[@id='btnYes1']"

        self.xpath_for_Item_store_mapping_option = "//body/nav[@id='menu']/ul[@class='mainList']/li[6]"
        self.xpath_for_item_store_adjustments_option = "//ul[@id='collapseMulti24']"
        self.xpath_for_adjustment_type_dropdown = "//select[@id='ddlAdjust']"
        self.xpath_for_tick_option = "//a//i[@id='fafatick']"
        self.xpath_for_search_option = "(//input[@type='text'])[6]"
        self.xpath_for_batches_suction_catherer = "//table[@id='tbldrugdtaillist']"

        self.xpath_for_Item_desc_table_rows = "//table[@id='tbldrugitemdesc']//tbody//tr"
        self.xpath_quantity = "//input[@ctype='qty']"
        self.xpath_for_reason = "//select[@class='required']"
        self.xpath_for_save_button = "//div//a//i[@class='fa fa-save']"

    ################## Adjustments #####################
    def select_facility(self):
        facility_dropdown = self.driver.find_element(By.XPATH, self.xpath_for_facility_dropdown)
        facility_option = self.driver.find_element(By.XPATH, self.xpath_for_facility_option)
        self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_facility_dropdown)))
        facility_dropdown.click()
        self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_facility_option)))
        facility_option.click()

    def click_inventory_option(self):
        self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_inventory_option)))
        inventory = self.driver.find_element(By.XPATH, self.xpath_for_inventory_option)
        inventory.click()

    def select_options_from_inventory_dropdown(self):
        self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_inventory_option_dropdown)))
        inventory_dropdown_option = self.driver.find_element(By.XPATH, self.xpath_for_inventory_option_dropdown)
        inventory_ops = Select(inventory_dropdown_option)
        for i in inventory_ops.options:
            if i.text.strip() == 'A-9-NS 7':
                i.click()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.xpath_for_yes_button_in_inventory_pop_up)))
        yes_Button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_inventory_pop_up)
        yes_Button.click()

    def item_adjustment(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_Item_store_mapping_option)))
        item_map_store_option = self.driver.find_element(By.XPATH, self.xpath_for_Item_store_mapping_option)
        item_map_store_option.click()
        time.sleep(5)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_item_store_adjustments_option)))

        options = self.driver.find_elements(By.XPATH, self.xpath_for_item_store_adjustments_option)
        xpath_for_adjustment_option_in_dropdown = "//a[text()='Adjustments']"
        for option in options:
            adjustment_option = option.find_element( By.XPATH, xpath_for_adjustment_option_in_dropdown)
            if adjustment_option.is_displayed():
                self.driver.execute_script("arguments[0].click();", adjustment_option)
                break
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_adjustment_type_dropdown)))
        adjustment_type = self.driver.find_element(By.XPATH, self.xpath_for_adjustment_type_dropdown)
        adjustment_type_dropdown = Select(adjustment_type)
        for option in adjustment_type_dropdown.options:
            if option.text.strip() == "Adjustment Issue":
                option.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_tick_option)))
        tick_option = self.driver.find_element(By.XPATH, self.xpath_for_tick_option)
        tick_option.click()

    def item_adj_table_one(self, adj_item_name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_search_option)))
        search_option = self.driver.find_element(By.XPATH, self.xpath_for_search_option)
        search_option.send_keys(adj_item_name)
        xpath_for_option_item = f"//tr//td[normalize-space(text())='{adj_item_name.strip()}']"
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_option_item)))
        option = self.driver.find_element(By.XPATH, xpath_for_option_item)
        self.driver.execute_script("arguments[0].click();", option)

        xpath_for_batches_suction_catherer = "//table[@id='tbldrugdtaillist']"
        table_2_elements = self.driver.find_elements(By.XPATH, xpath_for_batches_suction_catherer)
        xpath_of_numbers_comp = "//table[@id='tbldrugdtaillist']//td[text()='NOS']"
        # try:
        for option in table_2_elements:
            numbers_comp = option.find_elements(By.XPATH, xpath_of_numbers_comp)
            for element in numbers_comp:
                if element.is_displayed():
                    self.driver.execute_script("arguments[0].click();", element)
                    pop_up = self.driver.find_element(By.XPATH, self.xpath_for_expired_item_pop_up)
                    if pop_up.is_displayed():
                        button_yes = self.driver.find_element(By.XPATH, self.xpath_for_yes_button)
                        self.driver.execute_script("arguments[0].click();", button_yes)
                    else:
                        pass
        time.sleep(8)
        search_option.clear()

    def item_adj_table_two(self):
        # Wait for table to be visible
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_Item_desc_table_rows)))

        rows = self.driver.find_elements(By.XPATH, self.xpath_for_Item_desc_table_rows)

        qoh_values = []
        for row in rows:
            # Relative XPath to QOH cell inside this row
            qoh_element = row.find_element(By.XPATH, ".//td[@ctype='quantity']")
            if qoh_element.is_displayed():
                qoh_value = qoh_element.text.strip()
                qoh_values.append(qoh_value)

                # Find Qty input field ONLY in current row
                qty_input = row.find_element(By.XPATH, ".//input[@ctype='qty']")
                # for value in qoh_values:
                if qty_input.is_displayed():
                    qty_input.clear()
                    qty_input.send_keys(qoh_value)

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_reason)))
        reason = self.driver.find_element(By.XPATH, self.xpath_for_reason)
        reason_option = Select(reason)
        for option in reason_option.options:
            if option.text.strip() == 'Other':
                option.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_save_button)))
        save_button = self.driver.find_element(By.XPATH, self.xpath_for_save_button)
        save_button.click()










