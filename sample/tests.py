from django.test import TestCase
from models import Person
from django.contrib.auth.models import User

# Create your tests here.


class PersonTestCase(TestCase):

    def setUp(self):
        auth = User.objects.create(username="Test", email="test@tests.com")
        Person.objects.create(
            first_name="Test", last_name="last_name", user=auth)

    def test_person(self):
        name = Person.objects.get(first_name="Test")
