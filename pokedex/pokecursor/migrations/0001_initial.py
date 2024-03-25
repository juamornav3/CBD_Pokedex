# Generated by Django 4.1.13 on 2024-03-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type_1', models.CharField(max_length=255)),
                ('type_2', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('sp_atk', models.IntegerField()),
                ('sp_def', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('generation', models.IntegerField()),
                ('legendary', models.BooleanField()),
            ],
        ),
    ]
