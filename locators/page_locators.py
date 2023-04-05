class PageLocators:
    def set_month_birth(month):
        return f'option[value="{month}"]'

    def set_year_birth(year):
        return f'option[value="{year}"]'

    def set_day_birth(day):
        return f"react-datepicker__day--{day}"


    def set_saved_fields(field_name):
        return f"//tr[{field_name}]/td[2]"

    first_name = '#firstName'
    last_name = '#lastName'
    email = '#userEmail'

    gender_male = '[for="gender-radio-1"]'
    gender_female = '[for="gender-radio-2"]'
    gender_other = '[for="gender-radio-3"]'

    phone = '#userNumber'

    date_birth_field = '#dateOfBirthInput'
    date_birth_month = f'select[class="react-datepicker__month-select"] {set_month_birth("10")}'
    date_birth_year = f'select[class="react-datepicker__year-select"] {set_year_birth("2000")}'
    date_birth_day = f'*[class="react-datepicker__day {set_day_birth("020")}"]'

    hobby_field = '#subjectsInput'
    hobby_choose = '[for="hobbies-checkbox-1"]'

    photo = '#uploadPicture'

    address = '#currentAddress'

    state_choose = '#react-select-3-input'
    city_choose = '#react-select-4-input'

    submit = '#submit'

    saved_name = set_saved_fields(1)
    saved_email = set_saved_fields(2)
    saved_gender = set_saved_fields(3)
    saved_phone = set_saved_fields(4)
    saved_birth_day = set_saved_fields(5)
    saved_hobby = set_saved_fields(6)
    saved_hobby_add = set_saved_fields(7)
    saved_photo = set_saved_fields(8)
    saved_address = set_saved_fields(9)
    saved_state = set_saved_fields(10)

    close_form = '#closeLargeModal'