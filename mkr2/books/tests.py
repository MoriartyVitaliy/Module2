from django.test import TestCase
from books.models import Author, Book

# Create your tests here.

class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(first_name="George", last_name="Orwell")
        Author.objects.create(first_name="Aldous", last_name="Huxley")

    def test_author_full_name(self):
        """Author full name is correctly displayed"""
        orwell = Author.objects.get(first_name="George")
        huxley = Author.objects.get(first_name="Aldous")
        self.assertEqual(orwell.full_name(), 'George Orwell')
        self.assertEqual(huxley.full_name(), 'Aldous Huxley')


#Test for books
class BookTestCase(TestCase):
    def setUp(self):
        author = Author.objects.create(first_name="George", last_name="Orwell")
        Book.objects.create(title="1984", author=author)
        Book.objects.create(title="Animal Farm", author=author)

    def test_book_title(self):
        """Book title is correctly displayed"""
        book1 = Book.objects.get(title="1984")
        book2 = Book.objects.get(title="Animal Farm")
        self.assertEqual(book1.title, '1984')
        self.assertEqual(book2.title, 'Animal Farm')
