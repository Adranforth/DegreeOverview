from sqlalchemy import Column, String, Integer, orm
from app.models.human import Human

class Coursedesigner(Human):
    id = Column(Integer, primary_key=True, autoincrement=True)


    def __init__(self, ID_num, Name, Username, password, programme):
        super(Coursedesigner,self).__init__(ID_num, Name, Username, password, programme)
