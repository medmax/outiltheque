# Generated by Django 3.0.5 on 2020-05-02 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_auto_20200502_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='date_begin',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='loan',
            name='date_end',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
