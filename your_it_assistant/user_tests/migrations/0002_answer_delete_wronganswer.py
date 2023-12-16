# Generated by Django 4.2.7 on 2023-12-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_tests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wrong_answer', models.TextField()),
                ('explanation', models.TextField()),
                ('right', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='WrongAnswer',
        ),
    ]
