import sys

from book_database import connection
from member import Member


def add_member(member_object):           #add member to the database
    is_member_added = False
    db = connection()
    sql = "insert into member(user_id,name,contact_no) values ('{}','{}','{}')".format(member_object.getUserId(),
                                                                                       member_object.getName(),
                                                                                       member_object.getContact_no())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_member_added = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_member_added


def remove_member(member_object):        #remove member from the database
    is_member_removed = False
    db = connection()
    sql = "delete from member where user_id='{}'".format(member_object.getUserId())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_member_removed = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_member_removed


def update_member(member_object):        #update the member from the database
    is_member_updated = False
    db = connection()
    sql = "update member set name='{}',contact_no='{}' where user_id='{}'".format(member_object.getName(),
                                                                                  member_object.getContact_no(),
                                                                                  member_object.getUserId())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_member_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_member_updated


def show_member(member_object):
    is_member_shown = False
    db = connection()
    sql = "select * from member"
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        print("user_id={}".format(r[0]))
        print("name={}".format(r[1]))
        print("contact_no={}".format(r[2]))
        print()
    try:
        cursor.execute(sql)
        db.commit()
        is_member_shown = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_member_shown


def getMemberDetail(user_id):
    db = connection()
    sql = "select * from member where user_id='{}'".format(user_id)
    cursor = db.cursor()
    cursor.execute(sql)
    original_member = cursor.fetchone()
    if (original_member):
        m = Member(name=original_member[1], contact_no=original_member[2])
        m.setISBN(original_member[0])
    return original_member
    return m
