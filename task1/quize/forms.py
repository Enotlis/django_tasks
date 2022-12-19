from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Answer

class RegisterUserForm(forms.ModelForm):
    '''Форма для регистрации пользователя'''
    username = forms.CharField(max_length=100, label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля",
                                widget=forms.PasswordInput,
                                help_text="Введите пароль повторно")

    class Meta:
        model = User
        fields = [
            'username'
        ]

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise ValidationError("Введеные пароли не совпадают")
        return password2 

class LoginUserForm(AuthenticationForm):
    '''Форма для входа пользователя'''
    username = forms.CharField(max_length=100, label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

class ChoiceAnswerForm(forms.Form):
    '''Форма для выбора ответа на вопрос'''
    answers = forms.MultipleChoiceField(choices=(),
                                        widget=forms.CheckboxSelectMultiple,
                                        label='Ответы',
                                        error_messages={'required': 'Выберите вариант ответа'})

    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id')
        super(ChoiceAnswerForm, self).__init__(*args, **kwargs)
        choices = ((answer.id, answer.text)
                   for answer in Answer.objects.filter(question=question_id))
        self.fields['answers'].choices = choices
