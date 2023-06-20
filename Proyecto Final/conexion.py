import sqlite3

class baseDeDatos ():
    def ejecutar_conexion(self,consulta,parametros):
        conn = sqlite3.connect("proyecto_final_leyes.db")
        cursor = conn.cursor()
        cursor.execute(consulta, parametros)
        conn.commit()
        conn.close()

#.........................................................
#ACA CREAMOS LA BASE DE DATOS, LAS TABLAS Y LOS DATOS EN LAS TABLAS MEDIANTE CÓDIGO.
#UNA VEZ CREADOS, SE COMENTA PORQUE SINO CADA VEZ QUE EJECUTEMOS VA A DAR ERROR PORQUE YA ESTÁN HECHAS.
#..................................................................
# conn = sqlite3.connect("proyecto_final_leyes.db") #2)se crea la base de datos. Generar una conexion indicando por parametro el nombre de la base de datos elegido. Siempre terminar .db
# cursor = conn.cursor()  #a) ahora se van a crear las  tablas. Lo primero es crear el cursor que elija esa bd creada.

#b) asi se crea la primera tabla. Se coloca si no existe para que nose dupliquen.
# una vez creadas, se comenta porque sino crea nuevas bases de datos. Ya está creada con la primera ejecución.
# cursor.execute("CREATE TABLE IF NOT EXISTS Categorias" "(IdCategoria INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL UNIQUE,\
#                 NombreCategoria TEXT)")

# cursor.execute("CREATE TABLE IF NOT EXISTS Jurisdiccion" "(IdJurisdiccion INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL UNIQUE,\
#                 NombreJurisdiccion TEXT)")

# cursor.execute("CREATE TABLE IF NOT EXISTS Normativa" "(IdNormativa INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL UNIQUE,\
#                 NombreNormativa TEXT)")

# cursor.execute("CREATE TABLE IF NOT EXISTS Leyes" "(NumeroRegistro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,\
#              TipoDeNormativa INTEGER, NumeroDeNormativa TEXT,\
#              Fecha DATE,Descripcion TEXT,Categoria INTEGER,Jurisdiccion INTEGER,OrganoLegislativo TEXT, PalabraClave TEXT,\
#              FOREIGN KEY (TipoDeNormativa) REFERENCES Normativa (IdNormativa),\
#              FOREIGN KEY (Categoria) REFERENCES Categorias (IdCategoria),\
#              FOREIGN KEY (Jurisdiccion) REFERENCES Jurisdiccion (IdJurisdiccion))")
#............................................................
#Se cargan los valores, se ejecuta y se comenta para que no se carguen nuevamente.

# cursor.execute("INSERT INTO Jurisdiccion (IdJurisdiccion,NombreJurisdiccion)\
#                  VALUES (1,'Nacional'),(2,'Provincial')")

# cursor.execute("INSERT INTO Normativa (IdNormativa,NombreNormativa)\
#                  VALUES (1,'Ley'),(2,'Decreto'),(3,'Resolucion')")

# cursor.execute("INSERT INTO Categorias (IdCategoria,NombreCategoria) \
#                 VALUES (1 ,'Laboral '),(2 ,'Penal '),( 3,'Civil '),( 4,'Comercial'),( 5,'Familia y Suceciones'),(6,'Agrario y Ambiental'),( 7,'Mineria'),( 8,'Derecho informatico ')")


# conn.commit() # este método guarda los cambios realizados 
# conn.close() #3) se cierra la conexion. Asi son los 3 pasoss basicos para conectarse y crear una base de datos.
