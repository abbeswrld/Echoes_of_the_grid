# Generated by Django 5.1.1 on 2024-11-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='record',
            field=models.IntegerField(default=0),
        ),
    ]
