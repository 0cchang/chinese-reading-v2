from django.core.management.base import BaseCommand
from mcq.models import omegaCharacter
from mcq.data.omega import OMEGA

class Command(BaseCommand):
    help = 'Load omega mapping from OMEGA'

    def handle(self, *args, **kwargs):
        # Clear the existing records
        omegaCharacter.objects.all().delete()
        
        # Create a sorted, unique set of characters
        characters = "".join(sorted(set(OMEGA.strip())))
        
        # Prepare objects for bulk creation
        omega_objects = [omegaCharacter(character=char, unique_id=index) for index, char in enumerate(characters)]
        
        # Insert all objects in one transaction
        omegaCharacter.objects.bulk_create(omega_objects)

        self.stdout.write(self.style.SUCCESS('Successfully loaded character mapping'))
