# Generated by Django 5.1.4 on 2024-12-22 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0011_alter_word_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['-date_joined'], 'verbose_name_plural': 'words'},
        ),
    ]