# Generated by Django 3.1.5 on 2021-01-25 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('pub_date', models.DateField(null=True, verbose_name='发表日期')),
                ('readcount', models.IntegerField(default=0, verbose_name='阅读量')),
                ('commentcount', models.IntegerField(default=0, verbose_name='评论量')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='删除')),
            ],
            options={
                'verbose_name': '图书',
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='性别')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='描述')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookinfo', verbose_name='图书名称')),
            ],
            options={
                'verbose_name': '人物信息',
                'db_table': 'peopleinfo',
            },
        ),
    ]
