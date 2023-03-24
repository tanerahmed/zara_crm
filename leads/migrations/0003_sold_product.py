# Generated by Django 3.1.4 on 2023-03-18 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.product'),
        ),
    ]