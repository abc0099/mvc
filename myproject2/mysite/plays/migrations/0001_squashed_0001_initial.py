# Generated by Django 2.2.3 on 2019-08-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('plays', '0001_initial')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.IntegerField(default=0)),
                ('attack', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.IntegerField(default=0)),
                ('attack', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
