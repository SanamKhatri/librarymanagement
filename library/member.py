class Member():
    def __init__(self, user_id, name, contact_no):
        self.user_id = user_id
        self.name = name
        self.contact_no = contact_no

    def getUserId(self):
        return self.user_id

    def getName(self):
        return self.name

    def getContact_no(self):
        return self.contact_no

    def setUserId(self, user_id):
        self.user_id = user_id

    def setName(self, name):
        self.name = name

    def setContact_no(self, contact_no):
        self.contact_no = contact_no
