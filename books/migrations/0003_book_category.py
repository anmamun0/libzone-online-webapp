# Generated by Django 5.0.7 on 2025-01-05 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.category'),
        ),
    ]