import uuid

class Submission:
    def __init__(self, author, link, subId=uuid.uuid4(), collaborators=None):
        self.id = subId
        self.author = author
        self.link = link
        self.collaborators = collaborators if collaborators else []
        self.msg = None

    def __str__(self):
        if self.collaborators:
            return f"{self.id} - {self.author} - {self.link} - {self.collaborators}"
        else:
            return f"{self.id} - {self.author} - {self.link}"

    def add_msg(self, msg):
        self.msg = msg
