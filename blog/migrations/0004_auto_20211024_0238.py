# Generated by Django 3.2.5 on 2021-10-23 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comments_recomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='catagory',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(default='defthumb.jpg', upload_to=''),
        ),
    ]
