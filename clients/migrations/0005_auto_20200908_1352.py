# Generated by Django 2.2 on 2020-09-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20200902_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownedcar',
            name='date_of_last_service',
            field=models.DateField(default='yyyy-mm-dd'),
        ),
    ]
