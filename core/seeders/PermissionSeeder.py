from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class PermissionSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'PermissionSeeder'

    PERMISSION = [
        'Test'
    ]

    def seed(self):
        for permission in self.PERMISSION:
            if not Permission.objects.filter(name=permission).exists():
                content_type = ContentType.objects.get_for_model(Permission)
                Permission.objects.create(name=permission, content_type=content_type)
                self.succes(f'Permission {permission} created')
            else:
                self.error(f'Permission {permission} already exists')