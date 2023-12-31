# Generated by Django 4.2.6 on 2023-10-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0003_alter_authors_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='fullname',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='quote',
            field=models.CharField(unique=True),
        ),
    ]
