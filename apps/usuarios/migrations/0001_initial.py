# Generated by Django 5.0.4 on 2024-04-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='E-mail do usuário')),
                ('is_active', models.BooleanField(default=True, verbose_name='Usuário está ativo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Equipe de desenvolvimento')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='É um Superusuario')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')),
                ('last_modified_date', models.DateTimeField(auto_now=True, verbose_name='Ultima Modificação')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'Usuario',
            },
        ),
    ]
