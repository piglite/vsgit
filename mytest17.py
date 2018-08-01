from pymysql import *
settings = {
    "user":"root",
    "host":"127.0.0.1",
    "port":3306,
    "password":"110101",
    "database":"hfsql",
    "charset":"utf8"
}
conn = connect(**settings)
c = conn.cursor()
c.execute('select * from boys')
print(c.fetchall())
