# Generated by Django 3.0.9 on 2020-11-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('describtion', models.TextField()),
                ('image', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
