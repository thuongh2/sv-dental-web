# Generated by Django 4.0.6 on 2022-07-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svdental', '0004_alter_appointment_options_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='uploads/%Y/%m'),
        ),
    ]