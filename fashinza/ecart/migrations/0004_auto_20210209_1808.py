# Generated by Django 3.1.6 on 2021-02-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecart', '0003_auto_20210209_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecart',
            name='category_id',
        ),
        migrations.AddField(
            model_name='ecart',
            name='category_id',
            field=models.ManyToManyField(to='ecart.categorymap'),
        ),
    ]
