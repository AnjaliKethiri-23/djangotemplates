from django.shortcuts import render
import MySQLdb

def NEW_EMPLOYEE(request):

    con = MySQLdb.connect(
        user='root',
        host='localhost',
        password='anju-mysql'
    )

    cursor = con.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS Django_94")
    cursor.execute("USE Django_94")

    table = '''
    CREATE TABLE IF NOT EXISTS Employee (
        emp_id VARCHAR(10),
        Employee_name VARCHAR(20),
        email VARCHAR(50)
    )
    '''

    cursor.execute(table)

    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        emp_name = request.POST.get('emp_name')
        emp_email = request.POST.get('emp_email')

        data = f'''
        INSERT INTO Employee
        VALUES ('{emp_id}', '{emp_name}', '{emp_email}')
        '''

        cursor.execute(data)
        con.commit()

    return render(request, 'home.html')