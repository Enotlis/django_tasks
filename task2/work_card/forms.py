from django import forms
from django.core.exceptions import ValidationError

class FilterCreditCardForm(forms.Form):
    STATUS = [
        ('активирована','активирована'),    
        ('не активирована','не активирована'),    
        ('просрочена','просрочена'),
        ('','')
    ]

    series = forms.IntegerField(label='Серия', required=False)
    number = forms.IntegerField(label='Номер', required=False)
    date_issue = forms.DateField(label='Дата выпуска',
                                 input_formats = ['%d.%m.%Y'],
                                 required=False,
                                 error_messages={'invalid':'Введите корректную дату'})
    date_end_activity = forms.DateField(label='Дата окончания активации',
                                 input_formats = ['%d.%m.%Y'],
                                 required=False,
                                 error_messages={'invalid':'Введите корректную дату'})
    status = forms.ChoiceField(label='Статус', initial='',
                               required=False, choices=STATUS)

    def clean_series(self):
        if self.cleaned_data['series']:
            series = self.cleaned_data['series']
            if series < 0:
                raise ValidationError('Серия не может быть отрицательной')
            return series

    def clean_number(self):
        if self.cleaned_data['number']:
            number = self.cleaned_data['number']
            if number < 0:
                raise ValidationError('Номер не может быть отрицательным')
            return number

class GenerateCardForm(forms.Form):
    TERMS = [
        (12, '1 год'),
        (6, '6 месяцев'),
        (1, '1 месяц')
    ]

    series = forms.IntegerField(label='Серия')
    date_end_activity = forms.ChoiceField(label='Срок окончания активности',
                                          choices=TERMS)
    count = forms.IntegerField(label='Количестов', initial=1)

    def clean_series(self):
        if self.cleaned_data['series']:
            series = self.cleaned_data['series']
            if series < 0:
                raise ValidationError('Серия не может быть отрицательной')
            return series