# Generated by Django 2.2.13 on 2021-02-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='is_effective',
            field=models.BooleanField(default=True, verbose_name='是否有效'),
        ),
    ]
