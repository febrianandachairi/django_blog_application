# Generated by Django 4.1.3 on 2022-12-11 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_blogmodel_beritamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beritamodel',
            name='image',
            field=models.ImageField(upload_to='berita'),
        ),
    ]