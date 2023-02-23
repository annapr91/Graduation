# Generated by Django 4.1.5 on 2023-02-14 21:12

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Номер телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Имейл')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='KIDCHOICE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=154, unique=True)),
            ],
            options={
                'verbose_name': 'Допалнительный кружок',
                'verbose_name_plural': 'Допалнительные кружки',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Kindergarden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_places', models.BooleanField(default=True, verbose_name='Свободные места')),
                ('area', models.CharField(choices=[('Lasnamae', 'Lasnamae'), ('Kristiine', 'Kristiine'), ('Noome', 'Noome')], max_length=30, verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Детский садик',
                'verbose_name_plural': 'Детские садики',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('id_number', models.CharField(max_length=20)),
                ('ochered', models.IntegerField(default=None, null=True)),
                ('det_sads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.kindergarden', verbose_name='Детские сады')),
                ('roditeli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Родители')),
            ],
            options={
                'verbose_name': 'Ребенок',
                'verbose_name_plural': 'Дети',
            },
        ),
        migrations.CreateModel(
            name='KindergardenTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('photo', models.ImageField(blank=True, max_length=50, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('num_free_places', models.IntegerField(default=0, null=True, verbose_name='Количество свободных мест')),
                ('num_register_child', models.IntegerField(default=0, null=True, verbose_name='Кол-во заргис. детей')),
                ('addition', models.ManyToManyField(to='account.kidchoice', verbose_name='Доп. кружки')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='account.kindergarden')),
            ],
            options={
                'verbose_name': 'Детский садик Translation',
                'db_table': 'account_kindergarden_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
