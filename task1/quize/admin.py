from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from nested_admin.nested import NestedModelAdmin, NestedTabularInline, NestedStackedInline
from .models import TestSuit, Question, Answer


class AnswerInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super(AnswerInlineFormSet, self).clean()
        correct_answers = 0
        count_answers = 0
        
        for form in self.forms:
            if form.is_valid():
                if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                    count_answers += 1
                    if form.cleaned_data['correct_answer']:
                        correct_answers += 1
                
        if correct_answers == 0:
            raise ValidationError('Должен быть хотя бы один верный ответ')
        if correct_answers == count_answers:
            raise ValidationError('Не может быть, чтобы все ответы были верные')

class AnswerInLine(NestedStackedInline):
    model = Answer
    extra = 2
    formset = AnswerInlineFormSet

class QuestionInLine(NestedTabularInline):
    model = Question
    extra = 1
    inlines = [AnswerInLine]

class TestSuitAdmin(NestedModelAdmin):
    inlines = [QuestionInLine]

admin.site.register(TestSuit, TestSuitAdmin)
