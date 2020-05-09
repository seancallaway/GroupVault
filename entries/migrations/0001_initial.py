# Generated by Django 3.0.6 on 2020-05-08 21:48

from django.db import migrations, models
import django.db.models.deletion
import entries.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_folders', to='entries.Folder')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('login', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('_iv', models.BinaryField(default=entries.models.generate_iv_value, max_length=16)),
                ('_secret', models.BinaryField(blank=True, max_length=528)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='entries.Folder')),
            ],
        ),
    ]