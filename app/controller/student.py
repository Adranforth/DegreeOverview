import json

from flask import Flask, Blueprint, render_template, request, session

from app.controller.common import search_inner, visualize_inner
from app.models.base import db
from app.models.course import Cilo, Grade, Assessment, Course
from app.models.student import Student
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin

studentBP = Blueprint('student', __name__)


@studentBP.route('student_home')
@login_required
def student_home():
    user_id = session['_user_id']
    cs = Student.query.filter(Student.ID_num == user_id).first()
    name = cs.Name
    return render_template('index_s.html', name=name, type="student")


@studentBP.route('index')
def index():
    user_id = session['_user_id']
    cs = Student.query.filter(Student.ID_num == user_id).first()
    name = cs.Name
    return render_template('welcome.html', name=name)


@studentBP.route('search')
def search():
    search_word = request.args.get('search')
    search_type = request.args.get('a')
    return search_inner(search_word, search_type)

@studentBP.route('performance')
def performance():
    user_id = session['_user_id']
    cs = Student.query.filter(Student.ID_num == user_id).first()
    student_id = cs.Student_ID
    filter_student = Grade.query.filter(Grade.Student_ID == student_id)
    # 根据学号，查到上过哪几门课
    course_id_list = set(_.course_id for _ in filter_student.all())

    performance_list = []
    # 按课程、按CILO来统计
    for course_id in course_id_list:
        print(course_id)
        course = Course.query.get(course_id)
        grade_list = list(filter_student.filter(Grade.course_id == course_id).all())
        create_time = grade_list[0].create_time
        # 根据上过的课，找到对应的给分规则
        ass_list = Assessment.latest_before(create_time, course_id)
        # 汇总给分规则算出各个 CILO 的分数
        cilo_summary = {
            "1": [],
            "2": [],
            "3": [],
        }
        for ass in ass_list:
            method = ass.name
            grade = next(_grade for _grade in grade_list if _grade.EvaluationMethod == method)
            cilos = ass.cilos.split('-')
            for cilo in cilos:
                cilo_summary[cilo].append((ass.weight, grade.value, len(cilos)))
        print(cilo_summary)
        for k, v in cilo_summary.items():
            # clio 是空，无数据
            if len(v) == 0:
                continue
            sum_weight = 0
            sum_value = 0
            for _weight, _value, _split_count in v:
                sum_weight += _weight / _split_count
                sum_value += _value / _split_count
            score = sum_value / sum_weight * 100
            if k == '1':
                cilo = Cilo.query.get(course.cilo1_id)
                performance_list.append((course, cilo, "%.2f" % score))
            elif k == '2':
                cilo = Cilo.query.get(course.cilo2_id)
                performance_list.append((course, cilo, "%.2f" % score))
            elif k == '3':
                cilo = Cilo.query.get(course.cilo3_id)
                performance_list.append((course, cilo, "%%%.2f" % score))

    print(performance_list)
    return render_template('performance.html',
                           performance_list=performance_list)


@studentBP.route('all_cilos')
def all_cilos():
    return render_template('all_cilos.html', cilos=Cilo.query.all())


@studentBP.route('show_course_grade/<course_id>', methods=['GET'])
def show_course_grade(course_id):
    course = Course.query.get(course_id)
    user_id = session['_user_id']
    student = Student.query.filter(Student.ID_num == user_id).first()
    q = Grade.query \
        .filter(Grade.Student_ID == student.Student_ID) \
        .filter(Grade.course_id == course_id)

    return render_template('show_course_grade.html',
                           course=course,
                           student=student,
                           q=q)


@studentBP.route('show_cilo/<cilo_id>', methods=['GET'])
def show_cilo(cilo_id):
    cilo_id = int(cilo_id)
    cilo = Cilo.query.get(cilo_id)
    errmsg = None
    graph_array = []
    graph_array.append({"id": "root", "isroot": True, "topic": "<b>%s</b>" % (cilo.name)}, )
    if cilo.pre_cilo1:
        graph_array.append({"id": "sub1", "parentid": "root", "topic": Cilo.query.get(cilo.pre_cilo1).name}, )
    if cilo.pre_cilo2:
        graph_array.append({"id": "sub2", "parentid": "root", "topic": Cilo.query.get(cilo.pre_cilo2).name}, )
    if cilo.pre_cilo3:
        graph_array.append({"id": "sub3", "parentid": "root", "topic": Cilo.query.get(cilo.pre_cilo3).name}, )

    graph_json = json.dumps(graph_array)
    print(graph_json)
    return render_template('show_cilo.html',
                           title=errmsg,
                           cilo=cilo,
                           graph_json=graph_json,
                           )

@studentBP.route('visualize_dep', methods=['GET'])
def visualize_dep():
    keyword = request.args.get("programme")
    return visualize_inner(keyword)
