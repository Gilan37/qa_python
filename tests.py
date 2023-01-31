class TestBooksCollector:

    def test_get_books_rating_get_dict(self, book):
        # проверяем, что books_rating это словарь
        assert type(book.get_books_rating()) is dict

    def test_add_new_book_add_two_books(self, book):
        # проверяем, что книги добавляются в books_rating
        assert book.get_books_rating() == {'Гордость и предубеждение и зомби': 1, 'Что делать, если ваш кот хочет вас '
                                                                                  'убить': 1}

    def test_set_book_rating_to_five_changed_rating(self, book):
        # меняем рейтинг на 5
        book.set_book_rating('Гордость и предубеждение и зомби', 5)
        # проверяем, что рейтинг 5
        assert book.get_books_rating() == {'Гордость и предубеждение и зомби': 5, 'Что делать, если ваш кот хочет вас '
                                                                                  'убить': 1}

    def test_get_book_rating_by_name(self, book):
        # проверяем рейтинг книги по ее имени
        assert book.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_get_books_with_specific_rating_shows_books(self, book):
        # проверяем, что по рейтингу 1 мы получили список с 2 книгами
        assert book.get_books_with_specific_rating(1) == ['Гордость и предубеждение и зомби', 'Что делать, если ваш '
                                                                                              'кот хочет вас убить']

    def test_add_book_in_favorites_added_book(self, book):
        # добавляем книгу в избранное
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        # проверяем, что книга добавилась в избранное
        assert book.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites_deleted_book(self, book):
        # добавляем книгу в избранное
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        # удаляем книгу из избранного
        book.delete_book_from_favorites('Гордость и предубеждение и зомби')
        # проверяем, что список избранного пустой
        assert book.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_get_list(self, book):
        # добавляем книгу в избранное
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        # проверяем, что favorites это список
        assert type(book.get_list_of_favorites_books()) is list

    def test_add_new_book_duplicate_name_not_added(self, book):
        # добавляем дубль книги в books_rating
        book.add_new_book('Гордость и предубеждение и зомби')
        # проверяем, что дубля нет
        assert book.get_books_rating() == {'Гордость и предубеждение и зомби': 1, 'Что делать, если ваш кот хочет вас '
                                                                                  'убить': 1}

    def test_set_book_rating_to_not_added_book(self, book):
        # проверяем, что нельзя выставить рейтинг книге, которой нет в списке.
        assert book.set_book_rating('Дюна', 1) is None

    def test_set_book_rating_rating_0_not_set(self, book):
        # проверяем, что нельзя выставить рейтинг меньше 1
        assert book.set_book_rating('Гордость и предубеждение и зомби', 0) is None

    def test_set_book_rating_rating_15_not_set(self, book):
        # проверяем, что нельзя выставить рейтинг больше 10
        assert book.set_book_rating('Гордость и предубеждение и зомби', 15) is None
