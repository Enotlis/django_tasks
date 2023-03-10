# Generated by Django 3.2.6 on 2022-12-17 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.IntegerField(verbose_name='Серия')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('date_issue', models.DateTimeField(verbose_name='Дата выпуска')),
                ('date_end_activity', models.DateTimeField(verbose_name='Дата окончания')),
                ('date_use', models.DateTimeField(verbose_name='Дата использования')),
                ('amount', models.FloatField(verbose_name='Сумма')),
                ('status', models.CharField(choices=[('активирована', 'активирована'), ('не активирована', 'не активирована'), ('просрочена', 'просрочена')], max_length=15, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('date_purchase', models.DateTimeField(verbose_name='Дата покупки')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_card.creditcard', verbose_name='Кредитная карта')),
            ],
        ),
    ]
