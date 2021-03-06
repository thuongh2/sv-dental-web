# Generated by Django 4.0.6 on 2022-07-07 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svdental', '0002_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
