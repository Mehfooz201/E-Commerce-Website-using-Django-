# Generated by Django 4.0.4 on 2022-08-18 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_amonut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amonut',
            field=models.IntegerField(default=0),
        ),
    ]
