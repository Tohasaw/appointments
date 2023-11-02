# Generated by Django 4.2.1 on 2023-05-27 18:30

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': ('Должность',),
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approvalDate', models.DateField()),
            ],
            options={
                'verbose_name': ('Прайс-лист',),
                'verbose_name_plural': 'Прайс-листы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('length', models.IntegerField(verbose_name='Длительность')),
            ],
            options={
                'verbose_name': ('Услуга',),
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': ('Дата',),
                'verbose_name_plural': 'Расписание',
            },
        ),
        migrations.CreateModel(
            name='WorkingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.TimeField(verbose_name='Начало рабочего времени')),
                ('endtime', models.TimeField(verbose_name='Конец рабочего времени')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workingtime_employee_set', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.table', verbose_name='Дата')),
            ],
            options={
                'verbose_name': ('Рабочие часы',),
                'verbose_name_plural': 'Рабочие часы',
            },
        ),
        migrations.CreateModel(
            name='PriceListPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('priceList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.pricelist', verbose_name='Прайс-лист')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': ('Позиция прайс-листа',),
                'verbose_name_plural': 'Позиции прайс-листа',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('hiringDate', models.DateField(verbose_name='Дата приема')),
                ('dismissDate', models.DateField(blank=True, null=True, verbose_name='Дата увольнения')),
                ('birthDate', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.job', verbose_name='Должность')),
            ],
            options={
                'verbose_name': ('Сотрудник',),
                'verbose_name_plural': 'Сотрудники',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.TimeField(verbose_name='Врема начала приема')),
                ('endTime', models.TimeField(verbose_name='Время окончания приема')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('priceListPosition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.pricelistposition', verbose_name='Позиция прайс-листа')),
                ('workingTime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.workingtime', verbose_name='Рабочие часы')),
            ],
            options={
                'verbose_name': ('Запись на прием',),
                'verbose_name_plural': 'Записи на прием',
            },
        ),
    ]
