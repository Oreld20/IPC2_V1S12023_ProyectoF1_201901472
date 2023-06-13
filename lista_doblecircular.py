from nodo_doblecircular import Nodo
import xml.etree.ElementTree as ET
from peliculas import Pelicula
class ListaDoblementeEnlazadaCircular:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.primero = nuevo_nodo
        else:
            ultimo = self.primero.anterior
            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = ultimo
            self.primero.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo
            self.primero = nuevo_nodo

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.primero = nuevo_nodo
        else:
            ultimo = self.primero.anterior
            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = ultimo
            self.primero.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo

    def imprimir_Categoria(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            actual = self.primero
            actual.dato.imprimir_categoria()
            while True:
                actual = actual.siguiente
                actual.dato.imprimir_categoria()
                if actual == self.primero:
                    break

    def imprimir_pelicula(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            actual = self.primero
            actual.dato.imprimir_pelicula()
            while True:
                actual = actual.siguiente
                actual.dato.imprimir_pelicula()
                if actual == self.primero:
                    break


    def CargarXML_Categorias(self):
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\categorias_peliculas.XML')
        root = tree.getroot()
        for categoria in root.findall("categoria"):
            nombre = categoria.find('nombre').text
            print(f"Nombre: {nombre.strip()}")
            pelicula = categoria.find('peliculas')

            for peli in pelicula.findall('pelicula'):
                titulo = peli.find('titulo').text
                director = peli.find('director').text
                anio = peli.find('anio').text
                fecha = peli.find('fecha').text
                hora = peli.find('hora').text
                objeto = Pelicula(nombre, titulo, director, anio, fecha, hora)
                self.insertar_final(objeto)


    def buscar_elemento(self, dato):
        if self is None:
            return False

        actual = self.primero
        while True:
            if actual.dato.titulo == dato:
                return actual.dato
            actual = actual.siguiente
            if actual == self.primero:
                break

        return False
            
        







            