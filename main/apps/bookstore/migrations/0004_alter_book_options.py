# Generated by Django 4.0 on 2022-02-10 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
