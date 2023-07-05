import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS


# Configurar la conexión a la base de datos SQLite
DATABASE = 'inventariovuelos.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'productos' si no existe
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vuelos (
            codigo TEXT PRIMARY KEY,
            descripcion TEXT NOT NULL,
            numerovuelo TEXT NOT NULL,
            asientoslibres INTEGER NOT NULL,
            asientostotales INTEGER NOT NULL,
            asientosocupados INTEGER NOT NULL,
            codigoorigen TEXT NOT NULL,
            origen TEXT NOT NULL,
            codigodestino TEXT NOT NULL,
            destino TEXT NOT NULL,
            horariosalida TEXT NOT NULL,
            horariollegada TEXT NOT NULL,
            precio TEXT NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Verificar si la base de datos existe, si no, crearla y crear la tabla
def create_database():
    conn = sqlite3.connect(DATABASE)
    conn.close()
    create_table()

# Crear la base de datos y la tabla si no existen
create_database()

# -------------------------------------------------------------------
# Definimos la clase "Vuelo"
# -------------------------------------------------------------------
class Vuelo:
    def __init__(self, codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.numerovuelo = numerovuelo
        self.asientoslibres = asientoslibres
        self.asientostotales = asientostotales
        self.asientosocupados = asientosocupados
        self.codigoorigen = codigoorigen
        self.origen = origen
        self.codigodestino = codigodestino
        self.destino = destino
        self.horariosalida = horariosalida
        self.horariollegada = horariollegada
        self.precio = precio

    def modificar(self, nueva_descripcion, nueva_numerovuelo, nueva_asientoslibres, nueva_asientostotales, nueva_asientosocupados, nueva_codigoorigen, nueva_origen, nueva_codigodestino, nueva_destino,  nueva_horariosalida, nueva_horariollegada, nueva_precio):
        self.descripcion = nueva_descripcion
        self.numerovuelo = nueva_numerovuelo
        self.asientoslibres = nueva_asientoslibres
        self.asientostotales = nueva_asientostotales
        self.asientosocupados = nueva_asientosocupados
        self.codigoorigen = nueva_codigoorigen
        self.origen = nueva_origen
        self.codigodestino = nueva_codigodestino
        self.destino = nueva_destino
        self.horariosalida = nueva_horariosalida
        self.horariollegada = nueva_horariollegada
        self.precio = nueva_precio

# -------------------------------------------------------------------
# Definimos la clase "Inventario"
# -------------------------------------------------------------------
class Inventario:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()

    def agregar_vuelo(self, codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio):
        vuelo_existente = self.consultar_vuelo(codigo)
        if vuelo_existente:
            return jsonify({'message': 'Ya existe un vuelo con ese código.'}), 400

        nuevo_vuelo = Vuelo(codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio)
        self.cursor.execute("INSERT INTO vuelos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio))
        self.conexion.commit()
        return jsonify({'message': 'Vuelo agregado correctamente.'}), 200

    def consultar_vuelo(self, codigoorigen):
        self.cursor.execute("SELECT * FROM vuelos WHERE codigoorigen= ?", (codigoorigen,))
        row = self.cursor.fetchone()
        if row:
            codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio = row
            return Vuelo(codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio)
        return None

    def modificar_vuelo(self, codigo, nueva_descripcion, nueva_numerovuelo, nueva_asientoslibres, nueva_asientostotales, nueva_asientosocupados, nueva_origen, nueva_destino,  nueva_horariosalida, nueva_horariollegada, nueva_precio):
        vuelo = self.consultar_vuelo(codigo)
        if vuelo:
            vuelo.modificar(nueva_descripcion, nueva_numerovuelo, nueva_asientoslibres, nueva_asientostotales, nueva_asientosocupados, nueva_origen, nueva_destino,  nueva_horariosalida, nueva_horariollegada, nueva_precio)
            self.cursor.execute("UPDATE vuelos SET descripcion = ?, numerovuelo = ?, asientoslibres = ?, asientostotales = ?, asientosocupados = ?, origen = ?, destino = ?, horariosalida = ?, horariollegada = ?, precio= ? WHERE codigo = ?",
                                (nueva_descripcion, nueva_numerovuelo, nueva_asientoslibres, nueva_asientostotales, nueva_asientosocupados, nueva_origen, nueva_destino,  nueva_horariosalida, nueva_horariollegada, nueva_precio, codigo))
            self.conexion.commit()
            return jsonify({'message': 'Vuelo modificado correctamente.'}), 200
        return jsonify({'message': 'Vuelo no encontrado.'}), 404

    def listar_vuelos(self):
        self.cursor.execute("SELECT * FROM vuelos")
        rows = self.cursor.fetchall()
        vuelos = []
        for row in rows:
            codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio = row
            vuelo = {'codigo': codigo, 'descripcion': descripcion, 'numerovuelo': numerovuelo, 'asientoslibres':asientoslibres, 'asientostotales': asientostotales, 'asientosocupados': asientosocupados, 'codigoorigen': codigoorigen, 'origen': origen, 'codigodestino': codigodestino, 'destino': destino, 'horariosalida': horariosalida, 'horariollegada': horariollegada, 'precio': precio}
            vuelos.append(vuelo)
        return jsonify(vuelos), 200


    def listar_vuelos_ida(self, codigoorigen, codigodestino):
        self.cursor.execute("SELECT * FROM vuelos WHERE codigoorigen= ? AND codigodestino = ?", (codigoorigen, codigodestino))
        rows = self.cursor.fetchall()
        vuelos = []
        for row in rows:
            codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio = row
            vuelo = {'codigo': codigo, 'descripcion': descripcion, 'numerovuelo': numerovuelo, 'asientoslibres':asientoslibres, 'asientostotales': asientostotales, 'asientosocupados': asientosocupados, 'codigoorigen': codigoorigen, 'origen': origen, 'codigodestino': codigodestino, 'destino': destino, 'horariosalida': horariosalida, 'horariollegada': horariollegada, 'precio': precio}
            vuelos.append(vuelo)
        return jsonify(vuelos), 200

    def listar_vuelos_vuelta(self, codigodestino, codigoorigen):
        self.cursor.execute("SELECT * FROM vuelos WHERE codigodestino= ? AND codigoorigen = ?", (codigodestino, codigoorigen))
        rows = self.cursor.fetchall()
        vuelos = []
        for row in rows:
            codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio = row
            vuelo = {'codigo': codigo, 'descripcion': descripcion, 'numerovuelo': numerovuelo, 'asientoslibres':asientoslibres, 'asientostotales': asientostotales, 'asientosocupados': asientosocupados, 'codigoorigen': codigoorigen, 'origen': origen, 'codigodestino': codigodestino, 'destino': destino, 'horariosalida': horariosalida, 'horariollegada': horariollegada, 'precio': precio}
            vuelos.append(vuelo)
        return jsonify(vuelos), 200




    def eliminar_vuelo(self, codigo):
        self.cursor.execute("DELETE FROM vuelos WHERE codigo = ?", (codigo,))
        if self.cursor.rowcount > 0:
            self.conexion.commit()
            return jsonify({'message': 'Vuelo eliminado correctamente.'}), 200
        return jsonify({'message': 'Vuelo no encontrado.'}), 404

# -------------------------------------------------------------------
# Definimos la clase "Reserva vuelo"
# -------------------------------------------------------------------









# -------------------------------------------------------------------
# Configuración y rutas de la API Flask
# -------------------------------------------------------------------

app = Flask(__name__)
CORS(app)

#carrito = Carrito()         # Instanciamos un carrito
inventario = Inventario()   # Instanciamos un inventario
#inventario.agregar_vuelo("LA515", "Vuelo a Catamarca", "B-747", 15, 60, 45, "CNQ", "Corrientes", "CTC", "Catamarca", "17:05", "19:15", "$7800")

@app.route('/vuelos/<codigoorigen>/<codigodestino>', methods=['GET'])
def obtener_vuelo_ida(codigoorigen, codigodestino):
    return inventario.listar_vuelos_ida(codigoorigen, codigodestino)
   # vuelo = inventario.listar_vuelos_ida(codigoorigen, codigodestino)
   # if vuelo:
       # return jsonify({
      #      'codigo': vuelo.codigo,
     #       'horariosalida': vuelo.horariosalida,
     #       'horariollegada': vuelo.horariollegada,
     #       'codigoorigen': vuelo.codigoorigen,
     #       'origen': vuelo.origen,
     #       'codigodestino': vuelo.codigodestino,
     #       'destino': vuelo.destino,
     #       'precio': vuelo.precio,
     #       'asientoslibres': vuelo.asientoslibres,
     #       'numerovuelo': vuelo.numerovuelo
     #   }), 200
   # return jsonify({'message': 'Producto no encontrado.'}), 404

@app.route('/vuelos/<codigodestino>/<codigoorigen>', methods=['GET'])
def obtener_vuelo_vuelta(codigodestino, codigoorigen):
    return inventario.listar_vuelos_vuelta(codigodestino, codigoorigen)




@app.route('/vuelos', methods=['GET'])
def obtener_vuelos():
    return inventario.listar_vuelos()

@app.route('/')
def index():
    return ("<h1>API de vuelos a laquiaca<h1>")

if __name__ == '__main__':
    app.run()