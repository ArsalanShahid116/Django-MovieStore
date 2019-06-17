# Generated by Django 2.2.1 on 2019-06-17 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import moviesApp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moviesApp', '0003_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.SmallIntegerField(choices=[(1, 'LIKE'), (-1, 'DISLIKE')]),
        ),
        migrations.CreateModel(
            name='MovieImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=moviesApp.models.movie_directory_path_with_uuid)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviesApp.myMovie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
