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


    def modificar_asientos(self, nueva_asientoslibres):
        self.asientoslibres = nueva_asientoslibres



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

    #    nuevo_vuelo = Vuelo(codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio)
    #    self.cursor.execute("INSERT INTO vuelos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio))
     #   self.conexion.commit()
      #  return jsonify({'message': 'Vuelo agregado correctamente.'}), 200

    def consultar_vuelo(self, codigo):
        self.cursor.execute("SELECT * FROM vuelos WHERE codigo = ?", (codigo,))
        row = self.cursor.fetchone()
        if row:
            codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio = row
            return Vuelo(codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, codigoorigen, origen, codigodestino, destino,  horariosalida, horariollegada, precio)
        return False



   # def modificar_vuelo(self, codigo, asientosreserva):
    #    vuelo = self.consultar_vuelo(codigo)
    #    nueva_asientoslibres = vuelo.asientoslibres - asientosreserva
    #    if vuelo:
    #        vuelo.modificar_asientos(nueva_asientoslibres)
    #        self.cursor.execute("UPDATE vuelos SET asientoslibres = ? WHERE codigo = ?",
    #                            (nueva_asientoslibres, codigo))
    #        self.conexion.commit()
    #        return jsonify({'message': 'Reserva realizada correctamente.'}), 200
    #    return jsonify({'message': 'Reserva no realizada.'}), 404


    def modificar_vuelo(self, codigo, asientosreserva):
        vuelo = self.consultar_vuelo(codigo)
        nueva_asientoslibres = vuelo.asientoslibres - asientosreserva
        if vuelo.asientoslibres < asientosreserva:
            return jsonify({'message': 'No se puede realizar la reserva'}), 404
        elif vuelo.asientoslibres > asientosreserva:
            if vuelo:
                vuelo.modificar_asientos(nueva_asientoslibres)
                self.cursor.execute("UPDATE vuelos SET asientoslibres = ? WHERE codigo = ?",
                                    (nueva_asientoslibres, codigo))
                self.conexion.commit()
                return jsonify({'message': 'Reserva realizada correctamente.'}), 200
            return jsonify({'message': 'Reserva no realizada.'}), 404
        else:
            inventario.eliminar_vuelo(codigo)
            return jsonify({'message': 'Vuelo eliminado.'}), 404



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


    def listar_vuelos(self):
        self.cursor.execute("SELECT * FROM vuelos")
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

class Reserva:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()
        self.items = []

    def agregar(self, codigo, asientosreserva, inventario):
        vuelo = inventario.consultar_vuelo(codigo)
        if vuelo is None:
            return jsonify({'message': 'El vuelo no existe.'}), 404
        if vuelo.asientoslibres < asientosreserva:
            return jsonify({'message': 'No se puede realizar la reserva.'}), 400

        for item in self.items:
            if item.codigo == codigo:
                item.asientoslibres += asientosreserva
                self.cursor.execute("UPDATE vuelos SET asientoslibres = asientoslibres - ? WHERE codigo = ?",
                                    (asientosreserva, codigo))
                self.conexion.commit()
                return jsonify({'message': 'Reserva agregada correctamente.'}), 200

        nuevo_item = Vuelo(codigo, vuelo.descripcion, vuelo.numerovuelo, asientosreserva, vuelo.asientostotales, vuelo.asientosocupados, vuelo.codigoorigen, vuelo.origen, vuelo.codigodestino, vuelo.destino,  vuelo.horariosalida, vuelo.horariollegada, vuelo.precio)
        self.items.append(nuevo_item)
        return jsonify({'message': 'Producto agregado al carrito correctamente.'}), 200


    def mostrar(self):
        vuelos_reserva = []
        for item in self.items:
            reserva = {'codigo': item.codigo, 'descripcion': item.descripcion, 'numerovuelo': item.numerovuelo, 'asientoslibres': item.asientoslibres, 'asientostotales': item.asientostotales, 'asientosocupados': item.asientosocupados, 'codigoorigen': item.codigoorigen, 'origen': item.origen, 'codigodestino': item.codigodestino, 'destino': item.destino, 'horariosalida': item.horariosalida, 'horariollegada': item.horariollegada, 'precio': item.precio}
            vuelos_reserva.append(reserva)
        return jsonify(vuelos_reserva), 200


# -------------------------------------------------------------------
# Configuración y rutas de la API Flask
# -------------------------------------------------------------------

app = Flask(__name__)
CORS(app)

reserva = Reserva()         # Instanciamos una reserva
inventario = Inventario()   # Instanciamos un inventario
#inventario.agregar_vuelo("LA515", "Vuelo a Catamarca", "B-747", 15, 60, 45, "CNQ", "Corrientes", "CTC", "Catamarca", "17:05", "19:15", "$7800")





@app.route('/vuelos/<valorida>/<valorvuelta>', methods=['PUT'])
def modificar_vuelo_ida(valorida, valorvuelta):
    valorida = request.json.get('valorida')
    valorvuelta = request.json.get('valorvuelta')
    asientosreserva = request.json.get('asientos')
    codigos = [valorida, valorvuelta]
    for codigo in codigos:
        reserva.agregar(codigo, asientosreserva, inventario)
    return jsonify({'message': 'Vuelo no encontrado.'}), 200

@app.route('/reserva', methods=['GET'])
def obtener_reserva():
    return reserva.mostrar()

@app.route('/vuelos/<codigoorigen>/<codigodestino>', methods=['GET'])
def obtener_vuelo_ida(codigoorigen, codigodestino):
    return inventario.listar_vuelos_ida(codigoorigen, codigodestino)


@app.route('/vuelos/<codigodestino>/<codigoorigen>', methods=['GET'])
def obtener_vuelo_vuelta(codigodestino, codigoorigen):
    return inventario.listar_vuelos_vuelta(codigodestino, codigoorigen)


@app.route('/vuelos', methods=['GET'])
def obtener_vuelos():
    return inventario.listar_vuelos()

@app.route('/')
def index():
    return ("<h1>API de reserva de vuelos 1<h1>")

if __name__ == '__main__':
    app.run()
