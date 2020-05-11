# Generated by Django 2.2.7 on 2020-03-17 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OmniDB_app', '0006_auto_20200317_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='connection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
