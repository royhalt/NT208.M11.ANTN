# Generated by Django 3.2.9 on 2021-12-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
