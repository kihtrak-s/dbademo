from flask import Blueprint, request, jsonify
import sqlite3
import config
from sql import fetch_all_attendance


attendance_bp = Blueprint('attendence',__name__)

table_name='Student'
table_attributes=['StudentID','Name','DOB','Gender','AdmissionNo','ClassID','SectionID','ParentInfo']
attendance_api='/attendance'

@attendance_bp.route(attendance_api,methods=['GET'])
def get_attendance():
    with sqlite3.connect(config.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(fetch_all_attendance)
        items = cursor.fetchall()

    html = config.create_html_table("Attendance",table_attributes,items)
    return html