# Generated by Django 3.2 on 2021-04-22 01:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='token_expiration',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 22, 3, 22, 21, 575166)),
        ),
    ]
