# Generated by Django 5.0.7 on 2025-01-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_category_slug'),
        ('transactions', '0002_transaction_book_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='book',
        ),
        migrations.AddField(
            model_name='transaction',
            name='book',
            field=models.ManyToManyField(blank=True, null=True, related_name='viewer', to='books.book'),
        ),
    ]
