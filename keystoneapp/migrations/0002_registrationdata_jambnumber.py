# Generated by Django 3.0.2 on 2020-01-25 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('keystoneapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationdata',
            name='jambnumber',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
