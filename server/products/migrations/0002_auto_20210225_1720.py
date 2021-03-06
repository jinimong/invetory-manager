# Generated by Django 3.1.7 on 2021-02-25 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(
                max_length=50, unique=True, verbose_name="이름"
            ),
        ),
        migrations.AlterField(
            model_name="productcategory",
            name="name",
            field=models.CharField(
                max_length=50, unique=True, verbose_name="이름"
            ),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.product",
                verbose_name="제품",
            ),
        ),
        migrations.AlterField(
            model_name="productmaterial",
            name="name",
            field=models.CharField(
                max_length=50, unique=True, verbose_name="이름"
            ),
        ),
    ]
