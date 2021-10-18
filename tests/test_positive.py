from pages.base_page import Base
import pytest
from pages.contact_us import ContactUs
from time import sleep
from locators.locators import LocatorsXPath
from selenium.webdriver.common.by import By
import allure


# Positive - Check the clear button
# Positive - Check that the success notification pops up after form submission

@pytest.mark.usefixtures('set_up')
class TestPositive(Base):

    @allure.severity(allure.severity_level.CRITICAL)
    def test_fill_in_form(self):
        driver = self.driver
        contact = ContactUs(driver)
        contact.set_input_name("Nona")
        contact.set_input_email("nona-harutyunyan78@gmail.com")
        contact.set_input_phone_number("+37455787805")
        contact.set_input_country("Armenia")
        contact.set_input_company("BluNet")
        contact.set_input_message("Some text")
        contact.form_submit()
        assert contact.find_success_popup(), "Error message"
        sleep(3)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_clear_form(self):
        driver = self.driver
        contact = ContactUs(driver)
        contact.set_input_name("Nona")
        contact.set_input_email("nona-harutyunyan78@gmail.com")
        contact.set_input_phone_number("+37455787805")
        contact.set_input_country("Armenia")
        contact.set_input_company("BluNet")
        contact.set_input_message("Some text")
        contact.form_clear()

        assert len(contact.get_input_value(LocatorsXPath.fill_name_input)) == 0 and len(contact.get_input_value(LocatorsXPath.fill_email_input)) == 0 and len(contact.get_input_value(LocatorsXPath.fill_phone_number)) == 0 and len(
            contact.get_input_value(LocatorsXPath.fill_country_name_input)) == 0 and len(contact.get_input_value(LocatorsXPath.fill_company_name_input)) == 0 and len(contact.get_input_value(LocatorsXPath.fill_message_input)) == 0, "The input is not empty"

        sleep(3)
