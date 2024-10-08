# Generated by Django 5.1.1 on 2024-09-17 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SingleCharacterQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_word', models.CharField(max_length=1, unique=True)),
                ('pinyin', models.CharField(max_length=10)),
                ('english', models.CharField(max_length=200)),
                ('answer', models.IntegerField()),
            ],
        ),
    ]
