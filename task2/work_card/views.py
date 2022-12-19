from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import CreditCard
from .forms import FilterCreditCardForm, GenerateCardForm
from datetime import datetime
from dateutil.relativedelta import relativedelta

def _create_filters(form) -> dict:
    '''Создание фильтров на основе полей указанных пользователем'''
    #получаем название всех полей для фильтрации, которые есть в форме
    field_names = tuple(form.cleaned_data.keys())
    #создаем фильтры, только тех полей, которые были заполнены пользователем
    filter_clauses = {field:form.cleaned_data[field]
                      for field in field_names
                      if form.cleaned_data[field]}
    if 'date_issue' in filter_clauses:
        filter_clauses['date_issue__date'] = filter_clauses.pop('date_issue')
    if 'date_end_activity' in filter_clauses:
        filter_clauses['date_end_activity__date'] = filter_clauses.pop('date_end_activity')
    return filter_clauses


def get_creditcards(request):
    '''Вывод информации о кредитных картах'''
    cards = CreditCard.objects.all().values('pk','series','number',
                                            'date_issue','date_end_activity',
                                            'status')
    form = FilterCreditCardForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            filter_clauses = _create_filters(form)
            cards = cards.filter(**filter_clauses)
    return render(request, 'get_creditcards.html', {'form': form,
                                                    'cards_list': cards})

def delete_creditcard(request, pk):
    '''Удаление карту'''
    CreditCard.objects.filter(pk=pk).delete()
    return redirect(reverse_lazy('get_creditcards'))

def show_profile_card(request, pk):
    '''Показ профиля карты'''
    card = get_object_or_404(CreditCard, pk=pk) 
    return render(request, 'profile_card.html', {'card': card})

def activate_card(request, pk):
    '''Активация карты'''
    card = get_object_or_404(CreditCard, pk=pk)
    card.status = 'активирована'
    card.save()
    return redirect(reverse_lazy('get_creditcards'))

def deactivate_card(request, pk):
    '''Деактивация карты'''
    card = get_object_or_404(CreditCard, pk=pk)
    card.status = 'не активирована'
    card.save()
    return redirect(reverse_lazy('get_creditcards'))

def generate(request):
    '''Генерация карт'''
    form = GenerateCardForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            for i in range(1,form.cleaned_data['count']+1):
                now_date = datetime.now()
                term = int(form.cleaned_data['date_end_activity'])
                delta = relativedelta(months=+term)

                card = {'series': form.cleaned_data['series'],
                        'number': i,
                        'date_issue': now_date,
                        'date_end_activity': now_date+delta,
                        'status': 'активирована'}
                card = CreditCard.objects.get_or_create(**card)
        return redirect(reverse_lazy('get_creditcards'))
    return render(request, 'generate_cards.html', {'form': form})

def check_date_activity_card(request):
    '''Проверка срока дествия карт'''
    cards = CreditCard.objects.filter(date_end_activity__lt=datetime.now())
    for card in cards:
        card.status='просрочена'
        card.save()
    return redirect(reverse_lazy('get_creditcards'))