# Generated by Django 5.0.3 on 2024-05-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_toiletreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='toiletreview',
            name='notes',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
