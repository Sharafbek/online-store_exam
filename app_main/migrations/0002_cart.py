# Generated by Django 5.1.3 on 2024-11-21 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
        ('app_users', '0002_admin_customer_usermodel_is_admin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.customer')),
            ],
            options={
                'unique_together': {('product_id', 'user_id')},
            },
        ),
    ]
