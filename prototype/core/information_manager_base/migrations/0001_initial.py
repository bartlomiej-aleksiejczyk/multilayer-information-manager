# Generated by Django 4.2.7 on 2023-11-09 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InformationComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('informationcomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='information_manager_base.informationcomponent')),
                ('due_date', models.DateTimeField()),
            ],
            bases=('information_manager_base.informationcomponent',),
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('informationcomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='information_manager_base.informationcomponent')),
                ('description', models.TextField()),
            ],
            bases=('information_manager_base.informationcomponent',),
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('informationcomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='information_manager_base.informationcomponent')),
                ('knowledge_base', models.TextField()),
            ],
            bases=('information_manager_base.informationcomponent',),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('informationcomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='information_manager_base.informationcomponent')),
                ('scheduled_time', models.DateTimeField()),
            ],
            bases=('information_manager_base.informationcomponent',),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('informationcomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='information_manager_base.informationcomponent')),
                ('text_content', models.TextField()),
            ],
            bases=('information_manager_base.informationcomponent',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('informationcomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='information_manager_base.informationcomponent')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            bases=('information_manager_base.informationcomponent',),
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('informationcomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='information_manager_base.informationcomponent')),
                ('is_completed', models.BooleanField(default=False)),
            ],
            bases=('information_manager_base.informationcomponent',),
        ),
    ]
