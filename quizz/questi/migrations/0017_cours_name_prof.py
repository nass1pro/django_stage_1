# Generated by Django 2.2.1 on 2019-06-19 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questi', '0016_remove_cours_name_prof'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='name_prof',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='questi.prof'),
        ),
    ]