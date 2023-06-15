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


    def CargarXML_salas(self,operacion):
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\salas.XML')
        root = tree.getroot()
        cine = root.find('cine')

        for indice, sala in enumerate(cine.findall("salas/sala")):
            numero = sala.find('numero').text
            asientos = sala.find('asientos').text
            objeto = Salas(numero, asientos)
            if operacion == 1:
                if self.verificar_nodos_repetidos():
                    self.insertar_final(objeto)
            elif operacion == 2:
                self.modify(objeto, indice)

    def modify(self, nuevo_dato, posicion):
        if self.primero is None or posicion < 0:
            return  False

        nodo_actual = self.primero
        indice = 0
        while nodo_actual is not None:
            if indice == posicion:
                nodo_actual.dato = nuevo_dato
                return
            nodo_actual = nodo_actual.siguiente
            indice += 1


    def buscar_elemento(self, target):
        current_node = self.primero
        while current_node is not None:
            if current_node.dato.sala == target:
                return current_node.dato
            current_node = current_node.siguiente
        return None
    
    def verificar_nodos_repetidos(self):
        valores = set()

        nodo_actual = self.primero
        while nodo_actual is not None:
            if nodo_actual.dato in valores:
                return False

            valores.add(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

        return True
    
    def eliminar_elemento(self, elemento):
        if self.primero is None:
            return  # La lista está vacía, no hay nada que eliminar

        if self.primero.dato.sala == elemento:
            if self.primero == self.ultimo:
                self.primero = None
                self.ultimo = None
            else:
                self.primero = self.primero.siguiente
                self.primero.anterior = None
            return

        if self.ultimo.dato.sala == elemento:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            return

        nodo_actual = self.primero.siguiente
        while nodo_actual is not None:
            if nodo_actual.dato.sala == elemento:
                nodo_actual.anterior.siguiente = nodo_actual.siguiente
                nodo_actual.siguiente.anterior = nodo_actual.anterior
                return
            nodo_actual = nodo_actual.siguiente

            
    def editarXML_Salas(self, posicion, numero, asientos):
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\salas.XML')
        root = tree.getroot()
        cine = root.find('cine/salas')
        
        num = cine.find(f"sala[{posicion}]/numero")
        num.text = numero
        asien = cine.find(f"sala[{posicion}]/asientos")
        asien.text = asientos
        tree.write(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\salas.XML')
        self.CargarXML_salas(2)

    def nuevo_registroXML_Sala(self,numero, asientos):
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\salas.XML')
        root = tree.getroot()
        root=root.find('cines/cine/salas')
        nueva_Sala = ET.Element("sala")
        numer = ET.SubElement(nueva_Sala, 'numero')
        numer.text = numero
        asient = ET.SubElement(nueva_Sala, 'asientos')
        asient.text = asientos
        objeto = Salas(numer, asient)
        self.insertar_final(objeto)
        root.append(nueva_Sala)
        tree.write(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\salas.XML')

    def eliminar_elemento_xml_sala(self, posicion):
         # Parsear el archivo XML
        tree = ET.parse(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\salas.XML')
        root = tree.getroot()
        salas_elemento = root.find("cine/salas")
        # Obtener la lista de elementos <sala>
        salas_lista = salas_elemento.findall("sala")
            # Obtener el elemento <sala> correspondiente a la posición dada
        sala_elemento = salas_lista[int(posicion)]
            # Eliminar el elemento <sala> del árbol XML
        salas_elemento.remove(sala_elemento)
            # Guardar los cambios en el archivo XML
        tree.write(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Proyecto[IPC2]\salas.XML')
            
              

            

         
        