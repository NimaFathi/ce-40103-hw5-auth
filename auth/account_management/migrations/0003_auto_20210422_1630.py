# Generated by Django 3.2 on 2021-04-22 16:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0002_alter_accesstoken_token_expiration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesstoken',
            name='id',
        ),
        migrations.RemoveField(
            model_name='accesstoken',
            name='token_expiration',
        ),
        migrations.RemoveField(
            model_name='accesstoken',
            name='username',
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 22, 18, 30, 8, 246701)),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account_management.account'),
            preserve_default=False,
        ),
    ]
