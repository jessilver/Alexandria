from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .BaseSeeder import BaseSeeder

class Command(BaseSeeder):
    @property
    def seeder_name(self):
        return 'SuperUserSeeder'

    def seed(self):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='123456789',
                first_name='Admin',
                last_name='User'
            )
        else:
            raise Exception('Superuser already exists')