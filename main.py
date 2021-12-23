import json
import random

from faker import Faker
fake = Faker()

from conf import MODEL


def check_len_title(func):
    """Method checks length of books title, which should be less then 25 symbols"""
    def wrapper(*args, **kwargs):
        val = func()
        if len(val) > 25:
            raise ValueError("Name of this book is too long")
        else:
            return val

    return wrapper


@check_len_title
def get_value_title() -> str:
    """Method returns title from file books.txt"""
    with open("books.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return random.choice(lines)


def get_year() -> int:
    """Method returns random year value since 1800 to 2021"""
    return random.randrange(1800, 2021)


def get_pages() -> int:
    """Method returns random number of pages from 1 to 1000"""
    return random.randrange(1, 1000)


def get_price() -> float:
    """Method returns random float price value from 0 to 10000, significant digit 2"""
    return round(random.uniform(0, 10000), 2)


def get_isbn() -> str:
    """Method returns fake isbn number"""
    return fake.isbn13()


def get_rating() -> float:
    """Method returns random float rating value"""
    return random.uniform(0, 5)


def get_author() -> str:
    """Method returns fake author name"""
    return fake.name()


def generator_(pk: int = 1) -> dict:
    """Method returns dicts
    param: pk: start value of increment"""
    while True:
        fields = {"Title": get_value_title(),
                  "year": get_year(),
                  "pages": get_pages(),
                  "isbn13": get_isbn(),
                  "rating": get_rating(),
                  "price": get_price(),
                  "author": get_author()}
        book = {"pk": pk, "model": MODEL, "fields": fields}
        yield book
        pk += 1


def main() -> None:
    """Method receives list of 100 dictionaries and writes it into json file"""
    result = []
    book = generator_()
    for _ in range(100):
        result.append(next(book))
    with open("write.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
