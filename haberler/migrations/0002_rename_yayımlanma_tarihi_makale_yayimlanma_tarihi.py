# Generated by Django 4.2 on 2023-04-03 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("haberler", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="makale",
            old_name="yayımlanma_tarihi",
            new_name="yayimlanma_tarihi",
        ),
    ]
