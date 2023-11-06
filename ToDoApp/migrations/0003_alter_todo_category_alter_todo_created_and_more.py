# Generated by Django 4.2.6 on 2023-11-06 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0002_rename_todolist_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='ToDoApp.category'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateField(default='2023-11-06'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='expiration_date',
            field=models.DateField(default='2023-11-06'),
        ),
    ]