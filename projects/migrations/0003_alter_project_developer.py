# Generated by Django 3.2.5 on 2021-08-11 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0002_auto_20210811_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='developer',
            field=models.ForeignKey(blank=True, max_length=150, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]