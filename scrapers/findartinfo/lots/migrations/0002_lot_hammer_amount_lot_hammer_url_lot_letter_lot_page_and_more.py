# Generated by Django 4.1.4 on 2022-12-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='hammer_amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lot',
            name='hammer_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lot',
            name='letter',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='lot',
            name='page',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lot',
            name='photo_amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lot',
            name='photo_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lot',
            name='sign_amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lot',
            name='sign_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]