from flask import Blueprint, request, jsonify
import sqlite3
import config
from sql import fetch_all_teachers,insert_item

teachers_bp = Blueprint('techers',__name__)

table_name='Teacher'
table_attributes=['TeacherID','Name','Qualification','Contact','EmployeeType']
teachers_api='/teachers'

@teachers_bp.route(teachers_api,methods=['GET'])
def get_all():
    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(fetch_all_teachers)
        items = cursor.fetchall()

    html = config.create_html_table("Teachers",table_attributes,items)
    buttons_html = ""
    subjects = ["Mathematics", "Science", "English", "History", "Physics"]   
    for subject in subjects:
        subject_button = f'<button onclick="window.location.href=\'{teachers_api}/subject?subject={subject}\'">{subject}</button>'
        buttons_html += subject_button + " "
    html += buttons_html
    return html

@teachers_bp.route(f"{teachers_api}/subject", methods=['GET'])
def get_teachers_by_subject():
    subject = request.args.get('subject')
    if not subject:
        return jsonify({"error": "Subject parameter is required"}), 400
    table_attributes = ['TeacherID', 'TeacherName', 'SubjectName', 'ClassID']
    query = """
            SELECT 
                t.teacherID,
                t.name AS teacherName,
                s.subjectName,
                s.classID
            FROM 
                Teacher t
            JOIN 
                Subject s ON t.teacherID = s.teacherID
            WHERE 
                s.subjectName = ?;
    """

    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, (subject,))
        items = cursor.fetchall()

    html = config.create_html_table("Teachers", table_attributes, items)
    return html

@teachers_bp.route(teachers_api+"/count",methods=['GET'])
def count_teachers():
    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM Teacher')
        count = cursor.fetchone()[0]

    return jsonify({'count': count}), 200
