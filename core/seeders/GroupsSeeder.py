from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from django.contrib.auth.models import Group

class GroupsSeeder(BaseSeeder):
    
    @property
    def seeder_name(self):
        return 'GroupsSeeder'

    GROUPS = [
        'Admins',
        'Readers'
    ]

    def seed(self):
        for group in self.GROUPS:
            if not Group.objects.filter(name=group).exists():
                Group.objects.create(name=group)
                self.succes(f'Group {group} created')
            else:
                self.error(f'Group {group} already exists')