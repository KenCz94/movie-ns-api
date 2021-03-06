# Generated by Django 4.0.1 on 2022-02-01 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Add a movie genre', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('produced_by', models.CharField(blank=True, max_length=100)),
                ('release_date', models.IntegerField(blank=True, null=True)),
                ('fandango_url', models.CharField(blank=True, max_length=255, null=True)),
                ('poster_url', models.URLField(blank=True, max_length=255, null=True)),
                ('created_by', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('genre', models.ManyToManyField(help_text='Select a genre', to='movie_ns_api.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_ns_api.movie')),
            ],
            options={
                'unique_together': {('movie', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_ns_api.movie')),
            ],
            options={
                'unique_together': {('movie', 'user')},
            },
        ),
    ]
