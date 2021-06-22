from sqlalchemy import Column, String, Integer, orm
from app.models.base import Base

class Human(Base):
    __abstract__ = True # 抽象类 不会生成表
    ID_num = Column(String(50), nullable=False)
    Name = Column(String(50), nullable=False)
    Username = Column(String(50), unique=True, nullable=True)
    password = Column('password', String(100))
    programme = Column(String(50), nullable=False)


    def __init__(self, ID_num, Name, Username, password, programme):
        super(Human,self).__init__()
        self.ID_num = ID_num
        self.Name = Name
        self.Username = Username
        self.password = password
        self.programme = programme