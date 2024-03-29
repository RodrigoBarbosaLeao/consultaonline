# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=20)),
                ('mensagem', models.CharField(max_length=255)),
                ('hora', models.DateTimeField()),
                ('confirmado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='consultorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='backend.Consultorio'),
        ),
    ]
