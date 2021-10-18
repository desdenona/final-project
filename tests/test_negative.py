from pages.base_page import Base
import pytest
from pages.contact_us import ContactUs
from time import sleep
from selenium.webdriver.common.by import By
import allure

# Negative - check that the name field contains only letters and is not empty
# Negative - check that the email is valid
# Negative - phone only digits, not letters, not empty
# Negative - Country only letters and spaces
# Negative- Message cannot have more than 180 letters, can be empty


@pytest.mark.usefixtures('set_up')
class TestNegative(Base):

    # @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.parametrize("name_input", ["111111", "!@#$%^&*()_+", "  ", ""])
    # def test_name_field(self, name_input):
    #     driver = self.driver
    #     contact = ContactUs(driver)
    #     contact.set_input_name(name_input)
    #     contact.set_input_email("nona-harutyunyan78@gmail.com")
    #     contact.set_input_phone_number("+37455787805")
    #     contact.set_input_country("Armenia")
    #     contact.set_input_company("BluNet")
    #     contact.set_input_message("Some text")
    #     contact.form_submit()
    #     assert contact.find_name_error_popup(), "Error message popup doesn't exist"
    #     sleep(3)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("email_input", ["n@mail.ru"])
    def test_email_field(self, email_input):
        driver = self.driver
        contact = ContactUs(driver)
        contact.set_input_name("Nona")
        contact.set_input_email(email_input)
        contact.set_input_phone_number("+37455787805")
        contact.set_input_country("Armenia")
        contact.set_input_company("BluNet")
        contact.set_input_message("Some text")
        contact.form_submit()
        assert contact.find_email_error_popup, "Error message popup doesn't exist"
        sleep(3)


#     @allure.severity(allure.severity_level.NORMAL)
#     @pytest.mark.parametrize("phone_number_input", ["asdasd", "!@#$%", "  ", ""])
#     def test_phone_number_field(self, phone_number_input):
#         driver = self.driver
#         contact = ContactUs(driver)
#         contact.set_input_name("Nona")
#         contact.set_input_email("nona-harutyunyan78@gmail.com")
#         contact.set_input_phone_number(phone_number_input)
#         contact.set_input_country("Armenia")
#         contact.set_input_company("BluNet")
#         contact.set_input_message("Some text")
#         contact.form_submit()
#         assert contact.find_phone_number_error_popup, "Error message popup doesn't exist"
#         sleep(3)

    # @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.parametrize("country_input", ["111111", "~!@#$%^&*()_+ ", " ", ""])
    # def test_phone_number_field(self, country_input):
    #     driver = self.driver
    #     contact = ContactUs(driver)
    #     contact.set_input_name("Nona")
    #     contact.set_input_email("nona-harutyunyan78@gmail.com")
    #     contact.set_input_phone_number("+37455787805")
    #     contact.set_input_country(country_input)
    #     contact.set_input_company("BluNet")
    #     contact.set_input_message("Some text")
    #     contact.form_submit()
    #     assert country_input != ' ' and country_input != '' and all(chr.isalpha() or chr.isspace() for chr in country_input), "Error message popup doesn't exist"

    #     sleep(3)


#     @allure.severity(allure.severity_level.MINOR)
#     @pytest.mark.parametrize("message_input", ["","181asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasda"])
#     def test_message_field(self, message_input):
#         driver = self.driver
#         contact = ContactUs(driver)
#         contact.set_input_name("Nona")
#         contact.set_input_email("nona-harutyunyan78@gmail.com")
#         contact.set_input_phone_number("+37455787805")
#         contact.set_input_country("Armenia")
#         contact.set_input_company("BluNet")
#         contact.set_input_message(message_input)
#         assert len(message_input) <= 180, "Can not contain more than 180 letters"
#         contact.form_submit()
#         sleep(3)
