# Generated by Django 3.0.2 on 2020-01-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keystoneapp', '0002_registrationdata_jambnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationdata',
            name='jambnumber',
            field=models.CharField(max_length=12),
        ),
    ]