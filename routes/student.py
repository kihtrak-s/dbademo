from flask import Blueprint, request, jsonify
import sqlite3
import config
from sql import fetch_all_students,insert_item

students_bp = Blueprint('students',__name__)

table_name='Student'
table_attributes=['StudentID','Name','DOB','Gender','AdmissionNo','ClassID','SectionID','ParentInfo']
students_api='/students'

@students_bp.route(students_api,methods=['GET'])
def get_students():
    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(fetch_all_students)
        students = cursor.fetchall()

    html = config.create_html_table("Students",table_attributes,students)
    return html

@students_bp.route(students_api,methods=['POST'])
def add_student():
    # data = request.json
    # details = data.get('student_details')
    details={'name':'Ram','gender':'male'}
    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Student(name,gender) VALUES(?)', details)
        conn.commit()
    return jsonify({'message': 'Item added successfully'}), 201

@students_bp.route(students_api+'/<int:student_id>',methods=['GET'])
def get_student_by_id(student_id):
    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Student WHERE studentId = ?', (student_id,))
        student = cursor.fetchone()

    if student:
        return jsonify({'student': student}), 200
    else:
        return jsonify({'message': 'Student not found'}), 404
    
@students_bp.route(students_api + '/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Student WHERE studentID = ?', (student_id,))
        conn.commit()
    return jsonify({'message': f'Student with id {student_id} deleted successfully'}), 200

@students_bp.route(students_api, methods=['DELETE'])
def delete_all_students():
    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Student')
        conn.commit()
    return jsonify({'message': 'All students deleted successfully'}), 200
    