# Generated by Django 4.2.2 on 2024-09-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_username_user_first_name_user_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ethereum_wallet_address',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
