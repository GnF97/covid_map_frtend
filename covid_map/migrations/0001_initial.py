# Generated by Django 3.2.5 on 2021-07-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=4)),
                ('patient_count', models.IntegerField(max_length=10)),
            ],
        ),
    ]