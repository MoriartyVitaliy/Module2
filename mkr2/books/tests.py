from django.test import TestCase
from books.models import Author, Book
from datetime import date
from decimal import Decimal

class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(name="George Orwell", bio="George Orwell was an English novelist and essayist.")
        Author.objects.create(name="Aldous Huxley", bio="Aldous Huxley was an English writer and philosopher.")

    def test_author_str(self):
        """Author string representation is the name"""
        orwell = Author.objects.get(name="George Orwell")
        huxley = Author.objects.get(name="Aldous Huxley")
        self.assertEqual(str(orwell), 'George Orwell')
        self.assertEqual(str(huxley), 'Aldous Huxley')

class BookTestCase(TestCase):
    def setUp(self):
        orwell = Author.objects.create(name="George Orwell", bio="George Orwell was an English novelist and essayist.")
        self.book1 = Book.objects.create(title="1984", description="A dystopian novel", publication_date=date(1949, 6, 8), price=Decimal('9.99'))
        self.book2 = Book.objects.create(title="Animal Farm", description="A political allegory", publication_date=date(1945, 8, 17), price=Decimal('7.99'))
        self.book1.authors.add(orwell)
        self.book2.authors.add(orwell)

    def test_book_str(self):
        """Book string representation is the title"""
        self.assertEqual(str(self.book1), '1984')
        self.assertEqual(str(self.book2), 'Animal Farm')

    def test_book_author_relationship(self):
        """Books have the correct author"""
        orwell = Author.objects.get(name="George Orwell")
        self.assertIn(orwell, self.book1.authors.all())
        self.assertIn(orwell, self.book2.authors.all())
