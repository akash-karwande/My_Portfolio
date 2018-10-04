import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'Don.settings')

import django
django.setup()

from Mission.models import Don_info
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = Don_info.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
    print('populating Databases')
    populate(30)
    print("Complete")
