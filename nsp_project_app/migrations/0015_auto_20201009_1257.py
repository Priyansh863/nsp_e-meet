# Generated by Django 2.2.5 on 2020-10-09 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nsp_project_app', '0014_auto_20201009_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nsp_project_app.User_info'),
        ),
    ]
