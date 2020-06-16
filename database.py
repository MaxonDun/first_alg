import psycopg2
import xlwt


conn = psycopg2.connect(dbname='rainbow_database',
                        user='unicorn_user',
                        password='magical_password',
                        host='5.101.50.80',
                        port='5432')
cursor = conn.cursor()
cursor.execute('SELECT fssp_person FROM fssp')
record = cursor.fetchall()
i = 0
wb = xlwt.Workbook()
ws = wb.add_sheet('sheet1', cell_overwrite_ok=True)
ws.write(0, 0, 'fssp')
ws.write(0, 1, 'Фамилия')
ws.write(0, 2, 'Имя')
ws.write(0, 3, 'Отчество')

while i < len(record) :
    cursor.execute(f'SELECT surname,firstname,secondname FROM persons WHERE id={record[i][0]}')
    person = cursor.fetchall()
    print(record[i][0], person[0][0], person[0][1], person[0][2])
    ws.write(i + 1, 0, record[i][0])
    ws.write(i + 1, 1, person[0][0])
    ws.write(i + 1, 2, person[0][1])
    ws.write(i + 1, 3, person[0][2])
    i += 1
    wb.save('my_data.xls')
conn.close()

