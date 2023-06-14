from lista_enlazada import ListaEnlazada
from lista_doblecircular import ListaDoblementeEnlazadaCircular
from lista_doblenlazada import ListaDoblementeEnlazada
from clientes import Clientes
import xml.etree.ElementTree as ET
Usuarios=[]
Voletos=[]

lista_clientes = ListaEnlazada()
lista_Genero = ListaDoblementeEnlazadaCircular()
lista_salas = ListaDoblementeEnlazada()
No_Voleto = "USACIPC2_201901472_0"






def Menu():
    print("----------------------")
    print("1. Iniciar sesion")
    print("2. Registrar usuario")
    print("3. Ver listado de peliculas")
    print("4. Ver listado de usuarios")
    print("5. Salir")
    opcion = 0
    opcion = input("Ingrese el numero correspondiente a la opcion: ")
    
    if opcion == "1":
        print("Iniciar sesion en el sistema")
        login()
    
    elif opcion == "2":
        print("Registrar un usuario")
        agregar_cliente()
    
    elif opcion == "3":
        print("Ver listado de peliculas")
        lista_Genero.imprimir_pelicula()
    
    elif opcion == "4":
        print("Ver listado de usuarios")
        mostrar_clientes()
    
    elif opcion == "5":
        print("Salir del sistema")
        return False
    
    else:
        print("Opcion invalida")
        Menu()
        
def login():
    print("-----------------------------------------")
    correo = input("Ingrese su nombre de correo: ")
    password = input("Ingrese su contraseña: ")
    nodo_usuarios=lista_clientes.getNodo(correo)
    
    if correo == "administrador" and password =="201901472":
        Menu_Administrador()
    
    elif nodo_usuarios.rol =="administrador":
        print("si ingreso")
        if nodo_usuarios.correo == correo and nodo_usuarios.contrasena == password:
            Menu_Administrador()
    
    elif nodo_usuarios.rol =="cliente":
        print("si ingreso")
        if nodo_usuarios.correo == correo and nodo_usuarios.contrasena == password:
            Menu_Cliente()
    Menu()

def agregar_cliente():
    rol = "cliente"
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    telefono = int(input("Ingrese el telefono del cliente: "))
    correo = input("Ingrese el correro electronico del cliente: ")
    contreasena = input("Ingrese la contraseña del cliente: ")
    lista_clientes.nuevo_registroXML(rol, nombre, apellido, telefono, correo, contreasena)
    print("Cliente agregado correctamente.")
    Menu()

def mostrar_clientes():
    lista_clientes.Imprimir()  
    Menu()

def Menu_Cliente():
    print("1. Ver listado de peliculas")
    print("2. Ver listado de peliculas favoritas")
    print("3. Comprar voletos")
    print("4. Historial de voletos comprados")
    print("5. volver al menu")
    opcion = 0
    opcion = input("Ingrese el numero correspondiente a la opcion: ")
    
    if opcion == "1":
        print("Listado de peliculas")
        lista_Genero.imprimir_pelicula()
    
    elif opcion == "2":
        print("Listado de peliculas favoritas")
    
    elif opcion == "3":
        print("Comprar voletos")
        comprar_voletos()
    
    elif opcion == "4":
        print("Historial de voletos comprados")
        historial_voletos()
    
    elif opcion == "5":
        print("volver")
        Menu()
    
    else:
        print("Opcion invalida")
        Menu()

def Menu_Administrador():
    print("1. Cargar XML de Clientes")
    print("2. Cargar XML de peliculas")
    print("3. Cargar XML de Salas")
    print("4. Gestionar clientes")
    print("5. añadir cliente")
    print("6. Gestionar Peliculas")
    print("7. Gestionar Salas")
    print("8. Eliminar cliente")
    print("9. Volver")
    opcion = 0
    opcion = input("Ingrese el numero correspondiente a la opcion: ")
    
    if opcion == "1":
        print("Cargando XML de Clientes...")
        lista_clientes.CargarXML(1)
        lista_clientes.Imprimir()
        Menu_Administrador()
        print("XML de Clientes cargado")
    
    elif opcion == "2":
        print("Cargar XML de peliculas")
        lista_Genero.CargarXML_Categorias()
        lista_Genero.imprimir_Categoria()
        Menu_Administrador()
    
    elif opcion == "3":
        print("Cargar XML de salas")
        lista_salas.CargarXML_salas()
        lista_salas.imprimir_lista()
        Menu_Administrador()
    
    elif opcion == "4":
        print("Editar clientes")
        lista_clientes.Imprimir()
        print("----------------------------------")
        posicion = input("Ingrese la posicion del cliente que desea modificar: ")
        rol = input("Ingrese el nuevo rol: ")
        nombre = input("Ingrese el nuevo nombre: ")
        apellido = input("Ingrese el nuevo apellido: ")
        telefono = input("Ingrese el nuevo telefono: ")
        correo = input("Ingrese el nuevo correo: ")
        contrasena = input("Ingrese la nueva contraseña: ")
        lista_clientes.editarXML(posicion,rol,nombre,apellido,telefono,correo,contrasena)
        lista_clientes.Imprimir()
        Menu_Administrador()
    
    elif opcion == "5":
        print("añadir cliente")
        rol = input("Ingrese el rol del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        telefono = int(input("Ingrese el telefono del cliente: "))
        correo = input("Ingrese el correro electronico del cliente: ")
        contreasena = input("Ingrese la contraseña del cliente: ")
        lista_clientes.nuevo_registroXML(rol, nombre, apellido, telefono, correo, contreasena)
        print("Cliente agregado correctamente.")
        Menu_Administrador()
    
    elif opcion == "6":
        print("Gestionar peliculas")
    
    elif opcion == "7":
        print("Gestionar salas")
    
    elif opcion == "8":
        print("Eliminar Cliente")
        lista_clientes.Imprimir()
        dato = input("Ingrese el nombre del cliente a eliminar: ")
        lista_clientes.eliminar_nodo(dato)
        print("Cliente eliminado correctamente")
        Menu_Administrador()
    
    elif opcion == "9":
        print("Volver")
        Menu()




def comprar_voletos():
    print("Lista de peliculas: ")
    lista_Genero.imprimir_pelicula()
    decision = input("Escriba el nombre de la pelicula que desea adquirir: ")
    posicion = lista_Genero.buscar_elemento(decision)
    if decision == posicion.titulo:
        print(f"nombre: {posicion.titulo}, director: {posicion.director}, año: {posicion.anio}, fecha: {posicion.fecha}, hora: {posicion.hora}")
    noVoletos= input("Ingrese la cantidad de voletos que desea adquirir: ")
    print("Lista de salas: ")
    lista_salas.imprimir_lista()
    sla= input("Ingrese el numero de sala para la pelicula: ")
    existe_sala = lista_salas.buscar_elemento(sla)
    print(existe_sala)
    if existe_sala.sala == sla:
        asintos= input("Ingrese el numero de asientos para la pelicula: ")
        if asintos <= existe_sala.asientos:
            i=0
            while i <=asintos:
                lugares = []
                for volet in Voletos[4]:
                    for vol in volet:
                        escoger = input("Ingrese asiento: ")
                        if vol == escoger:
                            print("El lugar ya esta ocupado")
                            Menu()
                        else:
                            lugares.append(input("Ingrse el numero de asiento"))
                i=i+1
            print(" El momto total es de:")
            monto =int(asintos) * 42
            print(monto + " Q ")
            print("Ingrese sus datos de facturacion: ")
            nombre = input("Ingrese su nombre: ")
            nit = input("Ingrese su NIT si no cuenta con un nit ingrese C/F: ")
            No_Voleto = No_Voleto+"1"
            datos= [posicion, noVoletos, sla, asintos, lugares, monto, nombre, nit, No_Voleto]
            Voletos.append(datos)
            print("Compra realizada con exito")
        
    else:
        print("La sala ingresada no existe")
    Menu_Cliente()

def historial_voletos():
    if Voletos is None:
        print("no hay voletos comprados")
    else:
        for voleto in Voletos:
            print(voleto)
    Menu_Cliente()

        





Menu()