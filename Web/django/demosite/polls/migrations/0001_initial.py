# Generated by Django 3.1.2 on 2020-10-22 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='问题')),
                ('pub_date', models.DateTimeField(verbose_name='发布时间')),
            ],
            options={
                'verbose_name_plural': '问题',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='选项')),
                ('votes', models.IntegerField(default=0, help_text='投票的数量', verbose_name='票数')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionProxy',
            fields=[
            ],
            options={
                'ordering': ['pub_date'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('polls.question',),
        ),
    ]
