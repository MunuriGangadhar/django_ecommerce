# Generated by Django 4.2 on 2024-11-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_order_shipped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]
