from flask import request, render_template

from app.models.course import Course, Cilo


def search_inner(search_word, search_type):
    data = []
    if search_type == 'option1':
        course_name = search_word
        course = Course.query.filter(Course.name == course_name).first()
        if course:
            pre_courses = []
            if course.pre_course1_id:
                pre_courses.append(Course.query.get(course.pre_course1_id))
            if course.pre_course2_id:
                pre_courses.append(Course.query.get(course.pre_course2_id))
            if course.pre_course3_id:
                pre_courses.append(Course.query.get(course.pre_course3_id))

            post_courses = list(
                Course.query.filter((Course.pre_course1_id == course.id)
                                    | (Course.pre_course2_id == course.id)
                                    | (Course.pre_course3_id == course.id))
                    .all())

            for _course in pre_courses:
                data.append((_course.name, course_name, "-"))
            for _course in post_courses:
                data.append(("-", course_name, _course.name))


    elif search_type == 'option2':
        cilo_name = search_word
        cilo = Cilo.query.filter(Cilo.name == cilo_name).first()
        if cilo:
            pre_cilos = []
            if cilo.pre_cilo1:
                pre_cilos.append(Cilo.query.get(cilo.pre_cilo1))
            if cilo.pre_cilo2:
                pre_cilos.append(Cilo.query.get(cilo.pre_cilo2))
            if cilo.pre_cilo3:
                pre_cilos.append(Cilo.query.get(cilo.pre_cilo3))

            post_cilos = list(
                Cilo.query.filter((Cilo.pre_cilo1 == cilo.id)
                                  | (Cilo.pre_cilo2 == cilo.id)
                                  | (Cilo.pre_cilo3 == cilo.id))
                    .all())

            for _cilo in pre_cilos:
                data.append((_cilo.name, cilo_name, "-"))
            for _cilo in post_cilos:
                data.append(("-", cilo_name, _cilo.name))

    elif search_type == 'option3':
        course_query = Course.query.filter(Course.name.like("%" + search_word + "%"))
        for _ in course_query:
            data.append(("Course", _.name))
        cilo_query = Cilo.query.filter(Cilo.name.like("%" + search_word + "%"))
        for _ in cilo_query:
            data.append(("CILO", _.name))
    if not search_type:
        search_type = "option1"
    return render_template('search.html',
                           search_word=search_word,
                           search_type=search_type,
                           data=data)

def visualize_inner(keyword):
    programme_list = set(_.programme for _ in Course.query.all())
    data = []

    if keyword:
        print("keyword", keyword)
        visited_nodes = set()
        course_list = list(Course.query.filter(Course.programme == keyword))

        print("course_list", course_list)
        while len(course_list) > 0:
            to_visit = []
            for course in course_list:
                if (course.pre_course1_id is None or course.pre_course1_id in visited_nodes) \
                        and (course.pre_course2_id is None or course.pre_course2_id in visited_nodes) \
                        and (course.pre_course3_id is None or course.pre_course3_id in visited_nodes):
                    to_visit.append(course)
            for _course in to_visit:
                course_list.remove(_course)
                visited_nodes.add(_course.id)
                data.append((_course.name,
                             Course.query.get(_course.pre_course1_id).name if _course.pre_course1_id else None,
                             Course.query.get(_course.pre_course2_id).name if _course.pre_course2_id else None,
                             Course.query.get(_course.pre_course3_id).name if _course.pre_course3_id else None,
                             ))
            print("course_list", course_list)
    return render_template('visualize_dep.html',
                           keyword=keyword,
                           programme_list=programme_list,
                           data=data)
