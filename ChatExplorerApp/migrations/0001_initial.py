# Generated by Django 4.1.12 on 2023-10-31 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionId', models.CharField(max_length=100)),
                ('userId', models.CharField(max_length=100)),
                ('messageId', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
            ],
        ),
    ]
