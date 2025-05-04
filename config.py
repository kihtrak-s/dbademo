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
