import issue
from book import Book
from member import Member
from issue import Issue

class Allocate():
    def allocate(self):
        alloc_book_isbn=input("Enter the book isbn to be allocated:")
        if alloc_book_isbn in Book.isbn:
            alloc_member_id=input("Enter member id recieving the book:")
            if alloc_member_id in Member.user_id:
                issue_date=input("Enter issueing date:")
                return_date=input("Enter return date:")
                if issue_date>return_date:
                    print("Issueing date cannot be after return date")
                else:
                    issue_id=issue_date+Member.user_id+return_date
                    issue_date.save()
                    #issue.append(sr_no)
                    Issue.current_status= 'issued'
                    print("This is your issue id: {}".format(issue_id))
                    print("Your return date is: {}".format(return_date))
            else:
                print("user_id entered does not exist")
        else:
             print('ISBN entered is not present in the database')
