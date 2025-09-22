import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from page_Objects.Page_Object_HIS_User_Creation_Masters import His_User_Registration
from page_Objects.Page_Objects_HIS_Login_Page import His_Login_Page
from page_Objects.Page_Objects_HIS_Front_Office_Registration import His_OutPatient_Registration
from testCases.test_His_Login_page import TestHISLoginPage


class TestUserCreation(TestHISLoginPage):

    @pytest.mark.skip(reason='Not necessary for now')
    def test_his_user_creation(self, pandas_excel):
        ###################### Reading a sheet called Masters abd a column callled Mastersoptions from excelwork book ###############################
        data = pandas_excel('Masters')
        self.logger.info("*********Reading a sheet called Masters from excelwork book*************")
        search_option_name = data['MasterOptions'].iloc[0]
        self.logger.info(f'{search_option_name}')

        ###################### Assigning an oject to the Paje Object class name ###############################
        self.user_register_object = His_User_Registration(self.driver)
        self.logger.info(f'{self.user_register_object}')

        wait = WebDriverWait(self.driver, 30)

        ###################### Selecting a Facility ###############################
        self.user_register_object.select_facility(self.driver)

        ###################### waiting and clicking the Masters option in Home Page ###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.user_register_object.xpath_for_masters_option_in_home_page)))
        self.user_register_object.click_masters()

        ###################### waiting and clicking the yes button in the Masters Pop Up ###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.user_register_object.xpath_for_yes_button_in_Masters_Pop_up)))
        self.user_register_object.click_yes_button_in_masters_pop_up()

        ###################### waiting and clicking the search option ###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.user_register_object.xpath_for_search_field_in_Masters)))
        self.user_register_object.search_option_in_masters(search_option_name)

        ###################### waiting and clicking the user access option ###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.user_register_object.xpath_for_User_Access_under_User_Access_in_Master)))
        self.user_register_object.click_the_user_access_option()

        ###################### Iterating through all the columns and assigning the columns #############################
        for index, row in data.iterrows():
            Name = row['Name']
            LoginName = row['LoginName']
            Password = row['Password']
            Confirm_Password = row['Confirm_Password']
            Interface_ID = row['Interface_ID']
            Department = row['Department']
            Mobile_Number = row['Mobile_Number']

            ###################### Waiting and entering the Name ###########################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_Name_in_user_access)))
            self.user_register_object.enter_name_in_user_access(Name)

            ###################### Waiting and entering the Login Name #######################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_Login_name_in_user_access)))
            self.user_register_object.enter_login_name_in_user_access(LoginName)

            ###################### Waiting and entering the Password ##########################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_Password_in_user_access)))
            self.user_register_object.enter_password_in_user_access(Password)

            ###################### Waiting and entering the confirm Password ####################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_Confirm_Password_in_user_access)))
            self.user_register_object.enter_confirm_password_in_user_access(Confirm_Password)

            ###################### Waiting and entering the interface id ########################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_Interface_ID_in_user_access)))
            self.user_register_object.enter_interface_id(Interface_ID)

            ###################### Waiting and entering the departments name ####################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_department_names_in_user_access)))
            self.user_register_object.enter_department_names(Department)

            ###################### Waiting and entering the Login Name #########################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_mobile_number_in_user_access)))
            self.user_register_object.enter_mobile_number(Mobile_Number)

            ###################### Waiting and entering the Login Name ####################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_save_button_in_user_access)))
            self.user_register_object.click_save_button()

            ###################### Waiting and clicking the yes button in the save pop up ####################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_save_confirmation_pop_up_in_user_access)))
            self.user_register_object.click_yes_button_in_save_pop_up()

            time.sleep(5)

    def test_reset_password(self, pandas_excel):
        data = pandas_excel('Masters')
        search_option_name = data['MasterOptions'].iloc[0]
        login_id = str(data['LoginName'].iloc[0])
        user_id = str(data['LoginName'].iloc[0])
        ###################### Assigning an oject to the Paje Object class name ###############################
        self.user_register_object = His_User_Registration(self.driver)
        self.logger.info(f'{self.user_register_object}')

        wait = WebDriverWait(self.driver, 30)

        ###################### Selecting a Facility ###############################
        self.user_register_object.select_facility(self.driver)

        ###################### waiting and clicking the Masters option in Home Page ###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.user_register_object.xpath_for_masters_option_in_home_page)))
        self.user_register_object.click_masters()

        ###################### waiting and clicking the yes button in the Masters Pop Up ###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.user_register_object.xpath_for_yes_button_in_Masters_Pop_up)))
        self.user_register_object.click_yes_button_in_masters_pop_up()

        ###################### waiting and clicking the search option ###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.user_register_object.xpath_for_search_field_in_Masters)))
        self.user_register_object.search_option_in_masters(search_option_name)

        ###################### waiting and clicking the user access option ###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.user_register_object.xpath_for_User_Access_under_User_Access_in_Master)))
        self.user_register_object.click_the_user_access_option()

        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                      self.user_register_object.xpath_for_search_id_login_name)))
        self.user_register_object.enter_login_name(login_id)
        time.sleep(5)

        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.user_register_object.xpath_for_pop_up_for_login_name)))
        self.user_register_object.click_user_login_id_in_Pop_up(user_id)

        for index, row in data.iterrows():
            Password = row['Password']
            Confirm_Password = row['Confirm_Password']

            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_password_locked_checkbox)))
            self.user_register_object.click_the_check_box_to_uncheck()

            ###################### Waiting and entering the Password ##########################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_Password_in_user_access)))
            self.user_register_object.enter_password_in_user_access(Password)

            ###################### Waiting and entering the confirm Password ####################
            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_Confirm_Password_in_user_access)))
            self.user_register_object.enter_confirm_password_in_user_access(Confirm_Password)

            wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.user_register_object.xpath_for_update_button)))
            self.user_register_object.click_the_update_button()

            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.user_register_object.xpath_for_modification_pop_up)))
            self.user_register_object.click_the_yes_button_in_pop_up()

            time.sleep(30)
