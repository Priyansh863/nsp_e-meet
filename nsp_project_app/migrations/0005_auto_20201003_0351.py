# Generated by Django 2.2.5 on 2020-10-02 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nsp_project_app', '0004_auto_20201002_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='Post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nsp_project_app.post'),
        ),
    ]
