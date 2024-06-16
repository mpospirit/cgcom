# Generated by Django 5.0.3 on 2024-05-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_albumreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bookName', models.CharField(max_length=255)),
                ('authorName', models.CharField(max_length=255)),
                ('imgLink', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('overallRating', models.IntegerField()),
            ],
            options={
                'db_table': 'BookReview',
            },
        ),
    ]