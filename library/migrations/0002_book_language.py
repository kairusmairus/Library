# Generated by Django 3.1.7 on 2021-02-27 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='Русский', max_length=100),
        ),
    ]
