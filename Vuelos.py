import sqlite3
from flask import Flask,  jsonify, request
#from flask_cors import CORS


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
            codigo INTEGER PRIMARY KEY,
            descripcion TEXT NOT NULL,
            numerovuelo INTEGER NOT NULL,
            asientoslibres INTEGER NOT NULL,
            asientostotales INTEGER NOT NULL,
            asientosocupados INTEGER NOT NULL,
            origen TEXT NOT NULL,
            destino TEXT NOT NULL,
            horariosalida INTEGER NOT NULL,
            horariollegada INTEGER NOT NULL,
            precio REAL NOT NULL
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
    def __init__(self, codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, origen, destino,  horariosalida, horariollegada, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.numerovuelo = numerovuelo
        self.asientoslibres = asientoslibres
        self.asientostotales = asientostotales
        self.asientosocupados = asientosocupados
        self.origen = origen
        self.destino = destino
        self.horariosalida = horariosalida
        self.horariollegada = horariollegada 
        self.precio = precio

    def modificar(self, nueva_descripcion, nueva_numerovuelo, nueva_asientoslibres, nueva_asientostotales, nueva_asientosocupados, nueva_origen, nueva_destino,  nueva_horariosalida, nueva_horariollegada, nueva_precio):
        self.descripcion = nueva_descripcion
        self.numerovuelo = nueva_numerovuelo
        self.asientoslibres = nueva_asientoslibres
        self.asientostotales = nueva_asientostotales
        self.asientosocupados = nueva_asientosocupados
        self.origen = nueva_origen
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

    def agregar_vuelo(self, codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, origen, destino,  horariosalida, horariollegada, precio):
        vuelo_existente = self.consultar_vuelo(codigo)
        if vuelo_existente:
            return jsonify({'message': 'Ya existe un vuelo con ese código.'}), 400
        
        nuevo_vuelo = Vuelo(codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, origen, destino,  horariosalida, horariollegada, precio)
        self.cursor.execute("INSERT INTO vuelos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, origen, destino,  horariosalida, horariollegada, precio))
        self.conexion.commit()
        return jsonify({'message': 'Vuelo agregado correctamente.'}), 200

    def consultar_vuelo(self, codigo):
        self.cursor.execute("SELECT * FROM vuelos WHERE codigo = ?", (codigo,))
        row = self.cursor.fetchone()
        if row:
            codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, origen, destino,  horariosalida, horariollegada, precio = row
            return Vuelo(codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, origen, destino,  horariosalida, horariollegada, precio)
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
            codigo, descripcion, numerovuelo, asientoslibres, asientostotales, asientosocupados, origen, destino,  horariosalida, horariollegada, precio = row
            vuelo = {'codigo': codigo, 'descripcion': descripcion, 'numerovuelo': numerovuelo, 'asientoslibres':asientoslibres, 'asientostotales': asientostotales, 'asientosocupados': asientosocupados, 'origen': origen, 'destino': destino, 'horariosalida': horariosalida, 'horariollegada': horariollegada, 'precio': precio}
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





    
x = Inventario()

#x.agregar_vuelo(6, "vuelo a Mendoza", 15, 12, 50, 45, "Buenos Aires", "Mendoza", 10, 12, 50000)
x.listar_vuelos()
