# Generated by Django 2.0.5 on 2018-05-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_title', models.CharField(max_length=100)),
                ('img_src', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]