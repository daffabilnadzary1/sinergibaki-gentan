# Generated by Django 4.0.1 on 2022-07-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_activity_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(default='', upload_to='featured_image/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
