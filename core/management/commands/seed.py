from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Populate the database with all seeders'

    seeders = [
        'SuperUserSeeder',
    ]

    def handle(self, *args, **kwargs):
        confirm = input("Are you sure you want to proceed with seeding? [y/N]: ")
        if confirm.lower() != 'y':
            self.stdout.write(self.style.ERROR('Seeding canceled.'))
            return

        self.stdout.write(self.style.HTTP_SERVER_ERROR('Starting seeding... '))
        self.stdout.write('')
        
        for seeder in self.seeders:
            call_command(f'{seeder}')
            self.stdout.write('')
        
        self.stdout.write(self.style.HTTP_SERVER_ERROR('All seeders have been executed!'))