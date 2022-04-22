# Generated by Django 4.0.4 on 2022-04-22 01:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_rename_answer_answer_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='phone_number',
            field=models.CharField(blank=True, help_text='format: 01012341234', max_length=13, null=True, validators=[django.core.validators.RegexValidator('^\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d$', message='Wrong format enter')], verbose_name='전화번호'),
        ),
    ]
