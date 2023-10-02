# Generated by Django 4.2.5 on 2023-10-01 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_groups_alter_user_user_permissions'),
        ('pets', '0002_petprice_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='breed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pets.petbreed'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
        ),
    ]