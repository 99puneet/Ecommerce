# Generated by Django 3.0.2 on 2020-01-18 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='emailAddress',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ShippingAddress1',
            new_name='shippingAddress1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ShippingCity',
            new_name='shippingCity',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ShippingCountry',
            new_name='shippingCountry',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ShippingName',
            new_name='shippingName',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ShippingPostcode',
            new_name='shippingPostcode',
        ),
    ]
