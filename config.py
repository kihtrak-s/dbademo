DATABASE = 'schoolmgmt.db'
PORT = '5000'
def create_html_table(heading,headers,rows,num_column=0):
    #HTML headings
    html = f'''
    <html>
        <body>
            <h1>{heading}</h1>
            <table border="1">
                <thead>
                    <tr>
    '''
    for attribute in headers:
        html += f'<th>{attribute}</th>'
    html += '''
                    </tr>
                </thead>
                <tbody>
    '''
    for elements in rows:
        html += '<tr>'
        for element in elements:
            html += f'<td>{element}</td>'
        html += '</tr>'
    html += '''
                </tbody>
            </table>
        </body>
    </html>
    '''
    return html

def get_homepage():
    html = '''
    <html>
        <head>
            <title>Welcome</title>
            <script>
                async function fetchCounts() {
                    try {
                        const studentResponse = await fetch('/students/count');
                        const studentData = await studentResponse.json();
                        document.getElementById('student_count').innerText = studentData.count;

                        const teacherResponse = await fetch('/teachers/count');
                        const teacherData = await teacherResponse.json();
                        document.getElementById('teacher_count').innerText = teacherData.count;

                        const subjectResponse = await fetch('/subjects/count');
                        const subjectData = await subjectResponse.json();
                        document.getElementById('subject_count').innerText = subjectData.count;
                    } catch (error) {
                        console.error('Error fetching counts:', error);
                    }
                }
                window.onload = fetchCounts;
            </script>
        </head>
        <body>
            <h1>Welcome to the Student Management System!</h1>
            <button onclick="window.location.href='/students'">Show Student Details</button>
            <button onclick="window.location.href='/teachers'">Show Teacher Details</button>
            <button onclick="window.location.href='/attendance'">Show Attendance</button>
            <button onclick="window.location.href='/subjects'">Show Subjects</button>
            <table border="1">
                <thead>
                    <tr>
                        <th>Category</th>
                        <th>Count</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Students</td>
                        <td id="student_count">Loading...</td>
                    </tr>
                    <tr>
                        <td>Teachers</td>
                        <td id="teacher_count">Loading...</td>
                    </tr>
                    <tr>
                        <td>Subjects</td>
                        <td id="subject_count">Loading...</td>
                    </tr>
                </tbody>
            </table>
        </body>
    </html>
    '''
    return html