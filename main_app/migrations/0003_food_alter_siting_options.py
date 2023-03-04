# Generated by Django 4.1.7 on 2023-03-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_siting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('attracted_birds', models.TextField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='siting',
            options={'ordering': ['-date']},
        ),
    ]