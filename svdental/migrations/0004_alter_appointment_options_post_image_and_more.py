# Generated by Django 4.0.6 on 2022-07-10 10:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svdental', '0003_appointment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-created_on', 'active']},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='courses/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
