# Generated by Django 3.2.15 on 2022-12-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quize', '0002_quizsession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizsession',
            name='count_correct_answer',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='quizsession',
            name='count_wrong_answer',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
