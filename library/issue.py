class Issue():
    def __init__(self, user_id, isbn, issue_id, issue_date, return_date, current_status):
        self.user_id = user_id
        self.isbn = isbn
        self.issue_date = issue_date
        self.issue_id = issue_id
        self.return_date = return_date
        self.current_status = current_status

    def getUser_Id(self):
        return self.user_id

    def getISBN(self):
        return self.isbn

    def getIssue_Date(self):
        return self.issue_date

    def getIssue_Id(self):
        return self.issue_id

    def getReturn_Date(self):
        return self.return_date

    def getCurrent_Status(self):
        return self.current_status

    def setUser_Id(self, user_id):
        self.user_id = user_id

    def setISBN(self, isbn):
        self.isbn = isbn

    def setIssue_Date(self, issue_date):
        self.issue_date = issue_date

    def setIssue_Id(self, issue_id):
        self.issue_id = issue_id

    def setReturn_Date(self, return_date):
        self.return_date = return_date

    def setCurrent_Status(self, current_satus):
        self.current_status = current_satus