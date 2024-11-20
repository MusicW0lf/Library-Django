from django.core.management.base import BaseCommand
from book.models import Book
from author.models import Author

class Command(BaseCommand):
    help = 'Populate the database with authors and books.'

    def handle(self, *args, **kwargs):
        authors_data = [
            {'name': 'George', 'surname': 'Orwell'},
            {'name': 'Harper', 'surname': 'Lee'},
            {'name': 'F. Scott', 'surname': 'Fitzgerald'},
            {'name': 'Jane', 'surname': 'Austen'},
            {'name': 'J.D.', 'surname': 'Salinger'},
            {'name': 'Herman', 'surname': 'Melville'},
            {'name': 'Leo', 'surname': 'Tolstoy'},
            {'name': 'Aldous', 'surname': 'Huxley'},
            {'name': 'J.R.R.', 'surname': 'Tolkien'},
            {'name': 'Ray', 'surname': 'Bradbury'},
        ]

        authors = []
        for author_data in authors_data:
            author = Author.objects.create(**author_data)
            authors.append(author)

        books_data = [
            {'name': '1984', 'description': 'A dystopian novel by George Orwell.', 'count': 5, 'authors': [authors[0]]},
            {'name': 'To Kill a Mockingbird', 'description': 'A novel by Harper Lee about racial injustice.', 'count': 3, 'authors': [authors[1]]},
            {'name': 'The Great Gatsby', 'description': 'A novel by F. Scott Fitzgerald set in the Jazz Age.', 'count': 7, 'authors': [authors[2]]},
            {'name': 'Pride and Prejudice', 'description': 'A romantic novel by Jane Austen.', 'count': 4, 'authors': [authors[3]]},
            {'name': 'The Catcher in the Rye', 'description': 'A novel by J.D. Salinger about teenage alienation.', 'count': 2, 'authors': [authors[4]]},
            {'name': 'Moby-Dick', 'description': 'A novel by Herman Melville about the quest for revenge against a whale.', 'count': 6, 'authors': [authors[5]]},
            {'name': 'War and Peace', 'description': 'A historical novel by Leo Tolstoy.', 'count': 1, 'authors': [authors[6]]},
            {'name': 'Brave New World', 'description': 'A dystopian novel by Aldous Huxley.', 'count': 8, 'authors': [authors[7]]},
            {'name': 'The Hobbit', 'description': 'A fantasy novel by J.R.R. Tolkien.', 'count': 10, 'authors': [authors[8]]},
            {'name': 'Fahrenheit 451', 'description': 'A dystopian novel by Ray Bradbury about censorship.', 'count': 4, 'authors': [authors[9]]},
        ]

        for book_data in books_data:
            book = Book.objects.create(**{key: value for key, value in book_data.items() if key != 'authors'})
            book.authors.set(book_data['authors'])
            book.save()

        self.stdout.write(self.style.SUCCESS('Database populated with authors and books!'))
