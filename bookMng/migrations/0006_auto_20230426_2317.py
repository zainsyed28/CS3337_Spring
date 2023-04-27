# Generated by Django 3.2.16 on 2023-04-27 06:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0005_alter_comment_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='book',
            new_name='book_origin',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='publishdate',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]