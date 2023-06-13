from nodo import Nodo
from clientes import Clientes
import xml.etree.ElementTree as ET

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def add(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def modify(self, dato_nuevo, index):
        actual = self.cabeza
        indice = 0
        while actual is not None:
            if indice == index:
                actual.dato = dato_nuevo
                return
            indice += 1
            actual = actual.siguiente

    def Imprimir(self):
        actual = self.cabeza
        #print(actual.dato)
        actual.dato.imprimir()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir()
            #print(actual.dato)


    def CargarXML(self, operacion):
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\usuario.XML')
        root = tree.getroot()
        for indice, usuario in enumerate(root):
            rol = usuario.find('rol').text
            nombre = usuario.find('nombre').text
            apellido = usuario.find('apellido').text
            telefono = usuario.find('telefono').text
            correo = usuario.find('correo').text
            contrasena = usuario.find('contrasena').text
            objeto = Clientes(rol, nombre, apellido, telefono, correo, contrasena)
            if operacion == 1: # agregar datos a lista
                self.add(objeto)
            elif operacion == 2:
                self.modify(objeto, indice)
            

    def editarXML(self, posicion,rol, nombre, apellido, correo, telefono, contrasena):
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\usuario.XML')
        root = tree.getroot()
        rol1 = root.find(f"usuario[{posicion}]/rol")
        rol1.text = rol
        nombre1 = root.find(f"usuario[{posicion}]/nombre")
        nombre1.text = nombre
        apellido1 = root.find(f"usuario[{posicion}]/apellido")
        apellido1.text = apellido
        correo1 = root.find(f"usuario[{posicion}]/correo")
        correo1.text = correo
        telefono1 = root.find(f"usuario[{posicion}]/telefono")
        telefono1.text = telefono
        contrasena1 = root.find(f"usuario[{posicion}]/contrasena")
        contrasena1.text = contrasena
        tree.write(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\usuario.XML')
        self.CargarXML(2)

    def getNodo(self, correo):
        if self is None:
            print("La lista está vacía")
        else:
            actual = self.cabeza
            while actual:
                if actual.dato.correo == correo:
                  print("cierto")
                  return actual.dato
                actual = actual.siguiente
        print("mentira")
                
            


