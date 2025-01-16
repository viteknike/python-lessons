import cgi, html


r=cgi.FieldStorage()

a = html.escape(r.getvalue('a', ''))
b = html.escape(r.getvalue('b', ''))

message = ""
result = ""

try:
    result = float(a) + float(b)
    result = "<p>Сумма чисел равна: </p>" + str(result) + "</p>"
except ValueError:
    message = "<p style='color: red'>Вы ввели не числа</p>"

print('Content-type: text/html; charset=utf-8')
print()
print('<html><head><title>Заголовок</title></head><body style="text-align: center">')
print('<h1>Первая Web-страница!</h1>')


print('''
<form name="form" style="margin: 0 auto;" action="/cgi-bin/index.py" method="post">
    <h2>Сложение чисел</h2>'''
    + message + '''
    <label>Число 1:</label>
    <input type="text" name="a" value="''' + a + '''" />
    <br />
    <br />
    <label>Число 2:</label>
    <input type="text" name="b" value="''' + b + '''" />
    <br />
    <br />
    <button type="submit">Посчитать</button>
    ''' + result + '''
</form>''')

print('</body></html>')