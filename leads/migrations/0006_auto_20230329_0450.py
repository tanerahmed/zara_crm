# Generated by Django 3.1.4 on 2023-03-29 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20230321_0736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статия', 'verbose_name_plural': 'Статии'},
        ),
        migrations.AddField(
            model_name='sold',
            name='marsh',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
