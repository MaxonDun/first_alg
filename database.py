import psycopg2
import xlwt

conn = psycopg2.connect(dbname='rainbow_database',
                        user='unicorn_user',
                        password='magical_password',
                        host='5.101.50.80',
                        port='5432')
cursor = conn.cursor()
i = 0
wb = xlwt.Workbook()
ws = wb.add_sheet('sheet1', cell_overwrite_ok=True)
ws.write(0, 0, 'fssp')
ws.write(0, 1, 'Фамилия')
ws.write(0, 2, 'Имя')
ws.write(0, 3, 'Отчество')

cursor.execute(f'SELECT fssp.fssp_person, persons.firstname, persons.secondname, '
               f'persons.surname FROM persons JOIN fssp '
               f'ON persons.id = fssp.fssp_person '
               f'ORDER BY fssp.fssp_person')
person = cursor.fetchall()
print(person)

while i < len(person):
    ws.write(i + 1, 0, person[i][0])
    ws.write(i + 1, 1, person[i][3])
    ws.write(i + 1, 2, person[i][1])
    ws.write(i + 1, 3, person[i][2])
    i += 1
    wb.save('my_data.xls')
conn.close()
