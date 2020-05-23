# Generated by Django 3.0.6 on 2020-05-23 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='technology',
        ),
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, upload_to='mainpage/images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_link',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]
