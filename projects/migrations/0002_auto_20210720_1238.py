# Generated by Django 3.2.2 on 2021-07-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]