import json

from flask import Blueprint, render_template, request, jsonify, redirect, session

from app.controller.common import search_inner
from app.models.base import db
from app.models.course import Course, Cilo
from app.models.lecturer import Lecturer
from sqlalchemy import or_, and_, all_, any_
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin

lecturerBP = Blueprint('lecturer', __name__)


@lecturerBP.route('lecturer_home')
@login_required
def lecturer_home():
    user_id = session['_user_id']
    cs = Lecturer.query.filter(Lecturer.ID_num == user_id).first()
    name = cs.Name
    return render_template('index_l.html', name=name, type="lecture")


@lecturerBP.route('index')
def index():
    user_id = session['_user_id']
    name = Lecturer.query.filter(Lecturer.ID_num == user_id).first().Name
    return render_template('welcome.html', name=name)


@lecturerBP.route('search')
def search():
    search_word = request.args.get('search')
    search_type = request.args.get('a')
    return search_inner(search_word, search_type)


@lecturerBP.route('all_cilos')
def all_cilos():
    return render_template('all_cilos.html', cilos=Cilo.query.all())


@lecturerBP.route('show_cilo/<cilo_id>', methods=['GET', 'POST'])
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
