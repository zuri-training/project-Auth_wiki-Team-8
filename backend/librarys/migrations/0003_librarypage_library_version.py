# Generated by Django 4.0.6 on 2022-08-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarys', '0002_alter_librarypage_example_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarypage',
            name='library_version',
            field=models.CharField(default='version-1.0.5', max_length=50),
            preserve_default=False,
        ),
    ]