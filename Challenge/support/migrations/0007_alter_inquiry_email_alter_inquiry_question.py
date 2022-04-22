# Generated by Django 4.0.4 on 2022-04-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0006_alter_inquiry_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='email',
            field=models.CharField(max_length=80, verbose_name='작성자 이메일'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='question',
            field=models.CharField(max_length=80, verbose_name='문의 질문'),
        ),
    ]