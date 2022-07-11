# Generated by Django 4.0.6 on 2022-07-11 05:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('motel', '0003_alter_motel_latitude_alter_motel_longitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motelimage',
            name='motel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motel_image', to='motel.motel'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkin',
            field=models.DateField(default=datetime.datetime(2022, 7, 11, 5, 55, 32, 817543, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_room', to='motel.room'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_user', to='user.user'),
        ),
        migrations.AlterField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_images', to='motel.room'),
        ),
    ]
