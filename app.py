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

from flask import Flask, request, render_template
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
    
    # Consultar los datos actuales de la prenda según el ID
    cursor.execute("SELECT * FROM Prenda WHERE id = %s", (id,))
    prenda = cursor.fetchone()
    cursor.close()
    
    # Pasamos los datos al formulario para editarlos
    return render_template('editar_formulario.html', prenda=prenda)

# Ruta para procesar los cambios y actualizar la base de datos
@app.route('/actualizar_prenda/<int:id>', methods=['POST'])
def actualizar_prenda(id):
    if request.method == 'POST':
        # Recibe los datos modificados del formulario
        producto = request.form['producto']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        talle = request.form['talle']
        colores = request.form['colores']
        
        # Actualizar la prenda en la base de datos
        cursor = mydb.cursor()
        sql_query_update = """
            UPDATE Prenda 
            SET producto = %s, cantidad = %s, precio = %s, talle = %s, colores = %s 
            WHERE id = %s
        """
        values = (producto, cantidad, precio, talle, colores, id)
        
        # Ejecutar el comando SQL y actualizar los datos
        cursor.execute(sql_query_update, values)
        mydb.commit()
        cursor.close()

        # Redirige a una página de confirmación o lista de prendas
        return "Prenda actualizada correctamente"  # También puedes usar redirect(url_for('otra_ruta'))
            
    mydb.commit()

@app.route('/mostrar', methods=['POST'])
def mostrar_stock():
    #conexion = mysql.connector.connect(**db_config)
    #cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM stock")
    datos_stock = cursor.fetchall()
    cursor.close()
    cursor.conexion.close()
    return render_template('index.html', stock=datos_stock)
    
    mydb.commit()


    
if __name__ == '__main__':
    app.run(debug=True)
