# Generated by Django 3.1.4 on 2023-03-31 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0013_auto_20230331_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold',
            name='delivery_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
