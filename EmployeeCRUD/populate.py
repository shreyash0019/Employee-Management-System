import os
import django
from faker import Faker
from random import randint

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbvcrudproject.settings')
django.setup()  # Initialize Django environment

from testapp.models import Employee

faker = Faker()

def populate(n):
    for _ in range(n):
        fno = randint(1001, 9999)
        fname = faker.name()
        fesal = randint(10000, 30000)
        feaddr = faker.city()
        Employee.objects.get_or_create(
            eno=fno,
            ename=fname,
            esal=fesal,
            eaddr=feaddr
        )

if __name__ == "__main__":
    n = int(input("Enter the number of employees: "))
    populate(n)
    print(f"{n} Records Inserted Successfully!")
