# Generated by Django 3.0.5 on 2020-05-23 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0009_auto_20200522_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='borrower_grade',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='tool_owner_grade',
        ),
    ]
