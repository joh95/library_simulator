from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.encoders import jsonable_encoder
from app.models.book import Book, BookCreate, BookUpdate

router = APIRouter()

storage = []

@router.get('/')
def get_all_books():
    return storage


@router.get('/get_by_id/{book_id}')
def read_book_by_id(
    *,
    book_id: int):

    position_detected = False

    for i in range(len(storage)):
        if storage[i]["id"] == book_id:
            position_detected = True
        if position_detected:
            position_id = i
            continue

    if position_detected:
        book = storage[position_id]
        return book
    else:
        message = "Book not available"
        return message

@router.get('/get_by_name/{book_name}')
def read_book_by_id(
    *,
    book_name: str):

    position_detected = False

    for i in range(len(storage)):
        if storage[i]["name"] == book_name:
            position_detected = True
            
        if position_detected:
            position_id = i
            book = storage[position_id]
            return book

    message = "Book not available"
    return message

@router.put('/{book_id}')
def update_book(
    *,
    book_id: int,
    book_in: BookUpdate):

    position_detected = False
    book_in = book_in.dict()

    for i in range(len(storage)):
        if storage[i]["id"] == book_id:
            position_detected = True
        if position_detected:
            position_id = i
            if position_detected:
                storage.pop(i)
                storage.append(book_in)
                message = "Update completed"
                return message
    
    message = "Book not available"
    return message

@router.post('/')
def insert_book(
    *,
        book_in: BookCreate):

    id_exists = False
    book_in = book_in.dict()
    if len(storage) == 0:
        storage.append(book_in)
        message = "Insert successfully"
        return message
    else:
        for i in range(len(storage)):
            if storage[i]["id"] == book_in["id"]:
                id_exists = True

        if id_exists:
            message = "The book id already exists"
            return message
        else:
            storage.append(book_in)
            message = "Insert successfully"
            return message

@router.get('/generate_smoke_test/')
def generate_test():
    test1 = {
        "id": 11111,
        "name": "smoke book 1",
        "literary_genre": "smbk 1",
        "author": "team 1",
        "year": "2020",
        "price": 10000
    }

    test2 = {
        "id": 11112,
        "name": "smoke book 2",
        "literary_genre": "smbk 2",
        "author": "team 2",
        "year": "2020",
        "price": 10000
    }

    test3 = {
        "id": 11113,
        "name": "smoke book 3",
        "literary_genre": "smbk 3",
        "author": "team 3",
        "year": "2020",
        "price": 10000
    }

    storage.append(test1)
    storage.append(test2)
    storage.append(test3)

    message = "Smoke test generated"
    return message