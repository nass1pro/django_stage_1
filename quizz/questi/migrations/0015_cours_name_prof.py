# Generated by Django 2.2.1 on 2019-06-19 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questi', '0014_auto_20190619_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='name_prof',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='questi.prof'),
        ),
    ]