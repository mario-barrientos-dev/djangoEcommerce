# Generated by Django 4.1.1 on 2022-09-19 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
