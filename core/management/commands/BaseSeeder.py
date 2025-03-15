from abc import ABC, abstractmethod
from django.core.management.base import BaseCommand

class BaseSeeder(BaseCommand, ABC):
    @property
    @abstractmethod
    def seeder_name(self):
        pass

    help = f'Seed database with {seeder_name} data'

    @abstractmethod
    def seed(self):
        pass

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING(f'Executing {self.seeder_name}...'))
        try:
            self.seed()
            self.stdout.write(self.style.SUCCESS(f'Successfully seeded {self.seeder_name}!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error executing {self.seeder_name}: {e}'))