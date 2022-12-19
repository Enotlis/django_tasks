from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterUserForm, LoginUserForm, ChoiceAnswerForm
from .models import TestSuit, Question, QuizSession
import json

def _get_current_question(questions: str) -> tuple:
    '''Получение id текущего вопроса'''
    jsonDec = json.decoder.JSONDecoder()
    questions = jsonDec.decode(questions)
    question = questions.pop(0)
    return question, json.dumps(questions)

def _check_question(question, quiz_session, user_selected_answers: list):
    '''Проверка ответов на вопрос'''
    selected_answers = question.answer_set.filter(pk__in=user_selected_answers)
    correct_answers = question.answer_set.filter(correct_answer=True)

    if selected_answers == correct_answers or\
        set(selected_answers).issubset(correct_answers):
        weigth_answers = len(selected_answers)/len(correct_answers)
        quiz_session.count_correct_answer += weigth_answers
        quiz_session.count_wrong_answer += (1 - weigth_answers)
    else:
        quiz_session.count_wrong_answer += 1

def register(request):
    '''Регистрация нового пользователя'''
    form = RegisterUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse_lazy('login'))
    return render(request, 'registr.html', {'form': form})

class LoginView(LoginView):
    '''Вход пользователя'''
    form_class = LoginUserForm
    template_name = 'login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    '''Выход пользователя'''
    template_name = 'logout.html'

def get_testsuit(request):
    objects = TestSuit.objects.all()
    return render(request, 'get_testsuit.html', {'objects_list': objects})

@login_required
def create_session(request, pk):
    '''Создание сессии для пользователя и наборов тестов'''
    questions = list(Question.objects.filter(test_suit=pk).values('id'))
    quiz_session = {'username':request.user,
                    'test_suit': TestSuit.objects.get(pk=pk),
                    'unanswered_task':json.dumps(questions)}
    quiz_session = QuizSession.objects.create(**quiz_session)
    return redirect(reverse_lazy("quiz", kwargs={'pk':quiz_session.id}))

@login_required
def quiz(request, pk):
    '''Проведение тестирования'''
    quiz_session = QuizSession.objects.get(pk=pk)
    question_id, unanswered_task = _get_current_question(quiz_session.unanswered_task)
    question = Question.objects.get(pk=question_id['id'])
    form = ChoiceAnswerForm(request.POST or None, question_id=question.id)
    context = {'question': question,
               'form': form}

    if request.method == "POST":
        if form.is_valid():            
            quiz_session.unanswered_task = unanswered_task
            _check_question(question, quiz_session, form.cleaned_data['answers'])

            if unanswered_task == '[]':
                count_questions = quiz_session.count_correct_answer + quiz_session.count_wrong_answer
                quiz_session.percent_correct_answer = quiz_session.count_correct_answer/count_questions*100
                quiz_session.save()
                return redirect(reverse_lazy("complete_test",
                                             kwargs={'pk':quiz_session.id}))
           
            quiz_session.save()
            return redirect(reverse_lazy("quiz", kwargs={'pk':pk}))

    return render(request, 'question.html', context)

@login_required
def complete_test(request, pk):
    '''Вывод результата текущего тестирования'''
    result = QuizSession.objects.get(pk=pk)
    return render(request, 'success.html', {'result': result})