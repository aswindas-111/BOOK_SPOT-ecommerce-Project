# Generated by Django 4.2.5 on 2023-10-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_coupon_max_usage_coupon_usage_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='used_coupons',
            field=models.ManyToManyField(blank=True, to='store.coupon'),
        ),
    ]
