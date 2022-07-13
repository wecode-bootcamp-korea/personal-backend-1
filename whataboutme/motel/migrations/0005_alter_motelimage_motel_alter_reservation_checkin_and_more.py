# Generated by Django 4.0.6 on 2022-07-12 07:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('motel', '0004_alter_motelimage_motel_alter_reservation_checkin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motelimage',
            name='motel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motelimage', to='motel.motel'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkin',
            field=models.DateField(default=datetime.datetime(2022, 7, 12, 7, 53, 34, 770922, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservationroom', to='motel.room'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservationuser', to='user.user'),
        ),
        migrations.AlterField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomimages', to='motel.room'),
        ),
        migrations.AlterField(
            model_name='roomtheme',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomtheme', to='motel.room'),
        ),
        migrations.AlterField(
            model_name='roomtheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themeroom', to='motel.theme'),
        ),
    ]
