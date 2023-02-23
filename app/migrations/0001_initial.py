# Generated by Django 2.2 on 2023-02-22 23:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('short_url', models.URLField(blank=True)),
                ('token', models.CharField(max_length=6)),
                ('clicks_count', models.PositiveIntegerField(default=0)),
                ('max_clicks', models.PositiveIntegerField(default=0)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Link')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]