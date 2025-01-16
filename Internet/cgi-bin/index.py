import cgi, html

r = cgi.FieldStorage()

login = r.getvalue('login', '')
password = r.getvalue('password', '')

message = ''
auth = '''
<form method="post">
    <label>Логин</label>
    <input type="text" name="login" value="''' + login + '''" />
    <br />
    <br />
    <label>Пароль</label>
    <input type="text" name="password" value="''' + password + '''" />
    <br />
    <br />
    <button type="submit">Войти</button>
    '''

if login == 'Admin' and password == '123':
    auth = '<h1>Добро пожаловать, Администратор!</h1>'
else:
    message = "<p style='color: red'>Неверный логин или пароль</p>"

print('Content-type: text/html; charset=utf-8')
print()
print('<html><head><title>Заголовок</title></head><body style="text-align: center">')
print('<h1 style="text-align: center;">Авторизация</h1>')
print(message)
print(auth)
print('</body></html>')
