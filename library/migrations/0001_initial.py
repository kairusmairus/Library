# Generated by Django 3.1.7 on 2021-02-27 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField()),
                ('birth_place', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('written_date', models.DateField()),
                ('pages_num', models.IntegerField()),
                ('content', models.TextField()),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
        ),
    ]