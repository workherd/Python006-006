# Generated by Django 2.2.13 on 2021-02-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_auto_20210228_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='owner',
            new_name='author_id',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='article',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='articleid',
        ),
        migrations.AlterField(
            model_name='articles',
            name='createtime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='文章创建时间'),
        ),
    ]
