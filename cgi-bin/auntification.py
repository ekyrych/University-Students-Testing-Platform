import cgi,sqlite3,login,Blocks,Styles
from Structure import redirect
#sing in procedure

conn = sqlite3.connect("cgi-bin\Server.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

form = cgi.FieldStorage()
login = form['user'].value
password=form['password'].value

for userlog, userpass in cursor.execute('SELECT User_Name,User_Password from Users'):
        if userlog==login and userpass==password:
            redirect('http://127.0.0.1/cgi-bin/Admin.py')
        else:
            print('Content-type: text/html\n')
            print(ErorLogin%(Styles.style))
conn.close()

