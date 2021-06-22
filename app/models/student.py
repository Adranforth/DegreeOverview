from sqlalchemy import Column, String, Integer, orm
from app.models.human import Human


class Student(Human):
    id = Column(Integer, primary_key=True, autoincrement=True)
    Student_ID = Column(String(100), nullable=False)

    def __init__(self, ID_num, Name, Username, password, programme, Student_ID):
        super(Student, self).__init__(ID_num, Name, Username, password, programme)
        self.Student_ID = Student_ID

    def jsonstr(self):
        jsondata = {
            'ID_num': self.ID_num,
            'Name': self.Name,
            'Email': self.Email,
            'password': self.password

        }

        return jsondata
