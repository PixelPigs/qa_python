# qa_python

Автоматизированные тесты для BooksCollector

1. На метод add_new_book

1.1 test_add_new_book_empty_value
Проверяем, что при добавлении книги в словарь, ключу (наименование) по умолчанию должно 
присваиваться пустое значение (жанр).

1.2 test_add_new_book_add_same_book
Проверяем, что книгу, которая существует в словаре нельзя добавить еще раз.

1.3 test_add_new_book_check_book_name
Проверяем допустимые граничные значения в названии книги, используя параметризацию

1.4 test_add_new_book_negative_check_name
Проверяем недопустимые граничные значения в названии книги, используя параметризацию


2. На set_book_genre

2.1 test_set_book_genre_check_genre
Проверяем, что книге, существующей в словаре, можно присвоить жанр (т.е. ожидаем не пустое значение ключа)

2.2 test_set_book_genre_check_not_add_incorrect_genre
Проверяем, что нельзя присвоить значение (жанр) ключу (наименованию) не из списка жанров


3. На метод get_book_genre

3.1 test_get_book_genre_check_genre
Проверяем, что можно добавить книге, существующей в словаре, жанр из доступных жанров


4. На метод get_books_with_specific_genre

4.1 test_get_books_with_specific_genre_check_genre_add_list
Проверяем, что наименование по запрашиваемому жанру попало в список 

4.2 test_get_books_with_specific_genre_check_list
Проверяем, что при запросе по определенному жанру в список добавились несколько наименований конкретного этого жанра


5. На метод get_books_genre

5.1 test_get_books_genre_correct_dict 
Проверяем, что при запросе метод должен вернуть словарь, связывающий названия книг с их жанрами


6. На метод get_books_for_children

6.1 test_get_books_for_children_check_book_for_children_in_list
Проверяем, что можно добавить в список детских книг, с жанром не сходящим в список с возрастным рейтингом

6.2 test_get_books_for_children_check_book_age_rating_not_in_list
Проверяем, что книга не добавиться в список, если жанр указан из списка с возростным рейтингом

7. На метод add_book_in_favorites

7.1 test_add_book_in_favorites_check_book_in_favorites
Проверяем, что при добавлении книги в избранное, она добавилась

7.2 test_add_book_in_favorites_check_book_not_in_lest_not_add
Проверяем, что если книгу добавляют, не существующую в словаре книг, то она не добавить в список избранного

8. На метод delete_book_from_favorites

8.1 test_delete_book_from_favorites_check_book_remove_in_favorites
Проверяем, что, если книга была удалена из избранного, наименование в нем  будет отсутствовать

9. На метод get_list_of_favorites_books

9.1 Получаем список книг добавленных в избранное, существующих в словаре книг

