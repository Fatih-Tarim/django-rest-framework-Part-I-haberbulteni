# Generated by Django 3.2.16 on 2023-04-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haberler', '0006_alter_makale_yayimlanma_tarihi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makale',
            name='yayimlanma_tarihi',
            field=models.DateTimeField(),
        ),
    ]
