# Generated by Django 3.0.2 on 2020-01-31 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keystoneapp', '0004_auto_20200131_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationdata',
            name='regnumber',
        ),
    ]