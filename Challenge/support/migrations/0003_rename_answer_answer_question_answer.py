# Generated by Django 4.0.4 on 2022-04-19 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_inquiry_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='question_answer',
        ),
    ]