# Generated by Django 3.2.4 on 2021-06-28 13:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_history_sorted_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='sorted_cards_date',
        ),
        migrations.AddField(
            model_name='history',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='dailysortedcards',
            name='sorted_cards_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
