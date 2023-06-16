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
        if operacion == 1:
            self.cabeza=None
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
            if operacion == 1:
                if self.verificar_nodos_repetidos():
                    self.add(objeto)
            elif operacion == 2:
                self.modify(objeto, indice)
            

    def editarXML(self, posicion, rol, nombre, apellido, correo, telefono, contrasena):
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\usuario.XML')
        root = tree.getroot()
        rol1 = root.find(f"usuario[{posicion}]/rol")
        rol1.text = rol
        nombre1 = root.find(f"usuario[{posicion}]/nombre")
        nombre1.text = nombre
        apellido1 = root.find(f"usuario[{posicion}]/apellido")
        apellido1.text = apellido
        telefono1 = root.find(f"usuario[{posicion}]/telefono")
        telefono1.text = telefono
        correo1 = root.find(f"usuario[{posicion}]/correo")
        correo1.text = correo
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


    def nuevo_registroXML(self, ro , nombr, apellid, telefon, corre, contrasen):
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\usuario.XML')
        root = tree.getroot()
        nueva_persona = ET.Element("usuario")
        rol = ET.SubElement(nueva_persona, 'rol')
        rol.text = ro
        nombre = ET.SubElement(nueva_persona, 'nombre')
        nombre.text = nombr
        apellido = ET.SubElement(nueva_persona, 'apellido')
        apellido.text = apellid
        telefono = ET.SubElement(nueva_persona, 'telefono')
        telefono.text = telefon
        correo = ET.SubElement(nueva_persona, 'correo')
        correo.text = corre
        contrasena = ET.SubElement(nueva_persona, 'contrasena')
        contrasena.text = contrasen
        objeto = Clientes(rol.text, nombre.text, apellido.text, telefono.text, correo.text, contrasena.text)
        self.add(objeto)
        root.append(nueva_persona)
        tree.write(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\usuario.XML')

    def eliminar_nodo(self, dato):
        if self.cabeza is None:
            return False

        if self.cabeza.dato.correo == dato:
            self.cabeza = self.cabeza.siguiente
            return
        nodo_actual = self.cabeza
        nodo_anterior = None

        while nodo_actual is not None:
            if nodo_actual.dato.correo == dato:
                break
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        if nodo_actual is None:
            return False
        nodo_anterior.siguiente = nodo_actual.siguiente
        nodo_actual.siguiente = None
                
    def verificar_nodos_repetidos(self):
        valores = set() 

        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato in valores:
                return False  # Nodo repetido encontrado

            valores.add(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

        return True  # No se encontraron nodos repetidos
    
    def eliminar_elemento_xml(self,correo):
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\usuario.XML')
        root = tree.getroot()
            # Buscar el usuario por el correo
        for usuario in root.findall('usuario'):
            correo_usuario = usuario.find('correo').text
            if correo_usuario == correo:
                # Eliminar el usuario
                root.remove(usuario)

        tree.write(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\usuario.XML')


    
            


