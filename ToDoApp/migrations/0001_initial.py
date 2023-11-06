# Generated by Django 4.2.6 on 2023-11-03 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ToDolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2023-11-03')),
                ('expiration_date', models.DateField(default='2023-11-03')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDoApp.category')),
            ],
        ),
    ]