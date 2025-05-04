create_student_table='''
CREATE TABLE Student (
    studentID INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    dob DATE,
    gender VARCHAR(10),
    admissionNo VARCHAR(50) UNIQUE,
    classID INTEGER,
    sectionID INTEGER,
    parentInfo TEXT,
    FOREIGN KEY (classID) REFERENCES Class(classID),
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID)
);
'''
create_teacher_table='''
CREATE TABLE Teacher (
    teacherID INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    qualification VARCHAR(100),
    contact VARCHAR(15),
    employeeType VARCHAR(50)
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
    attendanceID INTEGER PRIMARY KEY,
    date DATE,
    studentID INTEGER,
    status VARCHAR(10),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);
'''
create_section_table='''
CREATE TABLE Section (
    sectionID INT PRIMARY KEY,
    sectionName VARCHAR(50),
    classID INT,
    classTeacherID INT,
    FOREIGN KEY (classID) REFERENCES Class(classID),
    FOREIGN KEY (classTeacherID) REFERENCES Teacher(teacherID)
);
'''
create_timetable_table='''
CREATE TABLE Timetable (
    timetableID INTEGER PRIMARY KEY,
    classID INTEGER,
    sectionID INTEGER,
    day VARCHAR(20),
    time TIME,
    subjectID INTEGER,
    teacherID INTEGER,
    FOREIGN KEY (classID) REFERENCES Class(classID),
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID),
    FOREIGN KEY (subjectID) REFERENCES Subject(subjectID),
    FOREIGN KEY (teacherID) REFERENCES Teacher(teacherID)
);
'''
create_class_table='''
CREATE TABLE Class (
    classID INTEGER PRIMARY KEY,
    className VARCHAR(50),
    academicYear VARCHAR(20)
);
'''
insert_studentdata='''
INSERT INTO Student (studentID, name, dob, gender, admissionNo, classID, sectionID, parentInfo) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
'''

fetch_all_students='SELECT * FROM Student'
fetch_all_teachers='SELECT * FROM Teacher'
fetch_all_subjects='SELECT * FROM Subject'
fetch_all_exams='SELECT * FROM Exam'
fetch_all_marks='SELECT * FROM Marks'
fetch_all_attendance='SELECT * FROM Attendance'
fetch_all_staff='SELECT * FROM NonTeachingStaff'
fetch_all_classes='SELECT * FROM Class'
fetch_all_sections='SELECT * FROM Section'

fetch_by_id='SELECT * FROM items WHERE id = ?'
insert_item='INSERT INTO items (name, description) VALUES (?, ?)'
delete_item_by_id='DELETE FROM items WHERE id = ?'
