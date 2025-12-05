import re
import time
from datetime import datetime

import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



class Receipt_Direct:
    def __init__(self):
        self.driver = None

    def read_an_excel_file(self):
        file_path = "C:\\Users\\10013655\\PycharmProjects\\Inventory\\AIG_Inventory_Code\\Excel_Test_Data\\Inventory_Test_Data.xlsx"
        data = pd.read_excel(file_path, sheet_name='LoginPage')
        data_one = pd.read_excel(file_path, sheet_name='Inventory')
        data_two = pd.read_excel(file_path, sheet_name='Direct_Receipt_Medicines')

        url = data['Input'].iloc[0]
        username = data['Input'].iloc[1]
        password = data['Input'].iloc[2]
        facility_option = data_one['Inputs'].iloc[0]
        main_menu_option = data_one['Inputs'].iloc[1]
        drop_down_option = data_one['Inputs'].iloc[2]
        footer_option = data_one['Inputs'].iloc[3]
        search_field_option = data_one['Inputs'].iloc[4]
        # search_field_option_indent = data_three['Inputs'].iloc[0]

        items_from_direct_receipt_sheet = []
        for index, row in data_two.iterrows():
            items_from_direct_receipt_sheet.append({
                "medicine": row["Medicines_List"],
                "quantity": row["Quantity"],
                "batch": row["Batch_numbers"],
                "date": row["Expiry_Date"],
            })

        return url, username, password, facility_option, main_menu_option, drop_down_option, footer_option, search_field_option, items_from_direct_receipt_sheet

    def login_page(self, url, username, password, facility_option):
        self.driver = webdriver.Chrome()

        ############### Credentials ###############################
        self.url = url
        self.username = username
        self.password = password
        self.facility = facility_option
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        ############### login page xpaths ###############################
        xpath_for_his_LoginPage_UserName = "//input[@id='txtLoginName']"
        xpath_for_his_LoginPage_Password = "//input[@id='txtPassword']"
        xpath_for_his_LoginPage_SubmitButton = "//input[@value='Login']"
        xpath_for_pop_up = "(//div[@id='popup650'])[2]"
        xpath_for_yes_button_in_active_session_pop_up = "//a[@id='btnYesAlreadyLogedinPopup']"
        xpath_for_facility_option = "//select[@id='Facility']"

        ############### Initializing wait ###############################
        wait = WebDriverWait(self.driver, 30)
        ############### Waiting and entering the username ###############################
        user_name = self.driver.find_element(By.XPATH, xpath_for_his_LoginPage_UserName)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_his_LoginPage_UserName)))
        user_name.send_keys(self.username)

        ############### Waiting and entering the password ###############################
        pass_word = self.driver.find_element(By.XPATH, xpath_for_his_LoginPage_Password)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_his_LoginPage_Password)))
        pass_word.send_keys(self.password)

        ############### Waiting and clicking the submit button ###############################
        submit_button = self.driver.find_element(By.XPATH, xpath_for_his_LoginPage_SubmitButton)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_his_LoginPage_SubmitButton)))
        submit_button.click()

        ############### Waiting and clicking the Yes button in Pop up ###############################
        yes_button = self.driver.find_element(By.XPATH, xpath_for_yes_button_in_active_session_pop_up)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_pop_up)))
        yes_button.click()

        ############### Waiting and clicking the facility dropdown ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_facility_option)))
        f_option = self.driver.find_element(By.XPATH, xpath_for_facility_option)
        facility = Select(f_option)
        for option in facility.options:
            if option.text.strip() == self.facility:
                option.click()

        time.sleep(5)

    def direct_update(self, main_menu_option, drop_down_option, footer_option, search_field_option, items_from_direct_receipt_sheet):

        self.main_menu_option = main_menu_option
        self.drop_down_option = drop_down_option
        self.footer_option = footer_option
        self.search_field_option = search_field_option


        xpath_for_all_the_options_in_His = "//section//ul[@id='da-thumbs']//li"
        xpath_for_inventory_dropdown = "//div[@id='popup280']"
        xpath_for_dropdown_values_of_inventory_pop_up = "//select[@id='Department']"
        xpath_for_footer_in_inventory_pop_up = "//div[@id='popup280']//footer//a"
        xpath_for_search_field_in_inventory = "//input[@id='nav-search']"
        xpath_for_Indent_Items = f"//a[text()='{self.search_field_option}']"
        xpath_for_tabs = "//div//ul[@class='nav nav-tabs']//li"
        xpath_for_remarks = "//textarea[@id='txtnewremark']"
        xpath_for_calculate = "//a[@id='btncalculate']"
        xpath_for_total = "//input[@id='txttotal']"
        xpath_for_save = "//div//a[@id='btnsave']"
        xpath_for_save_pop_up = "(//div[@id='popup280'])[3]"
        xpath_for_yes_button_in_save_pop_up = "(//div[@id='popup280'])[3]//span//a[@id='btnSaveYes']"

        ############### Initializing wait ###############################
        wait = WebDriverWait(self.driver, 10)

        ############### Wait and select option from the Main page ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_all_the_options_in_His)))
        all_options = self.driver.find_elements(By.XPATH, xpath_for_all_the_options_in_His)
        for option in all_options:
            if option.text.strip() == self.main_menu_option:
                option.click()
                break

        ############### Wait and select option from the inventory dropdown ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_inventory_dropdown)))
        inventory_dropdown_values = self.driver.find_element(By.XPATH,
                                                             xpath_for_dropdown_values_of_inventory_pop_up)
        dropdown_values = Select(inventory_dropdown_values)
        for options in dropdown_values.options:
            if options.text.strip() == self.drop_down_option:
                options.click()
                break
            # print(options.text)


        ############### wait and select "Yes" or "No" from the Inventory Pop up ###############################
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_footer_in_inventory_pop_up)))
        footer_locator_in_inventory_pop_up = self.driver.find_elements(By.XPATH,
                                                                       xpath_for_footer_in_inventory_pop_up)
        for button in footer_locator_in_inventory_pop_up:
            if button.text.strip() == self.footer_option:
                button.click()
                break
            elif button.text.strip() == self.footer_option:
                button.click()
                break
            else:
                print("No options found in footer")
                break

        ############### wait and enter option into the search field ###############################
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_search_field_in_inventory)))
        search_field = self.driver.find_element(By.XPATH, xpath_for_search_field_in_inventory)
        search_field.send_keys(self.search_field_option)



        ############### wait and click the Indent Item ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_Indent_Items)))
        Indent_item = self.driver.find_element(By.XPATH, xpath_for_Indent_Items)
        self.driver.execute_script("arguments[0].click();", Indent_item)

        xpath_for_search_direct_receipt_options = '//input[@id="txtSearch"]'
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_search_direct_receipt_options)))

        ############### wait and locate the 3tabs ###############################

        for index, object in enumerate(items_from_direct_receipt_sheet, start=1):
            medicine_found = False
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_tabs)))
            three_tabs = self.driver.find_elements(By.XPATH, xpath_for_tabs)

            unique_medicine = object["medicine"]
            qty_value = object["quantity"]
            bat_value = object["batch"]

            date_object = object["date"]

            # Skip empty (nan) rows
            if pd.isna(unique_medicine) or pd.isna(qty_value) or pd.isna(bat_value) or pd.isna(date_object):
                continue

                # Convert quantity float -> int
            qty_value = int(qty_value)

            print("Medicine: ", unique_medicine)
            print("Quantity: ", qty_value)
            print("Batch: ", bat_value)
            print("Date: ", date_object)

            # Convert date to DD/MM/YYYY safely
            if isinstance(date_object, str):
                try:
                    date_object = datetime.strptime(date_object, "%d/%m/%Y")
                except:
                    try:
                        date_object = datetime.strptime(date_object, "%Y-%m-%d %H:%M:%S")
                    except:
                        print(f"⚠ Invalid date format in Excel → {date_object} (skipped)")
                        continue

            date_value = date_object.strftime("%d/%m/%Y")

            for tab in three_tabs:
                tab_text = tab.text.strip()  # Removing the blank spaces using the strip and storing the text of the tabs (Medicine, Consumables and Others into a variable called tab_text
                if medicine_found:
                    break
                if tab_text == "Medicine":  # if text in the tab_text matches with Medicine then click the Medicine tab
                    tab.click()
                    search_option = self.driver.find_element(By.XPATH, xpath_for_search_direct_receipt_options)
                    search_option.clear()
                    search_option.send_keys(unique_medicine)
                    search_option.send_keys(Keys.ENTER)
                    xpath_for_items_under_tabs = f"//td[contains(normalize-space(.), '{unique_medicine}')]"

                    try:
                        # Wait and find the element
                        wait.until(
                            expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_items_under_tabs)))
                        item_medicine = self.driver.find_element(By.XPATH, xpath_for_items_under_tabs)

                        print(f"✅ Found '{item_medicine.text.strip()}' under tab: {tab_text}")
                        medicine_found = True
                        item_medicine.click()

                        xpath_for_qty_in_table_2 = f"//tr[td[1][contains(text(), '{index}')] and td[3][contains(text(), '{unique_medicine}')]]//input[contains(@id, 'txtQty')]"
                        qty_field = self.driver.find_element(By.XPATH, xpath_for_qty_in_table_2)
                        # qty_field.send_keys(Keys.ENTER)
                        # qty_field.clear()
                        # qty_field.send_keys(qty_value)
                        # print(f"{unique_medicine} qty is {qty_field}")
                        self.driver.execute_script("arguments[0].value = '';", qty_field)
                        qty_field.click()
                        qty_field.send_keys(Keys.CONTROL, "a")  # Select all
                        qty_field.send_keys(Keys.DELETE)  # Delete
                        qty_field.send_keys(str(qty_value))


                        xpath_for_batch_in_table_2 = f"//tr[td[1][contains(text(), '{index}')] and td[3][contains(text(),'{unique_medicine}')]]//input[contains(@id,'txtBatch')]"
                        batch_field = self.driver.find_element(By.XPATH, xpath_for_batch_in_table_2)
                        batch_field.send_keys(Keys.ENTER)
                        batch_field.clear()
                        batch_field.send_keys(bat_value)
                        print(f"{unique_medicine} qty is {bat_value}")

                        xpath_for_date_field = f"//tr[td[1][contains(text(), '{index}')] and td[3][contains(text(), '{unique_medicine}')]]//input[contains(@id, 'txtexpdate')]"
                        date_field = self.driver.find_element(By.XPATH, xpath_for_date_field)
                        date_field.send_keys(Keys.ENTER)
                        date_field.clear()
                        date_field.send_keys(date_value)
                        print(f"{unique_medicine} qty is {date_value}")
                        break  # Exit inner loop once found


                    except Exception as e:
                        print(f"❌ '{unique_medicine}' not found under tab: {tab_text} — {type(e).__name__}")
                        continue


                elif tab_text == "Consumables": # if text in the tab_text matches with Consumables then click the Consumables tab
                    tab.click()
                    search_option = self.driver.find_element(By.XPATH, xpath_for_search_direct_receipt_options)
                    search_option.clear()
                    search_option.send_keys(unique_medicine)
                    search_option.send_keys(Keys.ENTER)
                    xpath_for_items_under_tabs = f"//td[contains(normalize-space(.), '{unique_medicine}')]"

                    try:
                        # Wait and find the element
                        wait.until(
                            expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_items_under_tabs)))
                        item_consumables = self.driver.find_element(By.XPATH, xpath_for_items_under_tabs)

                        print(f"✅ Found '{item_consumables.text.strip()}' under tab: {tab_text}")
                        medicine_found = True
                        item_consumables.click()

                        xpath_for_qty_in_table_2 = f"//tr[td[1][contains(text(), '{index}')] and td[3][contains(text(), '{unique_medicine}')]]//input[contains(@id, 'txtQty')]"
                        qty_field = self.driver.find_element(By.XPATH, xpath_for_qty_in_table_2)
                        # qty_field.send_keys(Keys.ENTER)
                        # qty_field.clear()
                        # qty_field.send_keys(qty_value)
                        # print(f"{unique_medicine} qty is {qty_field}")
                        self.driver.execute_script("arguments[0].value = '';", qty_field)

                        qty_field.click()
                        qty_field.send_keys(Keys.CONTROL, "a")  # Select all
                        qty_field.send_keys(Keys.DELETE)  # Delete
                        qty_field.send_keys(str(qty_value))

                        xpath_for_batch_in_table_2 = f"//tr[td[1][contains(text(), '{index}')] and td[3][contains(text(),'{unique_medicine}')]]//input[contains(@id,'txtBatch')]"
                        batch_field = self.driver.find_element(By.XPATH, xpath_for_batch_in_table_2)
                        batch_field.send_keys(Keys.ENTER)
                        batch_field.clear()
                        batch_field.send_keys(bat_value)
                        print(f"{unique_medicine} qty is {bat_value}")

                        xpath_for_date_field = f"//tr[td[1][contains(text(), '{index}')] and td[3][contains(text(), '{unique_medicine}')]]//input[contains(@id, 'txtexpdate')]"
                        date_field = self.driver.find_element(By.XPATH, xpath_for_date_field)
                        date_field.send_keys(Keys.ENTER)
                        date_field.clear()
                        date_field.send_keys(date_value)
                        print(f"{unique_medicine} qty is {date_value}")
                        break  # Exit inner loop once found

                    except Exception as e:
                        print(f"❌ '{unique_medicine}' not found under tab: {tab_text} — {type(e).__name__}")
                        continue


                elif tab_text == "Others": # if text in the tab_text matches with Consumables then click the Consumables tab
                    tab.click()
                    search_option = self.driver.find_element(By.XPATH, xpath_for_search_direct_receipt_options)
                    search_option.clear()
                    search_option.send_keys(unique_medicine)
                    search_option.send_keys(Keys.ENTER)
                    xpath_for_items_under_tabs = f"//td[contains(normalize-space(.), '{unique_medicine}')]"
                    try:
                        # Wait and find the element
                        wait.until(
                            expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_items_under_tabs)))
                        item_others = self.driver.find_element(By.XPATH, xpath_for_items_under_tabs)

                        print(f"✅ Found '{item_others.text.strip()}' under tab: {tab_text}")
                        medicine_found = True
                        item_others.click()

                        xpath_for_qty_in_table_2 = f"//tr[td[1][contains(text(), '{index}')] and td[3][contains(text(), '{unique_medicine}')]]//input[contains(@id, 'txtQty')]"
                        qty_field = self.driver.find_element(By.XPATH, xpath_for_qty_in_table_2)
                        # qty_field.send_keys(Keys.ENTER)
                        # qty_field.clear()
                        # qty_field.send_keys(qty_value)
                        # print(f"{unique_medicine} qty is {qty_field}")
                        self.driver.execute_script("arguments[0].value = '';", qty_field)

                        qty_field.click()
                        qty_field.send_keys(Keys.CONTROL, "a")  # Select all
                        qty_field.send_keys(Keys.DELETE)  # Delete
                        qty_field.send_keys(str(qty_value))

                        xpath_for_batch_in_table_2 = f"//tr[td[1][contains(text(), '{index}')] and td[3][contains(text(),'{unique_medicine}')]]//input[contains(@id,'txtBatch')]"
                        batch_field = self.driver.find_element(By.XPATH, xpath_for_batch_in_table_2)
                        batch_field.send_keys(Keys.ENTER)
                        batch_field.clear()
                        batch_field.send_keys(bat_value)
                        print(f"{unique_medicine} qty is {bat_value}")

                        xpath_for_date_field = f"//tr[td[1][contains(text(), '{index}')] and td[3][contains(text(), '{unique_medicine}')]]//input[contains(@id, 'txtexpdate')]"
                        date_field = self.driver.find_element(By.XPATH, xpath_for_date_field)
                        date_field.send_keys(Keys.ENTER)
                        date_field.clear()
                        date_field.send_keys(date_value)
                        print(f"{unique_medicine} qty is {date_value}")
                        break  # Exit inner loop once found


                    except Exception as e:
                        print(f"❌ '{unique_medicine}' not found under tab: {tab_text} — {type(e).__name__}")
                        continue


        time.sleep(100)
        ############### wait and enter the remarks###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_remarks)))
        Remarks_Box = self.driver.find_element(By.XPATH, xpath_for_remarks)
        Remarks_Box.send_keys("abc")

        ############### wait and click the calculate button ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_calculate)))
        calculate_button = self.driver.find_element(By.XPATH, xpath_for_calculate)
        calculate_button.click()

        ############### wait and print total value ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_total)))
        total_amount = self.driver.find_element(By.XPATH, xpath_for_total)
        total_amount_value = total_amount.get_attribute("value")
        print(f"Total amount: {total_amount_value}")

        time.sleep(10)
        ############### wait and click save button ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_save)))
        save_button = self.driver.find_element(By.XPATH, xpath_for_save)
        save_button.click()
        ############### wait and print total value ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_save_pop_up)))
        Yes_button_save = self.driver.find_element(By.XPATH, xpath_for_yes_button_in_save_pop_up)
        Yes_button_save.click()
        time.sleep(30)

        self.driver.quit()

test_run = Receipt_Direct()
url, username, password, facility_option, main_menu_option, drop_down_option, footer_option, search_field_option, items_from_direct_receipt_sheet = test_run.read_an_excel_file()
test_run.login_page(url, username, password, facility_option)
test_run.direct_update(main_menu_option, drop_down_option, footer_option, search_field_option, items_from_direct_receipt_sheet)
