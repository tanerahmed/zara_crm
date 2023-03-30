# Generated by Django 3.1.4 on 2023-03-30 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0008_sold_sold'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='company',
        ),
        migrations.AddField(
            model_name='client',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.company'),
        ),
    ]
