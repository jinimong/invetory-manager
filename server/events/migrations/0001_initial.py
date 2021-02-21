# Generated by Django 3.1.7 on 2021-02-22 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_type', models.CharField(choices=[('SD', '개인 판매'), ('OP', '발주'), ('SP', '입고'), ('SS', '정산'), ('ES', '입점'), ('LS', '퇴점'), ('DP', '불량')], max_length=2, verbose_name='재고 변화 타입')),
                ('description', models.TextField(verbose_name='설명')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('description', models.TextField(verbose_name='설명')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(verbose_name='변화 수량')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event', verbose_name='재고 변화 내역')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='제품')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.store', verbose_name='입점처'),
        ),
    ]