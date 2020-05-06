from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import BackgroundTasks
from app import crud
from app.api.utils.db import get_db
from app.db_models.book import Book as DBBook
from app.models.book import Book, BookCreate, BookUpdate

router = APIRouter()


@router.get('/')
def get_all_books(
        db: Session = Depends(get_db)):
    books = crud.book.get_multiple_book(db_session=db)
    return books


@router.get('/get_by_id/{book_id}')
def read_book_by_id(
    *,
    db: Session = Depends(get_db),
        book_id: int):
    book = crud.book.get_by_id(db_session=db, book_id=book_id)
    if not book:
        raise HTTPException(status_code=400, detail="book not found")
    return book

@router.get('/get_by_name/{book_name}')
def read_book_by_id(
    *,
    db: Session = Depends(get_db),
        book_name: str):
    book = crud.book.get_by_name(db_session=db, name=book_name)
    if not book:
        raise HTTPException(status_code=400, detail="book not found")
    return book


@router.put('/{book_id}')
def update_book(
    *,
    db: Session = Depends(get_db),
    book_id: str,
    book_in: BookUpdate):

    book = crud.book.get_by_id(db_session=db, book_id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    book = crud.book.update(db_session=db, book=book, book_in=book_in)
    return book

@router.post('/')
def insert_book(
    *,
    db: Session = Depends(get_db),
        book_in: BookCreate):
    book = crud.book.get_by_id(db_session=db, book_id=book_in.id)
    if book:
        raise HTTPException(
            status_code=400,
            detail="The Book with this id already exists in the system."
        )
    book = crud.book.create(db_session=db, book_in=book_in)
    return book