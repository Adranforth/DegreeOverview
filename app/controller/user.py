from flask import Flask, Blueprint,render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user
from app.models.base import db
from app.models.student import Student
from app.models.coursedesigner import Coursedesigner
from app.models.lecturer import Lecturer
from app.models.registered import Registered
from app.controller.lecturer import lecturer_home
from app.controller.student import student_home
from app.controller.coursedesigner import coursedesigner_home
from sqlalchemy import or_,and_,all_,any_


userBP = Blueprint('user', __name__)
@userBP.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:

        ID_num = request.form.get('ID_num')
        _password = request.form.get('password')
        print(ID_num, _password)

        if ID_num == '' or _password == '':
            return render_template('login.html',title='Incomplete information')
        else:
            if 's' in ID_num:
                result1 =  Student.query.filter(and_(Student.ID_num == ID_num,Student.password == _password)).first()
                if result1:
                    print(result1.Name)
                    print(result1.password)
                    login_user(Registered(ID_num))
                    name = result1.Name
                    type = 'Student'
                    return redirect(url_for('student.student_home', name = name, type = type))
                else:
                    return render_template('login.html',title='Wrong student account')
                    
            elif 'c' in ID_num:
                result2 =  Coursedesigner.query.filter(and_(Coursedesigner.ID_num == ID_num,Coursedesigner.password == _password)).first()
                if result2:
                    print(result2.Name)
                    print(result2.password)
                    login_user(Registered(ID_num))
                    name = result2.Name
                    type = 'Course Designer'
                    prog = result2.programme
                    return redirect(url_for('coursedesigner.coursedesigner_home', name = name, type = type, prog = prog))
                else:
                    return render_template('login.html',title='Wrong course designer account')
            elif 'l' in ID_num:
                result3 =  Lecturer.query.filter(and_(Lecturer.ID_num == ID_num,Lecturer.password == _password)).first()
                if result3:
                    print(result3.Name)
                    print(result3.password)
                    login_user(Registered(ID_num))
                    name = result3.Name
                    type = 'Lecturer'
                    return redirect(url_for('lecturer.lecturer_home', name = name, type = type))
                else:
                    return render_template('login.html',title='Wrong lecturer account')
            else:
                return render_template('login.html',title='Wrong information')

@userBP.route('/logout',methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))