from django.forms.widgets import TextInput

class EmailInput(TextInput):
    input_type = 'email'

class DateInput(TextInput):
    input_type = 'date'

class PasswordInput(TextInput):
    input_type = 'password'

class HiddenInput(TextInput):
    input_type = 'hidden'