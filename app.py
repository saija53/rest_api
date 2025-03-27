from flask import Flask, jsonify


todo = Flask('__name__')

students = [
        {
            'id': 1,
            'student_name': 'std1',
            'age': 21,
            'email':'hello@gmail.com'
        },
        {
            'id':2,
            'student_name': 'std2',
            'age': 21,
            'email': 'hello@gmail.com'
        },
        {
            'id':3,
            'student_name': 'std3',
            'age': 21,
            'email': 'hello@gmail.com'
        },
    ]


@todo.route('/students-list')
def students_list():
    return jsonify(students)


@todo.route('/student/get/<int:id>')
def student_get_by_id(id):
    for std in students:
        if std['id'] == id:
            return jsonify(std)

    return "id not found"



if __name__ == '__main__':
    todo.run(
        debug=True
    )