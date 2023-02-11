# Generated by Django 4.1.6 on 2023-02-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('season_number', models.IntegerField()),
                ('total_seasons', models.IntegerField()),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]