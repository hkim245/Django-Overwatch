# Generated by Django 2.1.1 on 2020-01-15 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='createTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BattleTag_1', models.CharField(max_length=100)),
                ('BattleTag_2', models.CharField(max_length=100)),
                ('BattleTag_3', models.CharField(max_length=100)),
                ('BattleTag_4', models.CharField(max_length=100)),
                ('BattleTag_5', models.CharField(max_length=100)),
                ('BattleTag_6', models.CharField(max_length=100)),
                ('Hero_1', models.CharField(max_length=50)),
                ('Hero_2', models.CharField(max_length=50)),
                ('Hero_3', models.CharField(max_length=50)),
                ('Hero_4', models.CharField(max_length=50)),
                ('Hero_5', models.CharField(max_length=50)),
                ('Hero_6', models.CharField(max_length=50)),
                ('img_1', models.CharField(max_length=100)),
                ('img_2', models.CharField(max_length=100)),
                ('img_3', models.CharField(max_length=100)),
                ('img_4', models.CharField(max_length=100)),
                ('img_5', models.CharField(max_length=100)),
                ('img_6', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeamList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teamlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='createteam',
            name='teamlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedjangoapp.TeamList'),
        ),
    ]