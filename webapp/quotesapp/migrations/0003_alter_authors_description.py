# Generated by Django 4.2.6 on 2023-10-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0002_tag_remove_quotes_tags_quotes_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='description',
            field=models.CharField(),
        ),
    ]
