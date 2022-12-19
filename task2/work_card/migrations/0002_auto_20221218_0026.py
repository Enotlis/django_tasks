# Generated by Django 3.2.6 on 2022-12-17 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_card', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creditcard',
            options={'verbose_name': 'Кредитная карта', 'verbose_name_plural': 'Кредитные карты'},
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='number',
            field=models.BigIntegerField(verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='series',
            field=models.BigIntegerField(verbose_name='Серия'),
        ),
    ]
