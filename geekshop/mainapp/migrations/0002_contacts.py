# Generated by Django 3.0.3 on 2020-02-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30, verbose_name='Город')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон (формат: +7-888-888-8888)')),
                ('email', models.CharField(max_length=64, verbose_name='Почта')),
                ('address', models.CharField(max_length=64, verbose_name='Адрес')),
            ],
        ),
    ]