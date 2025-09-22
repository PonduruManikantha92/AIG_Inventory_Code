import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from page_Objects.Page_Object_HIS_Front_Office_Bills_Utility import His_OP_Bills_Utility
from page_Objects.Page_Object_HIS_Refund_Approval import His_OP_Refund_Approval
from page_Objects.Page_Objects_HIS_Front_Office_Billing import His_OP_Billing
from page_Objects.Page_Objects_HIS_Login_Page import (His_Login_Page)
from page_Objects.Page_Objects_HIS_Front_Office_Registration import His_OutPatient_Registration
from testCases.test_login_page_HIS import TestHIS_Login_Page




class TestHISFrontOffice(TestHIS_Login_Page):
    logger = LogGen.loggen()

    @pytest.fixture(scope='class')
    def excel_reader(self, pandas_excel):
        data_one = pandas_excel('Front_Office_Registration')
        return {'data': data_one}

    ################# Add Patient ##############
    def test_his_front_office_patient_registration(self, excel_reader, test_his_login_page):

        ####### data driving from the excel sheet #################
        desired_option_Add_Patient = excel_reader['data']['Add_Patient_Options'].iloc[0]
        title = "Mr."
        firstname = excel_reader['data']['Inputs'].iloc[0]
        Gender = excel_reader['data']['Inputs'].iloc[1]
        age = str(excel_reader['data']['Inputs'].iloc[2])
        status_of_marriage = excel_reader['data']['Inputs'].iloc[3]
        mobile_number = str(excel_reader['data']['Inputs'].iloc[8])
        house_number = str(excel_reader['data']['Inputs'].iloc[9])
        locality = excel_reader['data']['Inputs'].iloc[10]
        source_option = excel_reader['data']['Inputs'].iloc[11]
        yes_or_no = excel_reader['data']['Inputs'].iloc[13]
        option_yes_or_no = excel_reader['data']['Inputs'].iloc[14]
        output_data = []

        ######### storing the pageobject class name inside a variable ############
        driver = test_his_login_page
        ########### Powering the Page Object  class His_OutPatient_Registration by sending driver as an argument
        his_home_object = His_OutPatient_Registration(driver)

        self.logger.info("*********Select Facility*************")
        his_home_object.select_facility()

        self.logger.info("*********Click the Front office option in His HomePage*************")
        his_home_object.Select_Front_Office_from_HIS_Homepage()

        self.logger.info("*********Click Yes Button in the Front Office Pop up*************")
        his_home_object.Click_yes_button_in_front_office_pop_up()

        self.logger.info("********* Click the add patient option *************")
        his_home_object.click_the_Add_patient()

        self.logger.info("********* Click any option under the add paitent option *************")
        his_home_object.select_an_option_from_add_patient(desired_option_Add_Patient)

        self.logger.info("********* Select a Title *************")
        his_home_object.enter_title(title)
        if title:
            title_entered = "title entered successfully"
        else:
            title_entered = "failed to enter title"
        output_data.append(f'Title:{title_entered}')

        self.logger.info("********* Fill the firstname *************")
        his_home_object.enter_first_name(firstname)
        if firstname:
            first_name_entered = "firstname entered successfully"
        else:
            first_name_entered = "failed to enter firstname"
        output_data.append(f'First_name:{first_name_entered}')

        self.logger.info("********* Select a Gender *************")
        his_home_object.select_a_gender(Gender)
        if Gender:
            gender_update = "Gender entered successfully"
        else:
            gender_update = "failed to enter Gender"
        output_data.append(f'Gender:{gender_update}')

        self.logger.info("********* Click the age *************")
        his_home_object.click_age(age)
        if age:
            age_entered = "Age entered Successfully"
        else:
            age_entered = "Failed to enter age"
        output_data.append(f'age:{age_entered}')

        self.logger.info("********* Select status of Marriage *************")
        his_home_object.select_marital_status(status_of_marriage)
        if status_of_marriage:
            marriage_status = "Marriage status selected"
        else:
            marriage_status = "Unable to record the marital status"
        output_data.append(f'marriage_Status:{marriage_status}')

        self.logger.info("********* Enter the mobile number *************")
        his_home_object.enter_mobile_number(mobile_number)
        if mobile_number:
            mobile_number_entered = "Mobile entered Successfully"
        else:
            mobile_number_entered = "Failed to enter mobile number"
        output_data.append(f'mobile_number:{mobile_number_entered}')

        self.logger.info("********* Enter Address *************")
        his_home_object.enter_house_number(house_number)
        if house_number:
            house_number_entered = "Entered house successfully"
        else:
            house_number_entered = "Failed to enter house address"
        output_data.append(f'house_number: {house_number_entered}')

        self.logger.info("********* Enter Locality *************")
        his_home_object.enter_locality(locality)
        if locality:
            locality_entered = "Entered locality success"
        else:
            locality_entered = "Entered locality success"
        output_data.append(f'locality: {locality_entered}')

        self.logger.info("********* Enter source option *************")
        his_home_object.enter_source(source_option)
        if source_option:
            source_option_entered = "Source Option Entered Successfully"
        else:
            source_option_entered = "Failed to enter Source Option"
        output_data.append(f'source_option: {source_option_entered}')

        self.logger.info("********* Click register button *************")
        his_home_object.click_register_button()


        self.logger.info("********* Patient Details *************")
        patient_details = driver.find_element(By.XPATH,
                                                   his_home_object.xpath_for_patient_details_in_confirm_patient_details)
        output_data.append(patient_details.text)
        print(patient_details.text)

        self.logger.info("********* Save Patient Details *************")
        his_home_object.confirmation_pop_up(yes_or_no)
        if yes_or_no:
            yes_or_no_option = "Clicked yes or no button"
        else:
            yes_or_no_option = "Failed to click yes or no button"
        output_data.append(f'yes_or_no_option:{yes_or_no_option}')

        self.logger.info("********* Successful message *************")
        successful_message = driver.find_element(By.XPATH, his_home_object.xpath_for_successful_message)
        output_data.append(successful_message.text)

        self.logger.info("********* Registration Successful Pop up *************")
        his_home_object.Registered_Successfully_pop_up(option_yes_or_no)
        if option_yes_or_no:
            yes_or_no_option = "Clicked either yes or no"
        else:
            yes_or_no_option = "failed to click either yes or no"


        time.sleep(5)

    def test_generate_bill_by_cash (self, excel_reader, test_his_login_page):
        logger = LogGen.loggen()
        Doctor_name = excel_reader['data']['Billing_Details'].iloc[0]
        refer = excel_reader['data']['Billing_Details'].iloc[1]

        driver = test_his_login_page

        front_office_billing = His_OP_Billing(driver)

        ######### Search for Doctors Name #####################
        self.logger.info("*************** Search for Doctors name *********************")
        front_office_billing.search_for_doctor_name(Doctor_name)
        driver.save_screenshot(".\\Screenshots\\searching_for_doc_name.png")

        ######### Referred By#####################
        self.logger.info("*************** Referred By *********************")
        front_office_billing.refered_by(refer)
        driver.save_screenshot(".\\Screenshots\\Referred_By.png")

        ######### Clicking add to bill#####################
        self.logger.info("*************** Clicking add to bill *********************")
        front_office_billing.click_add_to_bill()
        driver.save_screenshot(".\\Screenshots\\click_add_to_bill.png")


        ######### Clicking the billing option #####################
        self.logger.info("*************** Clicking the billing option  *********************")
        front_office_billing.click_the_billing_option()
        driver.save_screenshot(".\\Screenshots\\Clicking_the_billing_option.png")


        ######### Generate Bill Pop up #####################
        self.logger.info("*************** Generate Bill Pop up  *********************")
        front_office_billing.generate_bill_pop_up()
        driver.save_screenshot(".\\Screenshots\\Generate_Bill_Pop_up.png")


        ######### Process Payment #####################
        self.logger.info("*************** Process Payment  *********************")
        front_office_billing.click_save_button_in_process_payment()
        driver.save_screenshot(".\\Screenshots\\Process Payment.png")


        ######### Print the Bill #####################
        self.logger.info("*************** Print the Bill  *********************")
        front_office_billing.print_the_bill()
        driver.save_screenshot(".\\Screenshots\\print_the_bill.png")

        ######### Click the home button #####################
        self.logger.info("*************** Click the home button  *********************")
        front_office_billing.click_home_button()
        driver.save_screenshot(".\\Screenshots\\click_home_button.png")

    def test_generate_bill_by_cash_discount (self, excel_reader, test_his_login_page):

        Doctor_name = excel_reader['data']['Billing_Details'].iloc[0]
        refer = excel_reader['data']['Billing_Details'].iloc[1]

        uhid_for_discount = excel_reader['data']['Discount_Details'].iloc[0]
        Discount_on_option = excel_reader['data']['Discount_Details'].iloc[1]
        Discount_head = excel_reader['data']['Discount_Details'].iloc[2]
        Discount_reason = excel_reader['data']['Discount_Details'].iloc[3]
        Discount_percentage = excel_reader['data']['Discount_Details'].iloc[4]
        Authorized_By = excel_reader['data']['Discount_Details'].iloc[5]

        driver = test_his_login_page
        front_office_billing_with_discount = His_OP_Billing(driver)
        his_home_object = His_OutPatient_Registration(driver)

        self.logger.info("*********Select Facility*************")
        his_home_object.select_facility()

        ######### Click the Front office option in His HomePage #####################
        self.logger.info("*********Click the Front office option in His HomePage*************")
        his_home_object.Select_Front_Office_from_HIS_Homepage()
        driver.save_screenshot(".\\Screenshots\\clicking_the_front_office_in_home_page.png")

        ######### Click Yes Button in the Front Office Pop up #####################
        self.logger.info("*********Click Yes Button in the Front Office Pop up*************")
        his_home_object.Click_yes_button_in_front_office_pop_up()
        driver.save_screenshot(".\\Screenshots\\Click_yes_button_in_the_front_Office_Pop.png")

        ######### Click the Billing option under Home #####################
        self.logger.info("************ Click the Billing option under Home ******************")
        front_office_billing_with_discount.click_billing_option_under_home()
        driver.save_screenshot(".\\Screenshots\\clicking_the_billing_option_under_home.png")

        ######### Enter the UHID #####################
        self.logger.info("************ Enter the UHID ******************")
        front_office_billing_with_discount.enter_the_uhid(uhid_for_discount)
        driver.save_screenshot(".\\Screenshots\\Enter_the_UHID.png")

        ######### Search for Doctors Name #####################
        self.logger.info("*************** Search for Doctors name *********************")
        front_office_billing_with_discount.search_for_doctor_name(Doctor_name)
        driver.save_screenshot(".\\Screenshots\\searching_for_doc_name.png")

        ######### Referred By#####################
        self.logger.info("*************** Referred By *********************")
        front_office_billing_with_discount.refered_by(refer)
        driver.save_screenshot(".\\Screenshots\\Referred_By.png")

        ######### Clicking add to bill#####################
        self.logger.info("*************** Clicking add to bill *********************")
        front_office_billing_with_discount.click_add_to_bill()
        driver.save_screenshot(".\\Screenshots\\click_add_to_bill.png")

        # ######### Close the deposit pop up#####################
        # self.logger.info("*************** Close the deposit pop up *********************")
        # front_office_billing.close_the_deposit_pop_up()
        # driver.save_screenshot(".\\Screenshots\\close_the_deposit_pop_up.png")
        # time.sleep(2)
        #########Click  yes button in discount pop up#####################
        self.logger.info("*************** Click  yes button in discount pop up *********************")
        front_office_billing_with_discount.click_yes_button_in_discount_pop()
        driver.save_screenshot(".\\Screenshots\\click_yes_button_in_discount_pop_up.png")

        ######### Process Discount #####################
        self.logger.info("*************** Process Discount *********************")
        front_office_billing_with_discount.process_discount(Discount_on_option, Discount_head, Discount_reason,
                                                   Discount_percentage, Authorized_By)
        driver.save_screenshot(".\\Screenshots\\click_yes_button_in_discount_pop_up.png")

        ######### Clicking the billing option #####################
        self.logger.info("*************** Clicking the billing option  *********************")
        front_office_billing_with_discount.click_the_billing_option()
        driver.save_screenshot(".\\Screenshots\\Clicking_the_billing_option ")


        ######### Generate Bill Pop up #####################
        self.logger.info("*************** Generate Bill Pop up  *********************")
        front_office_billing_with_discount.generate_bill_pop_up()
        driver.save_screenshot(".\\Screenshots\\Generate_Bill_Pop_up")
        time.sleep(3)

        ######### Process Payment #####################
        self.logger.info("*************** Process Payment  *********************")
        front_office_billing_with_discount.click_save_button_in_process_payment()
        driver.save_screenshot(".\\Screenshots\\Generate_Bill_Pop_up")

        #########Print the Bill #####################
        self.logger.info("*************** Print the Bill  *********************")
        front_office_billing_with_discount.print_the_bill()
        driver.save_screenshot(".\\Screenshots\\print_the_bill")

        #########Click the home button #####################
        self.logger.info("*************** Click the home button  *********************")
        front_office_billing_with_discount.click_home_button()
        driver.save_screenshot(".\\Screenshots\\click_home_button.png")
        time.sleep(5)


    def test_bills_utility_refund(self, excel_reader, test_his_login_page):
        driver = test_his_login_page
        his_home_object = His_OutPatient_Registration(driver)
        his_bills_utility_object = His_OP_Bills_Utility(driver)

        self.logger.info("*********Select Facility*************")
        his_home_object.select_facility()

        ######### Click the Front office option in His HomePage #####################
        self.logger.info("*********Click the Front office option in His HomePage*************")
        his_home_object.Select_Front_Office_from_HIS_Homepage()
        driver.save_screenshot(".\\Screenshots\\clicking_the_front_office_in_home_page.png")

        ######### Click Yes Button in the Front Office Pop up #####################
        self.logger.info("*********Click Yes Button in the Front Office Pop up*************")
        his_home_object.Click_yes_button_in_front_office_pop_up()
        driver.save_screenshot(".\\Screenshots\\Click_yes_button_in_the_front_Office_Pop.png")

        ######### Click Bills Utility Option #####################
        self.logger.info("*********Click Bills Utility Option*************")
        his_bills_utility_object.click_bills_utility_under_home()
        driver.save_screenshot(".\\Screenshots\\Click_bills_utility_option.png")

        ######### Enter UHID in Bills Utility Option #####################
        self.logger.info("*********Enter UHID in Bills Utility Option*************")
        his_bills_utility_object.enter_the_uhid_in_bills_utility()
        driver.save_screenshot(".\\Screenshots\\Enter_UHID_in_Bills_Utility_Option.png")

        ######### Click the select refund button #####################
        self.logger.info("*********Click the select refund button*************")
        his_bills_utility_object.click_the_select_refund_button()
        driver.save_screenshot(".\\Screenshots\\Click_the_select_refund_button.png")

        ######### Select all options in Refund Pop up #####################
        self.logger.info("*********Select all options in Refund Pop up*************")
        his_bills_utility_object.select_all_options_in_pop_up()
        driver.save_screenshot(".\\Screenshots\\Select_all_options_in_pop_up.png")

        ######### Select reason and remarks for sending approval request #####################
        self.logger.info("*********Select reason and remarks for sending approval request*************")
        his_bills_utility_object.select_reason_for_approval_request_and_remarks()
        driver.save_screenshot(".\\Screenshots\\Select_reason_remarks_for_sending_approval_request.png")
        time.sleep(20)

        #########Click the home button #####################
        self.logger.info("*************** Click the home button  *********************")
        his_bills_utility_object.click_home_button()
        driver.save_screenshot(".\\Screenshots\\click_home_button.png")
        time.sleep(5)


    def test_approve_refund(self, excel_reader, test_his_login_page):
        driver = test_his_login_page
        his_home_object = His_OutPatient_Registration(driver)
        his_approve_refund_object = His_OP_Refund_Approval(driver)

        self.logger.info("*********Select Facility*************")
        his_home_object.select_facility()

        ######### Click the Front office option in His HomePage #####################
        self.logger.info("*********Click the Front office option in His HomePage*************")
        his_home_object.Select_Front_Office_from_HIS_Homepage()
        driver.save_screenshot(".\\Screenshots\\clicking_the_front_office_in_home_page.png")

        ######### Click Yes Button in the Front Office Pop up #####################
        self.logger.info("*********Click Yes Button in the Front Office Pop up*************")
        his_home_object.Click_yes_button_in_front_office_pop_up()
        driver.save_screenshot(".\\Screenshots\\Click_yes_button_in_the_front_Office_Pop.png")

        ######### Click approve refund option under Billing #####################
        self.logger.info("*********Click approve refund option under Billing*************")
        his_approve_refund_object.click_refund_approval_under_billing()
        driver.save_screenshot(".\\Screenshots\\Click_approve_refund_option_under_Billing.png")

        ######### Click the search icon #####################
        self.logger.info("*********Click the search icon*************")
        his_approve_refund_object.click_the_search_icon()
        driver.save_screenshot(".\\Screenshots\\click_the_search_icon.png")

        ######### Click the approve button #####################
        self.logger.info("*********Click the approve button*************")
        his_approve_refund_object.click_the_approve_button()
        driver.save_screenshot(".\\Screenshots\\Click_the_approve_button.png")

        ######### Click the yes button in approve pop up#####################
        self.logger.info("*********Click the yes button in approve pop up*************")
        his_approve_refund_object.click_yes_button_in_approve_pop_up()
        driver.save_screenshot(".\\Screenshots\\Click_the_yes_button_in_approve_pop_up.png")

        ######### Click the home button #####################
        self.logger.info("*********Click the home button*************")
        his_approve_refund_object.click_home_button()
        driver.save_screenshot(".\\Screenshots\\Click_the_home_button.png")

    def test_refund_the_approved_op_bill(self, excel_reader, test_his_login_page):
        driver = test_his_login_page
        his_home_object = His_OutPatient_Registration(driver)
        his_bills_utility_object = His_OP_Bills_Utility(driver)


        self.logger.info("*********Select Facility*************")
        his_home_object.select_facility()

        ######### Click the Front office option in His HomePage #####################
        self.logger.info("*********Click the Front office option in His HomePage*************")
        his_home_object.Select_Front_Office_from_HIS_Homepage()
        driver.save_screenshot(".\\Screenshots\\clicking_the_front_office_in_home_page.png")

        ######### Click Yes Button in the Front Office Pop up #####################
        self.logger.info("*********Click Yes Button in the Front Office Pop up*************")
        his_home_object.Click_yes_button_in_front_office_pop_up()
        driver.save_screenshot(".\\Screenshots\\Click_yes_button_in_the_front_Office_Pop.png")

        ######### Click Bills Utility Option #####################
        self.logger.info("*********Click Bills Utility Option*************")
        his_bills_utility_object.click_bills_utility_under_home()
        driver.save_screenshot(".\\Screenshots\\Click_bills_utility_option.png")

        ######### Enter UHID in Bills Utility Option #####################
        self.logger.info("*********Enter UHID in Bills Utility Option*************")
        his_bills_utility_object.enter_the_uhid_in_bills_utility()
        driver.save_screenshot(".\\Screenshots\\Enter_UHID_in_Bills_Utility_Option.png")

        ######### Click the yes button in confirmed refund pop up #####################
        self.logger.info("*********Click the yes button in confirmed refund pop up*************")
        his_bills_utility_object.click_yes_button_in_confirm_refund_pop_up()
        driver.save_screenshot(".\\Screenshots\\Click_the_yes_button_in_confirmed_refund_pop_up.png")

        ######### Select the mode of payment #####################
        self.logger.info("*********Select the mode of payment *************")
        his_bills_utility_object.select_the_mode_of_payment()
        driver.save_screenshot(".\\Screenshots\\.Select_the_mode_of_payment.png")

        ######### Click the save button #####################
        self.logger.info("*********Click the save button*************")
        his_bills_utility_object.click_save_button()
        driver.save_screenshot(".\\Screenshots\\.Click_the_save_button.png")

        ######### Click yes button in refund by cash pop up #####################
        self.logger.info("*********Click yes button in refund by cash pop up*************")
        his_bills_utility_object.click_yes_button_in_refund_by_cash_pop_up()
        driver.save_screenshot(".\\Screenshots\\.Click_yes_button_in_refund_by_cash_pop_up.png")

        ######### Click the home button #####################
        self.logger.info("*********Click the home button*************")
        his_bills_utility_object.click_home_button()
        driver.save_screenshot(".\\Screenshots\\Click_the_home_button.png")


    def test_due_settle_the_op_bill_one(self, excel_reader, test_his_login_page):

        logger = LogGen.loggen()
        Doctor_name = excel_reader['data']['Billing_Details'].iloc[0]
        refer = excel_reader['data']['Billing_Details'].iloc[1]
        Uhid_for_due_settlement = excel_reader['data']['Due_Settlement_Details'].iloc[0]
        due_settlement_uhid = str(Uhid_for_due_settlement)

        driver = test_his_login_page

        his_home_object = His_OutPatient_Registration(driver)
        front_office_billing = His_OP_Billing(driver)
        his_bills_utility_object = His_OP_Bills_Utility(driver)

        self.logger.info("*********Select Facility*************")
        his_home_object.select_facility()

        ######### Click the Front office option in His HomePage #####################
        self.logger.info("*********Click the Front office option in His HomePage*************")
        his_home_object.Select_Front_Office_from_HIS_Homepage()
        driver.save_screenshot(".\\Screenshots\\clicking_the_front_office_in_home_page.png")

        ######### Click Yes Button in the Front Office Pop up #####################
        self.logger.info("*********Click Yes Button in the Front Office Pop up*************")
        his_home_object.Click_yes_button_in_front_office_pop_up()
        driver.save_screenshot(".\\Screenshots\\Click_yes_button_in_the_front_Office_Pop.png")

        ######### Click the Billing option under Home #####################
        self.logger.info("************ Click the Billing option under Home ******************")
        front_office_billing.click_billing_option_under_home()
        driver.save_screenshot(".\\Screenshots\\clicking_the_billing_option_under_home.png")

        ######### Enter the UHID #####################
        self.logger.info("************ Enter the UHID ******************")
        front_office_billing.enter_the_uhid(due_settlement_uhid)
        driver.save_screenshot(".\\Screenshots\\Enter_the_UHID.png")

        ######### Search for Doctors Name #####################
        self.logger.info("*************** Search for Doctors name *********************")
        front_office_billing.search_for_doctor_name(Doctor_name)
        driver.save_screenshot(".\\Screenshots\\searching_for_doc_name.png")

        ######### Referred By#####################
        self.logger.info("*************** Referred By *********************")
        front_office_billing.refered_by(refer)
        driver.save_screenshot(".\\Screenshots\\Referred_By.png")

        ######### Clicking add to bill#####################
        self.logger.info("*************** Clicking add to bill *********************")
        front_office_billing.click_add_to_bill()
        driver.save_screenshot(".\\Screenshots\\click_add_to_bill.png")

        ######### Clicking the billing option #####################
        self.logger.info("*************** Clicking the billing option  *********************")
        front_office_billing.click_the_billing_option()
        driver.save_screenshot(".\\Screenshots\\Clicking_the_billing_option.png")

        ######### Generate Bill Pop up #####################
        self.logger.info("*************** Generate Bill Pop up  *********************")
        front_office_billing.generate_bill_pop_up()
        driver.save_screenshot(".\\Screenshots\\Generate_Bill_Pop_up.png")

        ######### Process Payment only half amount #####################
        self.logger.info("*************** Process Payment only half amount  *********************")
        front_office_billing.amount_field_in_process_payment_Billing()
        driver.save_screenshot(".\\Screenshots\\Generate_Bill_Pop_up.png")

        ######### Enter amount in Process Payment pop up #####################
        self.logger.info("*************** Enter amount in Process Payment pop up  *********************")
        front_office_billing.amount_field_in_process_payment_Billing()
        driver.save_screenshot(".\\Screenshots\\Enter_amount_in_Process_payment_Pop_up.png")

        ######### Click save button in Process Payment #####################
        self.logger.info("*************** Click save button in Process Payment  *********************")
        front_office_billing.click_save_button_in_process_payment()
        driver.save_screenshot(".\\Screenshots\\click_the_save_button.png")
        time.sleep(3)

        ######### Select authorised by #####################
        self.logger.info("*************** Select authorised by  *********************")
        front_office_billing.select_authorized_by()
        driver.save_screenshot(".\\Screenshots\\select_authorized_by.png")

        ######### Enter Remarks #####################
        self.logger.info("*************** Enter Remarks  *********************")
        front_office_billing.enter_remarks()
        driver.save_screenshot(".\\Screenshots\\enter_remarks.png")

        ######### Click Verify Button ###################
        self.logger.info("*************** Click Verify Button ********************")
        front_office_billing.click_the_verify_button()
        driver.save_screenshot(".\\Screenshots\\click_the_verify_button.png")

        ######### Print the Bill ############
        self.logger.info("*************** Print the Bill *************")
        front_office_billing.print_the_bill()
        driver.save_screenshot(".\\Screenshots\\print_the_bill().png")
        time.sleep(2)

        ######### Click Home Button ###################
        self.logger.info("*************** Click Home Button ********************")
        his_bills_utility_object.click_home_button()
        driver.save_screenshot(".\\Screenshots\\click_home_button.png")


    def test_due_settle_the_op_bill_two(self, excel_reader, test_his_login_page):
        logger = LogGen.loggen()
        Doctor_name = excel_reader['data']['Billing_Details'].iloc[0]
        refer = excel_reader['data']['Billing_Details'].iloc[1]
        Uhid_for_due_settlement = excel_reader['data']['Due_Settlement_Details'].iloc[0]
        due_settlement_uhid = str(Uhid_for_due_settlement)

        driver = test_his_login_page

        his_home_object = His_OutPatient_Registration(driver)
        front_office_billing = His_OP_Billing(driver)
        his_bills_utility_object = His_OP_Bills_Utility(driver)

        self.logger.info("*********Select Facility*************")
        his_home_object.select_facility()

        ######### Click the Front office option in His HomePage #####################
        self.logger.info("*********Click the Front office option in His HomePage*************")
        his_home_object.Select_Front_Office_from_HIS_Homepage()
        driver.save_screenshot(".\\Screenshots\\clicking_the_front_office_in_home_page.png")

        ######### Click Yes Button in the Front Office Pop up #####################
        self.logger.info("*********Click Yes Button in the Front Office Pop up*************")
        his_home_object.Click_yes_button_in_front_office_pop_up()
        driver.save_screenshot(".\\Screenshots\\Click_yes_button_in_the_front_Office_Pop.png")

        ######### Click Bills Utility under Home ###################
        self.logger.info("*************** Click Bills Utility under Home ********************")
        his_bills_utility_object.click_bills_utility_under_home()
        driver.save_screenshot(".\\Screenshots\\click_bills_utility_under_home.png")

        # ######### Enter the UHID ###################
        self.logger.info("*************** Enter the UHID ********************")
        his_bills_utility_object.enter_the_uhid_in_bills_utility(due_settlement_uhid)
        driver.save_screenshot(".\\Screenshots\\enter_the_uhid_in_bills_utility.png")
        time.sleep(2)
        ######### Click Due Settlement ###################
        self.logger.info("*************** Click Due Settlement ********************")
        his_bills_utility_object.click_due_settlement()
        driver.save_screenshot(".\\Screenshots\\click_due_settlement.png")
        time.sleep(2)

        ######### Click Plus Button ###################
        self.logger.info("*************** Click Plus Button ********************")
        his_bills_utility_object.click_plus_button()
        driver.save_screenshot(".\\Screenshots\\click_plus_button.png")
        time.sleep(2)

        ######### Click make receipt button ############
        self.logger.info("*************** Click make receipt button *************")
        his_bills_utility_object.click_make_receipt_button()
        driver.save_screenshot(".\\Screenshots\\click_make_receipt_button().png")
        time.sleep(2)

        ######### Click yes in save pop up ############
        self.logger.info("*************** Click yes in save pop up *************")
        his_bills_utility_object.click_yes_in_save_pop_up()
        driver.save_screenshot(".\\Screenshots\\click_yes_in_save_pop_up().png")
        time.sleep(2)







