# Generated by Django 4.0.3 on 2022-04-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='Images/', verbose_name='Image')),
                ('describe', models.TextField(null=True, verbose_name='Description')),
            ],
        ),
    ]
