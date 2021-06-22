from sqlalchemy import Column, String, Integer, ForeignKey, Float
from app.models.base import Base, db
from typing import List


class Course(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    code = Column(String(100), nullable=False)
    academic_year = Column(String(100), nullable=False)
    programme = Column(String(100), nullable=False)
    _type = Column(String(100), nullable=False)
    cilo1_id = Column(Integer, ForeignKey('cilo.id'))
    cilo2_id = Column(Integer, ForeignKey('cilo.id'))
    cilo3_id = Column(Integer, ForeignKey('cilo.id'))
    pre_course1_id = Column(Integer, ForeignKey('course.id'))
    pre_course2_id = Column(Integer, ForeignKey('course.id'))
    pre_course3_id = Column(Integer, ForeignKey('course.id'))

    def __init__(self):
        super().__init__()


class Cilo(Base):
    id = Column(Integer, primary_key=True)
    pre_cilo1 = Column(Integer, ForeignKey('cilo.id'))
    pre_cilo2 = Column(Integer, ForeignKey('cilo.id'))
    pre_cilo3 = Column(Integer, ForeignKey('cilo.id'))
    name = Column(String(100), nullable=False)

    def __init__(self, name):
        super().__init__()
        self.name = name


class Assessment(Base):
    id = Column(Integer, primary_key=True)
    course = Column(Integer, ForeignKey('course.id'), nullable=False)
    weight = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    cilos = Column(String(100), nullable=False)

    def __init__(self, course, name, weight, cilos):
        super().__init__()
        self.course = course.id
        self.name = name
        self.weight = int(weight)
        self.cilos = cilos

    @staticmethod
    def latest_before(before_time: int, course_id: int):
        # 因为评分系统有很多个 version，新的评分体系不影响旧的成绩，因此需要根据录入成绩的时刻，查询适用的评分体系
        items = Assessment.query \
            .order_by(-Assessment.create_time) \
            .filter(Assessment.create_time <= before_time) \
            .filter(Assessment.course == course_id) \
            .all()
        return [item for item in items if item.create_time == items[0].create_time]


class Grade(Base):
    id = Column(Integer, primary_key=True)
    Student_ID = Column(String(100))
    course_id = Column(Integer, ForeignKey('course.id'))
    EvaluationMethod = Column(String(100))
    value = Column(Float)

    def __init__(self):
        super().__init__()
