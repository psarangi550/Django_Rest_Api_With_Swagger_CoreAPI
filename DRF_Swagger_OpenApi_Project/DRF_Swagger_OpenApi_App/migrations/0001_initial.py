# Generated by Django 4.0 on 2021-12-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WFMTTASKMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_number', models.CharField(max_length=100)),
                ('sne_id', models.IntegerField()),
                ('scheme_number', models.IntegerField()),
                ('trs', models.CharField(max_length=10)),
                ('estimate', models.CharField(max_length=10)),
            ],
        ),
    ]
