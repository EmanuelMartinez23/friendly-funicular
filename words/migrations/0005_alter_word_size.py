# Generated by Django 5.1.4 on 2024-12-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_alter_word_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='size',
            field=models.IntegerField(max_length=30),
        ),
    ]
