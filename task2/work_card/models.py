from django.db import models

class CreditCard(models.Model):
    '''Модель кредитной карты'''
    STATUS = [
        ('активирована','активирована'),    
        ('не активирована','не активирована'),    
        ('просрочена','просрочена'),        
    ]

    series = models.BigIntegerField(verbose_name='Серия')
    number = models.BigIntegerField(verbose_name='Номер')
    date_issue = models.DateTimeField(verbose_name='Дата выпуска')
    date_end_activity = models.DateTimeField(verbose_name='Дата окончания')
    date_use = models.DateTimeField(verbose_name='Дата использования',
                                    blank=True, null=True)
    amount = models.FloatField(verbose_name='Сумма', default=0)
    status = models.CharField(verbose_name='Статус', max_length=15,
                              choices=STATUS)

    class Meta:
        verbose_name_plural = 'Кредитные карты'
        verbose_name = 'Кредитная карта'

class Purchase(models.Model):
    '''Модель покупок'''
    card = models.ForeignKey(CreditCard,
                             on_delete=models.CASCADE,
                             verbose_name='Кредитная карта')
    name_product = models.CharField(max_length=100, verbose_name='Название продукта')
    price = models.FloatField(verbose_name='Цена')
    date_purchase = models.DateTimeField(verbose_name='Дата покупки')