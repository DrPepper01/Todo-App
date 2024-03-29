# Generated by Django 4.2.6 on 2023-11-06 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0003_alter_todo_category_alter_todo_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='ToDoApp.category'),
        ),
    ]
