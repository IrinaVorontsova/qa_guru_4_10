from selene.support.shared import browser
from selene import be, have, command
import pytest
import os

from locators.page_locators import PageLocators
from models.registration_model import FormRegistration, Hobbies
from pages.registration_page import RegistrationPage


class TestPage:

    @staticmethod
    def set_url():
        return 'https://demoqa.com/automation-practice-form'

    def test_form(self, driver_browser):
        user = FormRegistration(
            first_name='Антон',
            last_name='Антонов',
            email='anton@anton.ru',
            gender="Other",
            phone_number=7111111111,
            birth_month="October",
            birth_year="2000",
            birth_day="020",
            interests=Hobbies.science.value,
            hobby='Sports',
            photo_path="photo_test.jpg",
            address='USA, 12723 street',
            state='Rajasthan',
            city='Jaiselmer'
        )
        registration = RegistrationPage()

        registration.set_first_name(user.first_name)
        registration.set_last_name(user.last_name)
        registration.set_email(user.email)
        registration.set_gender(user.gender)
        registration.set_phone(user.phone_number)
        registration.set_date_birth()
        registration.set_hobby_one(user.interests)
        registration.set_hobby_two(user.hobby)
        registration.set_photo(user.photo_path)
        registration.set_address(user.address)
        registration.set_state(user.state)
        registration.set_city(user.city)
        registration.click_submit()

        #
        # browser.element('#currentAddress').should(be.blank).type(address)
        # browser.element('#react-select-3-input').should(be.blank).type('Rajasthan').press_enter()
        # browser.element('#react-select-4-input').should(be.blank).type('Jaiselmer').press_enter()
        # browser.element('#submit').perform(command.js.click)

        # Проверка
        browser.element('//tr[1]/td[2]').should(have.text(str(user.first_name + ' ' + user.last_name)))
        browser.element('//tr[2]/td[2]').should(have.text(user.email))
        browser.element('//tr[3]/td[2]').should(have.text('Other'))
        browser.element('//tr[4]/td[2]').should(have.text(str(user.phone_number)))
        browser.element('//tr[5]/td[2]').should(have.text('20 November,2000'))
        browser.element('//tr[6]/td[2]').should(have.text(user.interests))
        browser.element('//tr[7]/td[2]').should(have.text(user.hobby))
        browser.element('//tr[8]/td[2]').should(have.text(user.photo_path))
        browser.element('//tr[9]/td[2]').should(have.text(user.address))
        browser.element('//tr[10]/td[2]').should(have.text(user.state + ' ' + user.city))
        browser.element('#closeLargeModal').perform(command.js.click)
