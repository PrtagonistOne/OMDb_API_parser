# Generated by Django 4.1.6 on 2023-02-11 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0001_initial'),
        ('episodes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seasons.season'),
        ),
    ]