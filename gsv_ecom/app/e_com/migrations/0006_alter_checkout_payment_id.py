# Generated by Django 5.0.6 on 2024-11-15 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_com', '0005_alter_checkout_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='payment_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_com.payment'),
        ),
    ]