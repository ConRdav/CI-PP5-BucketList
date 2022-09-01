# Generated by Django 3.2 on 2022-08-31 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventures', '0003_excursion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.RemoveField(
            model_name='excursion',
            name='category',
        ),
        migrations.AddField(
            model_name='excursion',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adventures.country'),
        ),
        migrations.AlterField(
            model_name='adventure',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adventures.country'),
        ),
    ]