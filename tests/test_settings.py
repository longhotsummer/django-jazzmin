# from jazzmin.settings import get_search_model_string


# def test_get_search_model_string():
#     # model name is always lower case
#     assert get_search_model_string("books.Book") == "books.book"
#     assert get_search_model_string("books.book") == "books.book"
#     # the app name gets never touched
#     assert get_search_model_string("Books.Book") == "Books.book"
#     assert get_search_model_string("BookShelf.book") == "BookShelf.book"


from django.conf import settings

from jazzmin.types import JazzminSettings, MenuLink, UITweaks


def test_jazzmin_settings() -> None:
    JazzminSettings()
    JazzminSettings(**settings.JAZZMIN_SETTINGS)


def test_jazzmin_ui_tweaks() -> None:
    UITweaks()
    UITweaks(**settings.JAZZMIN_UI_TWEAKS)


def test_make_menu_link() -> None:
    MenuLink()
