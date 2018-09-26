from datetime import date
import issue_database
from book import Book
from issue import Issue


class De_allocate():
    def de_allocate(self):
        de_alloc_issue_id = input("Enter the issue id provided to you:")
        today_date=str(date.today())
        if de_alloc_issue_id in issue_database:
            if today_date == Issue.return_date in issue_database:
                print('Book received')
                Book.total_book+=1
                Issue.current_status = 'returned'

            elif today_date < Issue.return_date:
                overdue_days = Issue.return_date - today_date
                fine = 5 * overdue_days
                print
                "Your fine is Rs", fine
                Issue.current_status = 'returned'

            else:
                Book.book_no += 1
                print("Thank you for using the library")