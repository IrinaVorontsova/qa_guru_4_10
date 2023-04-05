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
            birth_month="November",
            birth_year="2000",
            birth_day="20",
            interests=Hobbies.science.value,
            hobby='Sports',
            photo_path="photo_test.jpg",
            address='USA, 12723 street',
            state='Rajasthan',
            city='Jaiselmer'
        )
        registration = RegistrationPage()
        registration.registration_user(user)

        registration.assert_saved_form(user),\
            "Some field was not corrected"
