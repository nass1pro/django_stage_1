# Generated by Django 2.2.1 on 2019-06-19 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questi', '0010_score_s_prof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='name_classe',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='questi.classe'),
        ),
    ]