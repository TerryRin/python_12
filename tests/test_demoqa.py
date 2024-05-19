import allure
from allure_commons.types import Severity

from model.pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("QA", "Polushina")
@allure.feature("Форма регистрации")
@allure.story("Заполнение формы регистрации")
@allure.link("https://demoqa.com", name="Test")
def test_form():
    with allure.step("Заполнение страницы"):
        registration_page = RegistrationPage()
        registration_page.open()

        registration_page.fill_first_name('Gandalf')
        registration_page.fill_last_name('Grey')
        registration_page.fill_email('gandalf@gmail.com')
        registration_page.fill_user_gender('Male')
        registration_page.fill_user_number('1234567890')
        registration_page.fill_date_of_birth('2024', 'March', '30')
        registration_page.fill_subjects_input('Arts')
        registration_page.fill_hobbies('Reading')
        registration_page.fill_upload_picture('Gendolf.jpg')
        registration_page.fill_current_address('adress')
        registration_page.fill_state('Haryana')
        registration_page.fill_city('Karnal')
        registration_page.fill_submit()

    with allure.step("Сравнение данных"):
        registration_page.should_finish_form_title('Thanks for submitting the form')
        registration_page.should_registered_user_with(
            'Gandalf Grey',
            'gandalf@gmail.com',
            'Male',
            '1234567890',
            '30 March,2024',
            'Arts',
            'Reading',
            'Gendolf.jpg',
            'adress',
            'Haryana Karnal'
        )
    with allure.step("Закрытие модалки"):
        registration_page.fill_close_large_modal()
