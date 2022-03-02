from django.forms.widgets import TextInput

class DateInput(TextInput):
    input_type='date'

class EmailInput(TextInput):
    input_type='email'

class PasswordInput(TextInput):
    input_type='password'