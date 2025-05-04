from flask import Flask, request, jsonify
import sql
import config
import sqlite3
import os
from routes import students_bp

app = Flask(__name__)
app.register_blueprint(students_bp)


# Initialize the database
def init_db():
    if not os.path.exists(config.DATABASE):
        print("Database not found. Creating a new one...")
        with sqlite3.connect(config.DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(sql.create_student_table)
            cursor.execute(sql.create_teacher_table)
            cursor.execute(sql.create_subject_table)
            cursor.execute(sql.create_exam_table)
            cursor.execute(sql.create_marks_table)
            cursor.execute(sql.create_attendance_table)
            conn.commit()
# Route to display welcome message at the root URL
@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to the Student Management System!"

# # Route to fetch all items
# @app.route('/items', methods=['GET'])
# def get_items():
#     with sqlite3.connect(config.DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute(sql.fetch_all_table)
#         items = cursor.fetchall()
#     html = '''
#     <html>
#         <body>
#             <h1>Items</h1>
#             <table border="1">
#                 <thead>
#                     <tr>
#                         <th>ID</th>
#                         <th>Name</th>
#                         <th>Description</th>
#                     </tr>
#                 </thead>
#                 <tbody>
#     '''
#     for item in items:
#         html += f'<tr><td>{item[0]}</td><td>{item[1]}</td><td>{item[2]}</td></tr>'
#     html += '''
#                 </tbody>
#             </table>
#         </body>
#     </html>
#     '''
#     return html

# # Route to add a new item
# @app.route('/items', methods=['POST'])
# def add_item():
#     data = request.json
#     name = data.get('name')
#     description = data.get('description', '')
#     with sqlite3.connect(config.DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute(insert_item, (name, description))
#         conn.commit()
#     return jsonify({'message': 'Item added successfully'}), 201

# # Route to fetch a single item by ID
# @app.route('/items/<int:item_id>', methods=['GET'])
# def get_item(item_id):
#     with sqlite3.connect(config.DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute(fetch_item_by_id, (item_id,))
#         item = cursor.fetchone()
#     if item:
#         return jsonify(item)
#     else:
#         return jsonify({'error': 'Item not found'}), 404

# # Route to delete an item by ID
# @app.route('/items/<int:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     with sqlite3.connect(config.DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute(delete_item_by_id, (item_id,))
#         conn.commit()
#     return jsonify({'message': 'Item deleted successfully'})    

if __name__ == '__main__':
    init_db()
    app.run(debug=True)