# Generated by Django 3.2.16 on 2023-04-27 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0006_auto_20230426_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='publishdate',
            field=models.DateField(auto_now=True),
        ),
    ]
