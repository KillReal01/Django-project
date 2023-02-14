from django.test import TestCase

# Create your tests here.

from django_seed import Seed

seeder = Seed.seeder()

from models import *

seeder.add_entity(Employee, 5)

inserted_pks = seeder.execute()
