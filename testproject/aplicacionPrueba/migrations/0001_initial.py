# Generated by Django 2.1.3 on 2018-11-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]