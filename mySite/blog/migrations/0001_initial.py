# Generated by Django 5.0.1 on 2024-07-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('signature', models.CharField(default="Developers are not born, they're made.", max_length=140)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
