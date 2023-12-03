# Generated by Django 3.2.23 on 2023-12-03 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('1', 'Todo'), ('2', 'Doing'), ('3', 'Done')], max_length=1)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]