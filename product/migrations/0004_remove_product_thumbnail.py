# Generated by Django 4.1.4 on 2022-12-20 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_thumnail_product_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]
