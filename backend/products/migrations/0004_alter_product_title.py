# Generated by Django 4.2.13 on 2024-05-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
