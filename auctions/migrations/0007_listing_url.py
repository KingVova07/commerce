# Generated by Django 3.0.1 on 2020-07-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='url',
            field=models.URLField(null=True),
        ),
    ]