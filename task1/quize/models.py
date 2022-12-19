from django.db import models

class TestSuit(models.Model):
    '''Модель набора тестов'''
    name = models.CharField(max_length=150, verbose_name='Набор тестов')

    class Meta:
        verbose_name_plural = 'Наборы тестов'
        verbose_name = 'Набор тестов'

    def __str__(self):
        return self.name

class Question(models.Model):
    '''Модель вопроса'''
    text = models.TextField(verbose_name='Вопрос')
    test_suit = models.ForeignKey(TestSuit,
                                  on_delete=models.CASCADE,
                                  verbose_name='Набор тестов')

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'

    def __str__(self):
        return self.text

class Answer(models.Model):
    '''Модель ответа'''
    text = models.TextField(verbose_name='Текст ответа')
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)
    correct_answer = models.BooleanField(default=False,
                                         verbose_name='Ответ верный')

    class Meta:
        verbose_name_plural = 'Ответы'
        verbose_name = 'Ответ'

    def __str__(self):
        return self.text

class QuizSession(models.Model):
    '''Тестовая сессия пользователя'''
    username = models.CharField(max_length=150,
                                verbose_name='Имя пользователя')
    unanswered_task = models.TextField(verbose_name='Не отвеченные вопросы')
    test_suit = models.ForeignKey(TestSuit,
                                  on_delete=models.CASCADE,
                                  verbose_name='Набор тестов')
    count_correct_answer = models.FloatField(blank=True, default=0,
                                             verbose_name='Количество правильных ответов')
    count_wrong_answer = models.FloatField(blank=True, default=0,
                                           verbose_name='Количество неправильных ответов')
    percent_correct_answer = models.FloatField(blank=True, default=0,
                                               verbose_name='Процент правильных ответов')