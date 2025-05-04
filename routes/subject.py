from flask import Blueprint, request, jsonify
import sqlite3
import config
from sql import fetch_all_subjects


subjects_bp = Blueprint('subject',__name__)

table_name='Subject'
table_attributes=['SubjectID','SubjectName','type','ClassID','TeacherID']
subjects_api='/subjects'

@subjects_bp.route(subjects_api,methods=['GET'])
def get_subjects():
    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(fetch_all_subjects)
        items = cursor.fetchall()

    html = config.create_html_table("Subjects",table_attributes,items)
    return html

@subjects_bp.route(subjects_api+'/count',methods=['GET'])
def count_subjects():
    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM Subject')
        count = cursor.fetchone()[0]

    return jsonify({'count': count}), 200
