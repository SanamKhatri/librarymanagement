import sys

from book_database import connection
from issue import Issue


def add_issue(issue_object):
    is_added_issue = False
    db = connection()
    sql = "insert into issue(user_id,isbn,issue_date,issue_id,return_date,current_status) values ('{}','{}','{}','{}','{}','{}')".format(
        issue_object.getUser_Id(), issue_object.getISBN(), issue_object.getIssue_Date(), issue_object.getIssue_Id(), issue_object.getReturn_Date(),
        issue_object.getCurrent_Status())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_added_issue = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_added_issue

def remove_issue(issue_object):
    is_issue_removed = False
    db = connection()
    sql = "delete from issue where issue_id='{}'".format(issue_object.getIssue_Id())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_issue_removed = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_issue_removed
#
#
#
# def show_book(issue_object):
#     is_issue_shown = False
#     db = connection()
#     sql = "select * from book"
#     cursor = db.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for r in result:
#         print("user_id={}".format(r[0]))
#         print("isbn={}".format(r[1]))
#         print("issue_id={}".format(r[2]))
#         print("issue_date={}".format(r[3]))
#         print("return_date={}".format(r[4]))
#         print("current_status={}".format(r[5]))
#         print()
#     try:
#         cursor.execute(sql)
#         db.commit()
#         is_issue_shown = True
#     except:
#         print(sys.exc_info())
#     finally:
#         db.close()
#     return is_issue_shown
