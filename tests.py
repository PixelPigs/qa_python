import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

# напиши свои тесты ниже
# чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тесты на метод add_new_book при добавлении новой книги
    def test_add_new_book_empty_value(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert collector.books_genre.get('Война и мир') == ''

    def test_add_new_book_add_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Унесенные ветром')
        collector.add_new_book('Унесенные ветром')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['Я', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_check_book_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre

    @pytest.mark.parametrize('name', ['', 'Клуб любителей книг и пирогов из картофельных очистков'])
    def test_add_new_book_negative_check_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # тесты на метод set_book_genre проверяем присвоение жанра книге
    def test_set_book_genre_check_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Темная башня')
        collector.set_book_genre('Темная башня', 'Фантастика')
        assert collector.books_genre.get('Темная башня') != ''

    def test_set_book_genre_check_not_add_incorrect_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Темная башня')
        collector.set_book_genre('Темная башня', 'Триллер')
        assert collector.books_genre.get('Темная башня') == ''

    # тест на метод get_book_genre проверяем жанр книги по его имени
    def test_get_book_genre_check_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.books_genre.get('Шерлок Холмс') == 'Детективы'

    # тесты на метод get_books_with_specific_genre проверяем список книг с определённым жанром
    def test_get_books_with_specific_genre_check_genre_add_list(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        books_with_specific_genre = collector.get_books_with_specific_genre('Мультфильмы')
        assert 'Колобок' in books_with_specific_genre

    def test_get_books_with_specific_genre_check_list(self):
        collector = BooksCollector()
        collector.add_new_book('Тонкое искусство пофигизма')
        collector.add_new_book('Двенадцать стульев')
        collector.set_book_genre('Тонкое искусство пофигизма', 'Комедии')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        books_with_specific_genre = collector.get_books_with_specific_genre('Комедии')
        assert books_with_specific_genre == ['Тонкое искусство пофигизма', 'Двенадцать стульев']

    # тест на метод get_books_genre проверяем словарь books_genre
    def test_get_books_genre_correct_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Аленький цветочек')
        collector.set_book_genre('Аленький цветочек', 'Мультфильмы')
        collector.add_new_book('Буратино')
        collector.set_book_genre('Буратино', 'Мультфильмы')
        books_genre = collector.get_books_genre()
        expected_dict = {'Аленький цветочек': 'Мультфильмы', 'Буратино': 'Мультфильмы'}
        assert books_genre == expected_dict

    # тест на метод get_books_for_children
    def test_get_books_for_children_check_book_for_children_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Аленький цветочек')
        collector.set_book_genre('Аленький цветочек', 'Мультфильмы')
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 1

    def test_get_books_for_children_check_book_age_rating_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Молчание ягнят')
        collector.set_book_genre('Молчание ягнят', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 0

    # тест на метод add_book_in_favorites
    def test_add_book_in_favorites_check_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_book_in_favorites('Оно')
        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_check_book_not_in_dict_not_add(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Унесенные ветром')
        assert len(collector.favorites) == 0

    # тест на метод delete_book_from_favorites
    def test_delete_book_from_favorites_check_book_remove_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector.favorites

    # тест на метод get_list_of_favorites_books
    def test_get_list_of_favorites_books_check_list_of_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Молчание ягнят')
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Молчание ягнят')
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Молчание ягнят', 'Оно']


