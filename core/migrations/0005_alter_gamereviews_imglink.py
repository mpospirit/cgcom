# Generated by Django 5.0.3 on 2024-03-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_gamereviews_imglink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereviews',
            name='imgLink',
            field=models.CharField(default=25, max_length=255),
            preserve_default=False,
        ),
    ]
