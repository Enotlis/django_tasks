# Generated by Django 3.2.6 on 2022-12-17 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_card', '0004_alter_creditcard_date_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='date_use',
            field=models.DateTimeField(verbose_name='Дата использования'),
        ),
    ]
