# Generated by Django 5.0 on 2023-12-13 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iq', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John', max_length=40)),
                ('sex', models.CharField(choices=[('male', 'мужской'), ('female', 'женский'), ('think', 'неопределенный'), ('fight helicopter', 'боевой вертолет')], max_length=20)),
                ('brain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='human', to='OnetoOneApp.brain')),
            ],
        ),
    ]
