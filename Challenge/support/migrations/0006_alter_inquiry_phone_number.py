# Generated by Django 4.0.4 on 2022-04-22 02:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_alter_inquiry_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='phone_number',
            field=models.CharField(blank=True, help_text='format: 010-1234-1234', max_length=13, null=True, validators=[django.core.validators.RegexValidator('^01([0|1|6|7|8|9]?)-([0-9]{3,4})-([0-9]{4})', message='Wrong format enter')], verbose_name='전화번호'),
        ),
    ]