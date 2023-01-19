from time import sleep
from bottle import route, run, template
import mariadb
import sys
import os


HOST = os.getenv("MYSQL_HOST", "mysql")
USER = os.getenv('MYSQL_USER')
PASSWORD = os.getenv('MYSQL_PASSWORD')
DATABASE = os.getenv('MYSQL_DATABASE')

try:
    conn = mariadb.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=3306,
        database=DATABASE

    )
except mariadb.Error as e:
    print(f"Impossible de se connecter{e}")
    sys.exit(1)

cur: any = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT)")

for i in range(10):

    print(f'Insérer un produit{i}')

    cur.execute(
        "INSERT INTO products (name, price) VALUES (?,?)", ('PRODUCT ' + str(i), i * 10))


@route('/')
def listAll():
    cur.execute("SELECT * FROM products")

    rows = cur.fetchall()
    res = ''

    for row in rows:
        res += f'<li>ID {row[0]} Name {row[1]} Price {row[2]}</li>'
    return res


@route('/<id>')
def get(id: int):
    cur.execute(f"SELECT * FROM products WHERE id='{id}'")
    row = cur.fetchone()

    if row is None:
        return f"{id} impossible à trouver"

    print(f'Produit trouvé {row is None}')
    print(row)

    return f"""

    Nom: <b>{row[0]}</b><br>
    Id: <b>{row[1]}</b><br>
    Prix: <b>{row[2]}</b><br>
    """
    print(f"nom: {name}, id: {id}, prix: {price}")


@ route('/insert/<name>/<price>')
def insert(name: str, price: int):

    cur.execute("INSERT INTO products (name, price) VALUES (?,?)", (name, price))
    conn.commit()

    return template("""
    nom: <b>{{name}}</b><br>
    prix: <b>{{price}}</b><br>
    """, name=name, price=price)


if __name__ == "__main__":

    run(host='0.0.0.0', port=8080,
        server='paste', debug=True, reloader=True)
