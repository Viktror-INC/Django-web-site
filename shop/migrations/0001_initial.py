# Generated by Django 3.0.4 on 2020-04-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('availibility', models.BooleanField(default=True)),
                ('group', models.CharField(choices=[('notebook', 'notebook'), ('mobile', 'mobile'), ('pc', 'pc'), ('tablet', 'tablet')], default='mobile', max_length=20)),
                ('image', models.ImageField(default='no_image.jpg', upload_to='product_image')),
            ],
        ),
    ]