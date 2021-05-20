# Generated by Django 3.2.3 on 2021-05-19 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp_username', models.CharField(help_text='Wikipedia username', max_length=235)),
                ('wp_registered', models.DateField(blank=True, help_text='Date registered at Wikipedia', null=True)),
                ('wp_sub', models.IntegerField(help_text='Wikipedia user ID', unique=True)),
                ('wp_editcount', models.IntegerField(help_text='Number of edits user has made')),
                ('wp_blocked', models.BooleanField(default=False, help_text='Does the user have any blocks on Wikipedia?')),
                ('app_username', models.CharField(help_text='WikiMentor generated username', max_length=235, unique=True)),
                ('email', models.CharField(blank=True, help_text='User provided email to send notifications', max_length=235, null=True)),
                ('number_of_blocks', models.IntegerField(help_text='Number of blocks the user has accumulated in WikiMentor')),
                ('blocked_by', models.ManyToManyField(help_text='A list of users that have blocked this user', related_name='blockedby', to='users.UserProfile')),
                ('has_blocked', models.ManyToManyField(help_text='A list of users this user has blocked', related_name='hasblocked', to='users.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user profile',
                'verbose_name_plural': 'user profiles',
            },
        ),
    ]
