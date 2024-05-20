# Generated by Django 5.0.6 on 2024-05-20 04:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_product_users_productcategory_users_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_products",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="users",
            field=models.ManyToManyField(
                related_name="products", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="productcategory",
            name="users",
            field=models.ManyToManyField(
                related_name="categories", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]