import csv

from typing import Union
from fastapi import FastAPI

app = FastAPI()


def read_books_from_csv():
    csv_file = open('books.csv', newline='')
    book_list = csv.DictReader(csv_file, delimiter=',')
    return list(book_list)


@app.get("/books", tags=["books"])
def get_books(year: Union[str, None] = None):

    """
    Get a list of books.
    :param year:
    :return:
    """

    book_list = read_books_from_csv()

    if year:
        book_list = list(filter(lambda book: book["Year"] == year, book_list))

    return {"books": book_list}


@app.get("/books/{position}", tags=["books"])
def get_single_book(position: str):

    """
    Get a single book from position in the list
    :param position:
    :return:
    """

    book_list = read_books_from_csv()
    book = book_list[position]

    return {"book": book}


@app.post("/books", tags=["books"])
def create_book():
    pass


@app.get("/categories", tags=["categories"])
def get_categories():
    pass
