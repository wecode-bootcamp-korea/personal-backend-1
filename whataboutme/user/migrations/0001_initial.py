# Generated by Django 4.0.6 on 2022-07-11 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kakao_id', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
