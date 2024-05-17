# Generated by Django 5.0.6 on 2024-05-17 11:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="users",
            field=models.ManyToManyField(
                null=True, related_name="products", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="productcategory",
            name="users",
            field=models.ManyToManyField(
                null=True, related_name="categories", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(
            name="UserProduct",
        ),
    ]