# Generated by Django 3.0.5 on 2020-06-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeongsi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeongsi',
            name='gun',
            field=models.CharField(choices=[('가군', '가군'), ('나군', '나군'), ('다군', '다군'), ('군외', '군외')], max_length=7, verbose_name='군'),
        ),
    ]
