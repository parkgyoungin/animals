# Generated by Django 2.2.2 on 2019-06-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('user_id', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=11)),
                ('gender', models.CharField(max_length=2)),
                ('animal_count', models.IntegerField()),
            ],
        ),
    ]