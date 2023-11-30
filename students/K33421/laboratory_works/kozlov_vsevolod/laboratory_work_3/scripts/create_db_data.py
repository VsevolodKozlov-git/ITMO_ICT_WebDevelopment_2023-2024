from datetime import datetime
from lab3 import models
from random import randrange, choice, seed


def convert_to_models(model_class, model_dicts):
    for i in range(len(model_dicts)):
        entity = model_class(**model_dicts[i])
        entity.save()
        model_dicts[i] = entity


def get_by_mod(choices, i):
    return choices[i % len(choices)]


def delete_all_data():
    models_seq = [
        models.ReaderBookHistory,
        models.ReaderRoomHistory,
        models.Reader,
        models.BookInstance,
        models.Room,
        models.BookAuthors,
        models.Book,
        models.Section,
        models.Publisher,
        models.Author,

    ]
    for model in models_seq:
        model.objects.all().delete()

def run():
    delete_all_data()
    # print(models.Book.objects.all())
    authors = [
        {'first_name': 'Vsevolod', 'last_name': 'Kozlov'},
        {'first_name': 'Ivan', 'last_name': 'Pupkin'},
        {'first_name': 'Anton', 'last_name': 'Votykov'},
        {'first_name': 'Eduard', 'last_name': 'Surikov'}
    ]
    convert_to_models(models.Author, authors)

    publishers = [
        {'name': 'itmo publishing'},
        {'name': "O'relly"},
        {'name': 'Anton publishing'}
    ]
    convert_to_models(models.Publisher, publishers)

    sections = [
        {'name': 'science'},
        {'name': 'pulp fiction'},
        {'name': 'non pulp'}
    ]
    convert_to_models(models.Section, sections)


    books = []
    years_to_choose = [2002, 2010, 2021, 1998]
    for i in range(20):
        title = f'BookTitle{i}'
        section = get_by_mod(sections, i)
        publisher = get_by_mod(publishers, i)
        year = get_by_mod(years_to_choose, i)
        books.append({
            'title': title,
            'section': section,
            'publisher': publisher,
            'year': year
        })
    convert_to_models(models.Book, books)

    book_author = []
    for i in range(20):
        for j in range(i%2+1):
            book = books[i]
            author = get_by_mod(authors, i+j)
            book_author.append({
                'book': book,
                'author': author
            })
    convert_to_models(models.BookAuthors, book_author)

    rooms = [
        {'name':'room1', 'capacity': 100},
        {'name': 'room2', 'capacity': 100}
    ]
    convert_to_models(models.Room, rooms)

    book_instances = []
    qualities = ['b', 'g', 'n']
    # Для каждой книги 4 экземпляра
    # Первые 10 в 1-й зал
    # Вторые 10 во 2-й зал
    for book_ind in range(20):
        for j in range(4):
            code = f'000{book_ind}{j}'
            book = books[book_ind]
            room = rooms[book_ind//10]
            quality = get_by_mod(qualities, j)
            book_instances.append({
                'code': code,
                'book': book,
                'room': room,
                'quality': quality
            })
    convert_to_models(models.BookInstance, book_instances)

    readers = []
    dates = [datetime(year=2021, day=1, month=1),
             datetime(year=2023, day=1, month=1)]
    birth_dates = [datetime(year=1980, day=1, month=1),
                   datetime(year=2010, day=1, month=1),
                   datetime(year=2008, day=1, month=1)]

    education_types = ('b','m', 'h', 'd')
    for i in range(20):
        reader_number = f'0000{i}'
        registration_date = dates[i // 10]
        active = True
        first_name = f'Name{i}'
        last_name = f'Lastname{i}'
        passport_number = f'0001000{i//10}{i%10}'
        birth_date = get_by_mod(birth_dates, i)
        address = f'50 let vlksm 1{i}'
        mobile_number = f'+799646450{i//10}{i%10}'
        education = get_by_mod(education_types, i)
        readers.append({
            'reader_number': reader_number,
            'registration_date': registration_date,
            'active': active,
            'first_name': first_name,
            'last_name': last_name,
            'passport_number': passport_number,
            'birth_date': birth_date,
            'address': address,
            'mobile_number': mobile_number,
            'education': education
        })
    convert_to_models(models.Reader, readers)

    reader_room_history = []
    # Первые 10 в 1
    # Вторые 10 в 2
    for i in range(20):
        reader = readers[i]
        first_room = rooms[int(not (i // 10))]
        last_room = rooms[i // 10]
        first_date = datetime(year=2023, month=1, day=1)
        second_date = datetime(year=2023, month=6, day=1)
        reader_room_history.append({
            'reader': reader,
            'room': first_room,
            'start_date': first_date,
            'end_date': second_date,
        })
        reader_room_history.append({
            'reader': reader,
            'room': last_room,
            'start_date': second_date,
            'end_date': None
        })

    convert_to_models(models.ReaderRoomHistory, reader_room_history)

    reader_book_history = []

    # Каждому читателю дается от 1-го до 4-х экземпляров книги
    for reader_ind in range(20):
        for i in range(randrange(4)+1):
            book_instance = book_instances[reader_ind*4+i]
            reader = readers[reader_ind]
            start_date = datetime(year=2023, month=choice([11, 11, 11, 11, 9]), day=randrange(1, 20))
            end_date=None
            reader_book_history.append({
                'reader': reader,
                'book_instance': book_instance,
                'start_date': start_date,
                'end_date': end_date
            })
    convert_to_models(models.ReaderBookHistory, reader_book_history)

    # adding rare book
    book = models.Book(title='RareBook',
                       section=sections[0],
                       publisher=publishers[0],
                       year=2022)
    book.save()
    author = models.BookAuthors(book=book,
                                author=authors[0])
    author.save()
    book_instance = models.BookInstance(code='122022',
                                        book=book,
                                        room=rooms[1])
    book_instance.save()
    reader_book_history = models.ReaderBookHistory(
        book_instance=book_instance,
        reader=readers[-1],
        start_date=datetime(year=2023, month=10, day=20),
        end_date=None
    )
    reader_book_history.save()


