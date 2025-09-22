from numpy.f2py.rules import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class His_OutPatient_Registration:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.xpath_for_facility_dropdown = "//select[@id='Facility']"
        self.xpath_for_facility_option = "//option[text()='AIG Hospitals, Gachibowli']"
        self.xpath_for_front_office = "//li[.//div/span[normalize-space(text())='Front Office']]"
        self.xpath_for_front_office_pop_up = "//div[@id='popup280']"
        self.xpath_for_yes_button_in_Front_Office_Pop_up = "//a[@id='btn_yes_desh']"
        self.xpath_for_add_patient = "//li[@id='FOAddPatientMenu']"
        self.xpath_for_all_options_under_Add_Patient = "//ul[@style='display: block;']"

        ################### Patient Registration Form ################
        self.xpath_for_title = "//Select[@id='title']"
        self.xpath_for_First_name = "//input[@id='firstName']"
        self.xpath_for_Gender = "//select[@id='gender']"
        # self.xpath_for_Dob = "//span[@id='sdob']//input[@id='dob']"
        self.xpath_for_age = "//input[@key='Age']"
        self.xpath_for_marital_status = "//select[@id='mStatus']"
        self.xpath_for_nationality = "//select[@id='nationality']"
        self.xpath_for_mobile_number = "//input[@id='mobileNo']"
        self.xpath_for_House_address = "//textarea[@id='address']"
        self.xpath_for_city = "//select[@id='city']"
        self.xpath_for_Locality = "//input[@id='locationid']"
        self.xpath_for_reason_for_modification = "//textarea[@id='_reasonForModifiaction']"
        self.xpath_for_source = "//select[@id='sref']"
        self.xpath_for_register = "//a[@id='register']"

        ################### Confirm Patient Details Popup xpath ################
        self.xpath_for_confirm_patient_details = "(//div[@id='popup300'])[1]"
        self.xpath_for_patient_details_in_confirm_patient_details = "(//section[@class='popupBodyupdate'])[1]"
        self.xpath_for_yes_and_no_button_in_confirm_patient_details_pop_up = "(//footer[@class='popupHeader'])[4]"
        self.xpath_for_yes_in_confirm_patient_details_pop = "(//a[text()='Yes'])[2]"
        self.xpath_for_no_in_confirm_patient_details_pop = "(//a[text()='No'])[2]"

        ################### Registered Successfully ################
        self.xpath_for_Registered_successfully = "(//div[@id='popup400'])[2]"
        self.xpath_for_successful_message = "(//section[@class='popupBody1'])[1]"
        self.xpath_for_yes_and_no_buttons_in_Registered_successfully_pop_up = "(//footer[@class='popupHeader'])[2]"
        self.xpath_for_yes_button_in_Registered_successfully_pop_up = "(//a[text()='Yes'])[1]"
        self.xpath_for_no_button_in_Registered_successfully_pop_up = "(//a[text()='No'])[1]"


    #################### Select a facility and select an option called Front Office from Home page ################
    def select_facility(self):
        facility_dropdown = self.driver.find_element(By.XPATH, self.xpath_for_facility_dropdown)
        facility_option = self.driver.find_element(By.XPATH, self.xpath_for_facility_option)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_facility_dropdown)))
        facility_dropdown.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_facility_option)))
        facility_option.click()

    def Select_Front_Office_from_HIS_Homepage(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_front_office)))
        front_office = self.driver.find_element(By.XPATH, self.xpath_for_front_office)
        front_office.click()

    def Click_yes_button_in_front_office_pop_up(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_yes_button_in_Front_Office_Pop_up)))
        yes_button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_Front_Office_Pop_up)
        yes_button.click()

    #################### Clicking the Add Patients option from the Front office page ################
    def click_the_Add_patient(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_add_patient)))
        add_patient_option = self.driver.find_element(By.XPATH, self.xpath_for_add_patient)
        add_patient_option.click()

    #################### Selecting an option under the Add Patients  #########################
    def select_an_option_from_add_patient(self, desired_option_Add_Patient):
        add_patients_xpath = f"//li/a[text()='{desired_option_Add_Patient}']"
        click_add_patients = self.driver.find_element(By.XPATH, add_patients_xpath)
        click_add_patients.click()

    #################### Patient Registration form action items ################
    def enter_title(self, title):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_title)))
        title_before_name = self.driver.find_element(By.XPATH, self.xpath_for_title)
        list_of_titles = Select(title_before_name)
        for option in list_of_titles.options:
            if option.text.strip() == title:
                option.click()

    def enter_first_name(self, firstname):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_First_name)))
        first_name = self.driver.find_element(By.XPATH, self.xpath_for_First_name)
        first_name.send_keys(firstname)

    def select_a_gender(self, Gender):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_Gender)))
        gender_name = self.driver.find_element(By.XPATH, self.xpath_for_Gender)
        gender_dropdown = Select(gender_name)

        for option in gender_dropdown.options:
            if option.text.strip() == Gender:
                option.click()
                print(f"selected:{option.text}")
                break

    def click_age(self, age):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_age)))
        age_radio_button = self.driver.find_element(By.XPATH, self.xpath_for_age)
        age_radio_button.click()
        xpath_of_age_field = "//input[@id='age']"
        field_of_age = self.driver.find_element(By.XPATH, xpath_of_age_field)
        field_of_age.send_keys(age)

    def select_marital_status(self, status_of_marriage):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_marital_status)))
        status = self.driver.find_element(By.XPATH, self.xpath_for_marital_status)
        marital_status = Select(status)

        for option in marital_status.options:
            if option.text.strip() == status_of_marriage:
                option.click()
                print(f"selected: {option.text}")
                break

    def enter_mobile_number(self, mobile_number):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_mobile_number)))
        phone_number = self.driver.find_element(By.XPATH, self.xpath_for_mobile_number)
        phone_number.send_keys(mobile_number)

    def enter_house_number(self, house_number):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_House_address)))
        flat = self.driver.find_element(By.XPATH, self.xpath_for_House_address)
        flat.send_keys(house_number)

    def enter_locality(self, locality):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_Locality)))
        place = self.driver.find_element(By.XPATH, self.xpath_for_Locality)
        place.send_keys(locality)

    def enter_source(self, source_option):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_source)))
        source = self.driver.find_element(By.XPATH, self.xpath_for_source)
        source_field = Select(source)
        for option in source_field.options:
            if option.text.strip() == source_option:
                print(option)
                option.click()

    def click_register_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_register)))
        register = self.driver.find_element(By.XPATH, self.xpath_for_register)
        register.click()

    def confirmation_pop_up(self, yes_or_no):
        if yes_or_no == "Yes":
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_yes_in_confirm_patient_details_pop)))
            yes_button = self.driver.find_element(By.XPATH, self.xpath_for_yes_in_confirm_patient_details_pop)
            yes_button.click()
        elif yes_or_no == "No":
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_no_in_confirm_patient_details_pop)))
            no_button = self.driver.find_element(By.XPATH, self.xpath_for_no_in_confirm_patient_details_pop)
            no_button.click()
        else:
            print("Unable to click either yes or no buttons")

    def Registered_Successfully_pop_up(self, option_yes_or_no):
        if option_yes_or_no == "Yes":
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_yes_button_in_Registered_successfully_pop_up)))
            yes_option = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_Registered_successfully_pop_up)
            yes_option.click()
        elif option_yes_or_no == "No":
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_no_button_in_Registered_successfully_pop_up)))
            no_option = self.driver.find_element(By.XPATH, self.xpath_for_no_button_in_Registered_successfully_pop_up)
            no_option.click()
        else:
            print("Unable to click either yes or no buttons")
