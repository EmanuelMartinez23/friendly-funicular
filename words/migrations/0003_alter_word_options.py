# Generated by Django 5.1.4 on 2024-12-22 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_alter_word_options_alter_word_table_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['size']},
        ),
    ]
