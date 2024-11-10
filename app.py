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
    password="S0f1anrub10.",
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
    cantidad = request.form.get("cantidad", '')
    precio = request.form.get("precio", '')
    talle = request.form.get("talle", '')
    colores = request.form.get("colores", '')
    # Comprobar si 'prenda' tiene un valor
    if producto:
        # Insertar el valor en la base de datos
        sql_query_insert = "INSERT INTO Stock (producto, cantidad, precio, talle, colores) VALUES (%s, %s, %s, %s, %s)"
        values = (producto, cantidad, precio, talle, colores)
        cursor.execute(sql_query_insert, values)

        # Confirmar cambios en la base de datos
        mydb.commit()

        return redirect(url_for('mostrar_stock'))
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

    # Actualización de la tabla 'Stock' con los datos proporcionados
    sql = "UPDATE Stock SET producto = %s, cantidad = %s, precio = %s, talle = %s, colores = %s WHERE id = %s"
    datos = (producto_nombre, cantidad_valor, precio_valor, talle_valor, color_nombre, id)

    cursor = mydb.cursor()
    cursor.execute(sql, datos)
    mydb.commit()
    cursor.close()
    return redirect(url_for('mostrar_stock'))

@app.route('/mostrar', methods=['GET', 'POST'])
def mostrar_stock():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Stock")
    datos_prenda = cursor.fetchall()
    cursor.close()
    return render_template('index.html', Stock=datos_prenda)

@app.route('/eliminar', methods=['POST'])
def eliminar():
    id = request.form.get('id')
    
    # Validación y ejecución de la eliminación
    if id:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Stock WHERE id = %s", (id,))
        mydb.commit()
        cursor.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
