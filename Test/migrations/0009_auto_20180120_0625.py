# Generated by Django 2.0.1 on 2018-01-20 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0008_remove_charinst_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charinst',
            name='char',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char_insts', to='Test.Character'),
        ),
    ]