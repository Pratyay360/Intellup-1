# Generated by Django 3.2.5 on 2021-07-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahandler', '0012_contest_starting_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='contesthistory',
            name='is_running',
            field=models.BooleanField(default=True, null=True),
        ),
    ]