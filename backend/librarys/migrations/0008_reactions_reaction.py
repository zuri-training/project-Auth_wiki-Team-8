# Generated by Django 4.0.6 on 2022-08-15 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarys', '0007_reactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactions',
            name='reaction',
            field=models.CharField(default='like', max_length=10),
            preserve_default=False,
        ),
    ]
