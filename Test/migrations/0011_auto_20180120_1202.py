# Generated by Django 2.0.1 on 2018-01-20 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0010_auto_20180120_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='char_inst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='Test.CharInst'),
        ),
    ]