# Generated by Django 2.2.1 on 2019-06-21 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questi', '0019_auto_20190621_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='cours',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questi.cours'),
        ),
    ]