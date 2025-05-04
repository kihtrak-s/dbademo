create_student_table='''
CREATE TABLE Student (
    studentId INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    dob DATE,
    gender VARCHAR(10),
    admissionNumber VARCHAR(50) UNIQUE,
    contactInfo VARCHAR(255),
    parentName VARCHAR(100),
    parentContact VARCHAR(100),
    classId INTEGER,
    FOREIGN KEY (classId) REFERENCES Class(classId)
)
'''
create_teacher_table='''
CREATE TABLE Teacher (
    teacherId INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    qualification VARCHAR(100),
    contactInfo VARCHAR(255)
)
'''
create_staff_table='''
CREATE TABLE NonTeachingStaff (
    staffId INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50),
    department VARCHAR(100),
    contactInfo VARCHAR(255),
    joiningDate DATE
)
'''
create_subject_table='''
CREATE TABLE Subject (
    subjectId INTEGER PRIMARY KEY AUTOINCREMENT,
    subjectName VARCHAR(100) NOT NULL,
    type VARCHAR(20), -- Core or Elective
    classId INTEGER,
    teacherId INTEGER,
    FOREIGN KEY (classId) REFERENCES Class(classId),
    FOREIGN KEY (teacherId) REFERENCES Teacher(teacherId)
)
'''

create_exam_table='''
CREATE TABLE Exam (
    examId INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    term VARCHAR(50),
    startDate DATE,
    endDate DATE,
    classId INTEGER,
    FOREIGN KEY (classId) REFERENCES Class(classId)
)
'''

create_marks_table='''
CREATE TABLE Marks (
    marksId INTEGER PRIMARY KEY AUTOINCREMENT,
    studentId INTEGER,
    subjectId INTEGER,
    examId INTEGER,
    marksObtained DECIMAL(5,2),
    grade VARCHAR(10),
    FOREIGN KEY (studentId) REFERENCES Student(studentId),
    FOREIGN KEY (subjectId) REFERENCES Subject(subjectId),
    FOREIGN KEY (examId) REFERENCES Exam(examId)
)
'''

create_attendance_table='''
CREATE TABLE Attendance (
    attendanceId INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    status VARCHAR(10) CHECK (status IN ('Present', 'Absent')),
    studentId INTEGER,
    staffId INTEGER,
    FOREIGN KEY (studentId) REFERENCES Student(studentId),
    FOREIGN KEY (staffId) REFERENCES NonTeachingStaff(staffId)
);
'''

fetch_all_students='SELECT * FROM Student'
fetch_by_id='SELECT * FROM items WHERE id = ?'
insert_item='INSERT INTO items (name, description) VALUES (?, ?)'
delete_item_by_id='DELETE FROM items WHERE id = ?'
