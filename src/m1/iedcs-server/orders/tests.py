from django.test import TestCase
from .models import Book
from rest_framework.test import APIClient
from django.core.files.storage import default_storage
from iedcs.settings import BASE_DIR
from authentication.models import Account


class OrdersTestCase(TestCase):
    def setUp(self):
        self.b1 = Book.objects.create(name="Seguranca em Redes Informaticas", author="Andre Zuquete",
                                      production_date="2013-05-01",
                                      original_file=default_storage.path(BASE_DIR + '/media/books/pg6598.txt'))

        self.b2 = Book.objects.create(name="Cyclopedia of Telephony & Telegraphy Vol. 2",
                                      author="Kempster Miller et. al.",
                                      production_date="2010-08-15",
                                      original_file=default_storage.path(BASE_DIR + '/media/books/pg33437.txt'))

        self.a1 = Account.objects.create(email='test@test.com', username='test', first_name='unit', last_name='test')

    def test_books(self):
        client = APIClient()
        client.force_authenticate(user=self.a1)

        url = "/api/v1/orders/"
        data = {'books_identifier': [self.b1.identifier, self.b2.identifier]}
        response = client.post(path=url, data=data)
        res = response.data
        print res
