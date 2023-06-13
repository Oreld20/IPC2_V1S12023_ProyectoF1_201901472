from nodo_doblenlace import Nodo
import xml.etree.ElementTree as ET
from salas import Salas
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def imprimir_lista(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            actual = self.primero
            while actual is not None:
                actual.dato.imprimir()
                actual = actual.siguiente

    def imprimir_lista_reversa(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            actual = self.ultimo
            while actual is not None:
                print(actual.dato)
                actual = actual.anterior


    def CargarXML_salas(self):
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\salas.XML')
        root = tree.getroot()
        cine = root.find('cine')

        for sala in cine.findall("salas/sala"):
            numero = sala.find('numero').text
            asientos = sala.find('asientos').text
            objeto = Salas(numero, asientos)
            self.insertar_final(objeto)


    def buscar_elemento(self, dato):
        if self.esta_vacia():
            return False

        actual = self.primero
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False

            