# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-10 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('version_a', models.CharField(max_length=400)),
                ('version_b', models.CharField(max_length=400)),
                ('version_c', models.CharField(blank=True, max_length=400, null=True)),
                ('version_d', models.CharField(blank=True, max_length=400, null=True)),
                ('true', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'Питання тесту',
                'verbose_name_plural': 'Питання тестів',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('rating', models.CharField(max_length=3)),
                ('choices', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результати',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тести',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.Test'),
        ),
    ]