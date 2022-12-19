# Generated by Django 3.2.15 on 2022-12-12 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestSuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Набор тестов')),
            ],
            options={
                'verbose_name': 'Набор тестов',
                'verbose_name_plural': 'Наборы тестов',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Вопрос')),
                ('test_suit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quize.testsuit', verbose_name='Набор тестов')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст ответа')),
                ('correct_answer', models.BooleanField(default=False, verbose_name='Ответ верный')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quize.question')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
