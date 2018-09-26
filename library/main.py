import member_database
from book import Book
import book_database
from member import Member
from allocate import Allocate
from de_allocate import De_allocate


def welcome_menu():
    #esc = 1
    #while (esc != 0):
        menu = """
        Welcome to Library System.
	        1. To add a book
	        2. To update a book
	        3. To show all the books
	        4. To delete a book
	        5. To add a member
	        6. To update a member
	        7. To show all the members
	        8. To delete a member
	        9.  To allocate a book
	        10. To return a book
	  	    """
        print(menu)
        choice = int(input("Enter your choice"))
        if choice == 1:
            #while
                title = input("Enter the title")
                author = input("Enter the author")
                publication = input("Enter the publication")
                publication_year = input("Enter the publication year")
                isbn = input("Enter the ISBN no")
                total_books = input("Enter the total no of books")
                b = Book(title=title, author=author, publication=publication, publication_year=publication_year, isbn=isbn,
                     total_book=total_books)
                is_book_inserted = book_database.add_book(b)
                if (is_book_inserted):
                   print("Book have been added")
                else:
                    print("Book have not been added")
        elif choice == 2:
            #while
                isbn = input("Enter ISBN no of the book")
                is_inserted = book_database.getBookDetail(isbn)
                if (is_inserted):
                    book_detail = book_database.getBookDetail(isbn)
                    print("Original Info")
                    print("Author= " + book_detail[1])
                    print("Title= " + book_detail[0])
                    print("Publication= " + book_detail[2])
                    print("Publication Year= " + book_detail[3])
                    print("Total no of books= " + book_detail[4])
                    author = input("Enter the author name")
                    title = input("Enter the title")
                    publication = input("Enter the publication")
                    publication_year = input("Enter the publication year")
                    isbn = input("Enter the ISBN No")
                    total_books = input("Enter the total no of books")
                    book_object = Book(title=title, author=author, publication=publication,
                                   publication_year=publication_year,
                                   isbn=isbn, total_book=total_books)
                    book_object.setISBN(book_detail[4])
                    is_updated = book_database.update_book(book_object)
                    if (is_updated):
                        print("Book updated")
                    else:
                        print("Update error")
                else:
                    pass
        elif choice == 3:
                b = Book
                book_database.show_book(b)
        elif choice == 4:
            #while
                isbn = input("Enter the book ISBN no to remove")
                b = Book(title=None, author=None, publication=None, publication_year=None, isbn=isbn, total_book=None)
                book_database.remove_book(b)
        elif choice == 5:
            #while
                user_id = input("Enter the user id")
                name = input("Enter the user name")
                contact_no = input("Enter the contact no")
                m = Member(user_id=user_id, name=name, contact_no=contact_no)
                is_member_inserted = member_database.add_member(m)
                if (is_member_inserted):
                    print("Member have been added")
                else:
                    print("Member have not been added")
        elif choice == 6:
            #while
                user_id = input("Enter member user id")
                is_member_updated = member_database.getMemberDetail(user_id)
                if (is_member_updated):
                    member_detail = member_database.getMemberDetail(user_id)
                    print("Original Info")
                    print("Name= " + member_detail[1])
                    print("Contact No= " + member_detail[2])
                    user_id = input("Enter the User ID")
                    contact_no = input("Enter the Contact No")
                    user_name = input("Enter the User Name")
                    member_object = Member(name=user_name, user_id=user_id, contact_no=contact_no)
                    member_object.setUserId(member_detail[0])
                    is_updated = member_database.update_member(member_object)
                    if (is_updated):
                        print("Member updated")
                    else:
                        print("Update error")
                else:
                    pass
        elif choice == 7:
            m = Member
            member_database.show_member(m)
        elif choice == 8:
            #while
                user_id = input("Enter the User Id")
                m = Member(user_id=user_id, name=None, contact_no=None)
                member_database.remove_member(m)
        # elif choice == 9:
        #     Allocate.allocate()
        # elif choice == 10:
        #     De_allocate.de_allocate()
        else:
            print("The choice is invalid")
if __name__ == '__main__':
    welcome_menu()
