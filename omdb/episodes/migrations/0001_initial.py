# Generated by Django 4.1.6 on 2023-02-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('released', models.DateField()),
                ('imdbRating', models.FloatField()),
                ('runtime', models.CharField(max_length=10)),
                ('poster', models.CharField(max_length=500, unique=True)),
                ('actors', models.ManyToManyField(to='episodes.actor')),
                ('genre', models.ManyToManyField(to='episodes.genre')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]