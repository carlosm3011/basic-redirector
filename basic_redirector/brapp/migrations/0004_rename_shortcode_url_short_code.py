# Generated by Django 4.2 on 2023-04-28 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brapp', '0003_rename_short_code_url_shortcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='shortcode',
            new_name='short_code',
        ),
    ]
