# Generated by Django 4.2 on 2023-04-28 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brapp', '0002_rename_hits_hit_rename_secrets_secret_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='short_code',
            new_name='shortcode',
        ),
    ]
