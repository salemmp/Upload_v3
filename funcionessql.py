import sqlite3
def guardarproducto_db(nombre_carpeta):
    con = sqlite3.connect('data.db')
    cursor= con.cursor()
    cursor.execute("""INSERT INTO productos (producto) VALUES (?)""",(nombre_carpeta,))
    con.commit()
    con.close()


def obtenerid_db(nombre_carpeta):
    con = sqlite3.connect('data.db')
    cursor= con.cursor()
    cursor.execute("""SELECT id from productos WHERE producto=?""",(nombre_carpeta,))
    data= cursor.fetchone()
    con.commit()
    con.close()
    return data





def guardarimg_db(url,id_producto):
    con = sqlite3.connect('data.db')
    cursor= con.cursor()
    cursor.execute("""INSERT INTO imagenes (url_img,id_producto) VALUES (?,?)""",(url,id_producto))
    con.commit()
    con.close()

def productos_sql():
    con = sqlite3.connect('data.db')
    cursor= con.cursor()
    cursor.execute("""SELECT * FROM productos""")
    data = cursor.fetchall()
    con.commit()
    con.close()

    return data


def solicitar_imagen_sql(id):
    con = sqlite3.connect('data.db')
    cursor= con.cursor()
    cursor.execute("""SELECT url_img FROM imagenes WHERE id_producto = ?""",(id,))
    data = cursor.fetchall()
    con.commit()
    con.close()

    return data
    