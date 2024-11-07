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

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # Obtener los valores del formulario
        id_prenda = request.form.get("id_prenda", '')
        producto = request.form.get("producto", '')
        cantidad=request.form.get("cantidad", '')
        precio=request.form.get("precio", '')
        talle=request.form.get("talle", '')
        colores=request.form.get("colores", '')
        # Comprobar si 'id_prenda' tiene un valor
        if id_prenda:
            # Actualizar los valores en la base de datos
            sql_query = "SELECT * FROM" + sql_query + " WHERE" 
    mydb.commit()

@app.route('/mostrar', methods=['POST'])
def mostrar_stock():
    #conexion = mysql.connector.connect(**db_config)
    #cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM stock")
    datos_stock = cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template('index.html', stock=datos_stock)

    
if __name__ == '__main__':
    app.run(debug=True)
