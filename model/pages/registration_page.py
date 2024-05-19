from selene import command, by, have
from selene.support.shared import browser

import resource


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.user_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.subjects_input = browser.element('#subjectsInput')
        self.upload_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def fill_click_element(self, value):
        browser.element(by.text(value)).perform(command.js.click)

    def fill_user_gender(self, value):
        self.fill_click_element(value)

    def fill_user_number(self, value):
        self.user_number.type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subjects_input(self, value):
        browser.element('#subjectsInput').set_value(value).press_enter()

    def fill_hobbies(self, value):
        self.fill_click_element(value)

    def fill_upload_picture(self, file):
        self.upload_picture.set_value(resource.path(file))

    def fill_current_address(self, value):
        self.current_address.set_value(value)

    def fill_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view)
        self.state.click().element(by.text(value)).click()

    def fill_city(self, value):
        self.city.click().element(by.text(value)).click()

    def fill_submit(self):
        self.submit.click()

    def should_finish_form_title(self, value):
        browser.element('.modal-title').should(have.text(value))

    def should_registered_user_with(self, full_name, email,
                                    user_gender, user_number, date_of_birth,
                                    subjects_input, hobbies, upload_picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                user_gender,
                user_number,
                date_of_birth,
                subjects_input,
                hobbies,
                upload_picture,
                current_address,
                state_and_city
            )
        )

    def fill_close_large_modal(self):
        browser.element('#closeLargeModal').perform(command.js.click)
