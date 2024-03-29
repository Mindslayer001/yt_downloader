# Generated by Django 5.0.2 on 2024-02-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yt_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('thumbnail', models.URLField()),
                ('length', models.BigIntegerField()),
                ('views', models.IntegerField()),
            ],
        ),
    ]
