import sys

import pymysql

from book import Book


def connection():
    dbconnection = pymysql.connect("localhost", "root", "", "python_project")
    return dbconnection


def add_book(book_object):
    is_book_added = False
    db = connection()
    sql = "insert into book(title,author,publication,publication_year,isbn,total_books) values('{}','{}','{}','{}','{}','{}')".format(
        book_object.getTitle(), book_object.getAuthor(), book_object.getPublication(), book_object.getPublicationYear(), book_object.getISBN(),
        book_object.getTotalBook())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_book_added = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_book_added


def remove_book(book_object):
    is_book_removed = False
    db = connection()
    sql = "delete from book where title='{}'".format(book_object.getTitle())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_book_removed = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_book_removed


def update_book(book_object):
    is_book_updated = False
    db = connection()
    sql = "update book set title='{}',author='{}',publication='{}',publication_year='{}',total_book='{}' where isbn='{}'".format(
        book_object.getTitle(), book_object.getAuthor(), book_object.getPublication(), book_object.getPublicationYear(), book_object.getTotalBook(),
        book_object.getISBN())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_book_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_book_updated


def show_book(book_object):
    is_book_shown = False
    db = connection()
    sql = "select * from book"
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        print("title={}".format(r[0]))
        print("author={}".format(r[1]))
        print("publication={}".format(r[2]))
        print("publication_year={}".format(r[3]))
        print("isbn={}".format(r[4]))
        print("total_books={}".format(r[5]))
        print()
    try:
        cursor.execute(sql)
        db.commit()
        is_book_shown = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_book_shown


def getBookDetail(isbn):
    db = connection()
    sql = "select * from book where isbn='{}'".format(isbn)
    cursor = db.cursor()
    cursor.execute(sql)
    original_book = cursor.fetchone()
    if (original_book):
        b = Book(title=original_book[0], author=original_book[1], publication=original_book[2],
                 publication_year=original_book[3], total_book=original_book[5])
        b.setISBN(original_book[4])
    return original_book
    return b
