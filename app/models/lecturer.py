from sqlalchemy import Column, String, Integer, orm
from app.models.human import Human

class Lecturer(Human):
    id = Column(Integer, primary_key=True, autoincrement=True)


    def __init__(self, ID_num, Name, Username, password, programme):
        super(Lecturer,self).__init__(ID_num, Name, Username, password, programme)
