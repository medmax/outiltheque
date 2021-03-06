# Generated by Django 3.0.5 on 2020-05-05 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_loan_date_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='status',
            field=models.CharField(choices=[('New', 'demandé'), ('Accepted', 'accepté'), ('Rejected', 'refusé'), ('ToolRetrived', 'outil récupéré'), ('InProgress', 'prêt en cours'), ('ToolReturned', 'outil rendu'), ('Completed', 'terminé')], default='New', max_length=100),
        ),
    ]
