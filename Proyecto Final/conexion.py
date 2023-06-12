import sqlite3
conn = sqlite3.connect("proyecto_final_leyes.db")
cursor = conn.cursor()


conn.execute('''CREATE TABLE Categorias
(IdCategoria INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL UNIQUE, NombreCategoria TEXT)''')

conn.execute('''CREATE TABLE Jurisdiccion
(IdJurisdiccion INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL UNIQUE, NombreJurisdiccion TEXT)''')

conn.execute('''CREATE TABLE Normativa
(IdNormativa INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL UNIQUE, TipoNormativa TEXT)''')

conn.execute("INSERT INTO Jurisdiccion (IdJurisdiccion,NombreJurisdiccion) VALUES (1,'Nacional'),(2,'Provincial')")

conn.execute("INSERT INTO Normativa (IdNormativa,TipoNormativa) VALUES (1,'Ley'),(2,'Decreto'),(3,'Resolucion')")

conn.execute("INSERT INTO Categorias (IdCategoria,NombreCategoria) VALUES (1 ,'Laboral '),(2 ,'Penal '),( 3,'Civil '),( 4,'Comercial'),( 5,'Familia y Suceciones'),(6,'Agrario y Ambiental'),( 7,'Mineria'),( 8,'Derecho informatico ')")
print ("Registro Insertado Exitosamente")

conn.execute ('''CREATE TABLE Leyes 
   (NumeroRegistro	INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
	TipoDeNormativa	INTEGER,  
	NumeroDeNormativa	TEXT,
	Fecha	DATE,
	Descripcion	TEXT,
	Categoria	INTEGER, 
	Jurisdiccion	INTEGER, 
	OrganoLegislativo	TEXT,
	PalabraClave	TEXT,
    FOREIGN KEY (TipoDeNormativa) REFERENCES Normativa (IdNormativa),
    FOREIGN KEY (Categoria) REFERENCES Categorias (IdCategoria),
    FOREIGN KEY (Jurisdiccion) REFERENCES Jurisdiccion (IdJurisdiccion)
	)''')

conn.commit()
conn.close()





