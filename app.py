#from flask import Flask, request, render_template

#app = Flask(__name__)

#@app.route("/")
#def index():
#    return render_template("index.html")

#@app.route("/process", methods=["POST"])
#def process():
#    prenda=request.form.get("prenda")
#    return "La prenda agregada es %s"  % (prenda)

#sql_query_insert = "INSERT INTO Stock (prenda) VALUES (%s)"
#values = (prenda)
#cursor.execute(sql_query_insert, values)

    # Confirmar cambios en la base de datos
#mydb.commit()

from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = "jhfgk"

# Configura la conexión a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="juli",
    password="45875403",
    database="easily_store"
)
cursor = mydb.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    # Obtener el valor de 'prenda' del formulario
    producto = request.form.get("producto", '')
    cantidad=request.form.get("cantidad", '')
    precio=request.form.get("precio", '')
    talle=request.form.get("talle", '')
    colores=request.form.get("colores", '')
    # Comprobar si 'prenda' tiene un valor
    if producto:
        # Insertar el valor en la base de datos
        sql_query_insert = "INSERT INTO Stock (producto, cantidad, precio, talle, colores) VALUES (%s, %s, %s, %s,%s)"
        values = (producto, cantidad, precio, talle, colores)
        cursor.execute(sql_query_insert, values)

        # Confirmar cambios en la base de datos
        mydb.commit()

        return f"La prenda agregada es: {producto},{cantidad}, {precio}, {talle}, {colores}"
    else:
        return "No se ha proporcionado ninguna prenda..."

@app.route("/edit/<int:id>", methods=["GET"])
def edit(id):
    cursor = mydb.cursor(dictionary=True)
    # Consulta la prenda específica
    cursor.execute("SELECT * FROM Stock WHERE id = %s", (id,))
    producto = cursor.fetchone()
    cursor.close()
    
    # Verifica si la prenda fue encontrada
    if producto is None:
        return "Producto no encontrado o no cargado correctamente.", 404
    
    # Renderiza el formulario de edición con los datos de la prenda
    return render_template('index.html', producto=producto)

@app.route('/actualizar_producto/<int:id>', methods=['POST'])
def actualizar_producto(id):
    producto_nombre = request.form['producto']
    cantidad_valor = request.form['cantidad']
    precio_valor = request.form['precio']
    talle_valor = request.form['talle'] 
    color_nombre = request.form['colores']

    sql = "UPDATE producto SET producto = %s, cantidad = %s, precio = %s, talle = %s, colores = %s WHERE id = %s"
    datos = (id, producto_nombre, cantidad_valor, precio_valor, talle_valor, color_nombre)

    cursor = mydb.cursor()
    cursor.execute(sql, datos)
    mydb.commit()
    return redirect(url_for('mostrar_stock'))
    #mydb.commit()

@app.route('/mostrar', methods=['GET', 'POST'])
def mostrar_stock():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Stock")
    datos_prenda = cursor.fetchall()
    cursor.close()
    print(datos_prenda)
    return render_template('index.html', Stock=datos_prenda)

@app.route('/eliminar', methods=['POST'])
def eliminar():
    id = request.form.get('id')
    
    # Usa la conexión ya existente sin llamarla como función
    cursor = mydb.cursor()

    # Validación y ejecución de la eliminación
    if id:
        cursor.execute("DELETE FROM Stock WHERE id = %s", (id,))
        mydb.commit()
    
    cursor.close()
    return redirect(url_for('index'))

"""
@app.route('/eliminar', methods=['POST'])
def eliminar():
    id = request.form.get('id')  # Obtenemos el valor del campo "id" en el formulario
    if id:  # Verificamos que el ID no esté vacío
        conexion = mysql.connector.connect(mydb)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM stock WHERE id = %s", (id,))
        conexion.commit()
        cursor.close()
        conexion.close()
    return redirect(url_for('index'))
"""

if __name__ == '__main__':
    app.run(debug=True)
