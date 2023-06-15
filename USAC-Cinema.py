from lista_enlazada import ListaEnlazada
from lista_doblecircular import ListaDoblementeEnlazadaCircular
from lista_doblenlazada import ListaDoblementeEnlazada
from clientes import Clientes
import xml.etree.ElementTree as ET
Voletos=[]
contador = 0
lista_clientes = ListaEnlazada()
lista_Genero = ListaDoblementeEnlazadaCircular()
lista_salas = ListaDoblementeEnlazada()

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
        print("---------------------------")
        print("Iniciar sesion en el sistema")
        print("---------------------------")
        login()
    
    elif opcion == "2":
        print("---------------------------")
        print("Registrar un usuario")
        print("---------------------------")
        agregar_cliente()
    
    elif opcion == "3":
        print("---------------------------")
        print("Ver listado de peliculas")
        print("---------------------------")
        lista_Genero.imprimir_pelicula()
    
    elif opcion == "4":
        print("---------------------------")
        print("Ver listado de usuarios")
        print("---------------------------")
        mostrar_clientes()
    
    elif opcion == "5":
        print("---------------------------")
        print("Salir del sistema")
        print("---------------------------")
        return False
    
    else:
        print("---------------------------")
        print("Opcion invalida")
        print("---------------------------")
        Menu()
        
def login():
    print("-----------------------------------------")
    correo = input("Ingrese su nombre de correo: ")
    password = input("Ingrese su contraseña: ")
    nodo_usuarios=lista_clientes.getNodo(correo)
    
    if correo == "administrador" and password =="201901472":
        Menu_Administrador()
    
    elif nodo_usuarios.rol =="administrador":
        if nodo_usuarios.correo == correo and nodo_usuarios.contrasena == password:
            Menu_Administrador()
    
    elif nodo_usuarios.rol =="cliente":
        if nodo_usuarios.correo == correo and nodo_usuarios.contrasena == password:
            Menu_Cliente()
    Menu()

def agregar_cliente():
    print("---------------------------")
    rol = "cliente"
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    telefono = input("Ingrese el telefono del cliente: ")
    correo = input("Ingrese el correro electronico del cliente: ")
    contreasena = input("Ingrese la contraseña del cliente: ")
    lista_clientes.nuevo_registroXML(rol, nombre, apellido, telefono, correo, contreasena)
    print("Cliente agregado correctamente.")
    Menu()

def mostrar_clientes():
    print("---------------------------")
    lista_clientes.Imprimir()  
    Menu()

def Menu_Cliente():
    print("---------------------------")
    print("1. Ver listado de peliculas")
    print("2. Ver listado de peliculas favoritas")
    print("3. Comprar voletos")
    print("4. Historial de voletos comprados")
    print("5. volver al menu")
    opcion = 0
    opcion = input("Ingrese el numero correspondiente a la opcion: ")
    
    if opcion == "1":
        print("---------------------------")
        print("Listado de peliculas")
        print("---------------------------")
        lista_Genero.imprimir_pelicula()
    
    elif opcion == "2":
        print("---------------------------")
        print("Listado de peliculas favoritas")
        print("---------------------------")
    
    elif opcion == "3":
        print("---------------------------")
        print("Comprar voletos")
        print("---------------------------")
        comprar_voletos()
    
    elif opcion == "4":
        print("---------------------------")
        print("Historial de voletos comprados")
        print("---------------------------")
        historial_voletos()
    
    elif opcion == "5":
        print("---------------------------")
        print("volver")
        print("---------------------------")
        Menu()
    
    else:
        print("---------------------------")
        print("Opcion invalida")
        print("---------------------------")
        Menu()

def Menu_Administrador():
    print("---------------------------")
    print("1. Cargar XML de Clientes")
    print("2. Cargar XML de Peliculas")
    print("3. Cargar XML de Salas")
    print("4. Editar Clientes")
    print("5. añadir Cliente")
    print("6. Eliminar Clientes")
    print("7. Editar Salas")
    print("8. Añadir Salas")
    print("9. Eliminar Salas")
    print("10. Editar Peliculas")
    print("11. Añadir Peliculas")
    print("12. Eliminar Peliculas")
    opcion = 0
    opcion = input("Ingrese el numero correspondiente a la opcion: ")
    
    if opcion == "1":
        print("---------------------------")
        print("Cargando XML de Clientes...")
        print("---------------------------")
        lista_clientes.CargarXML(1)
        lista_clientes.Imprimir()
        Menu_Administrador()
        print("XML de Clientes cargado")
    
    elif opcion == "2":
        print("---------------------------")
        print("Cargar XML de peliculas")
        print("---------------------------")
        lista_Genero.CargarXML_Categorias()
        lista_Genero.imprimir_Categoria()
        Menu_Administrador()
    
    elif opcion == "3":
        print("---------------------------")
        print("Cargar XML de salas")
        print("---------------------------")
        lista_salas.CargarXML_salas(1)
        lista_salas.imprimir_lista()
        Menu_Administrador()
    
    elif opcion == "4":
        print("---------------------------")
        print("Editar clientes")
        print("---------------------------")
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
        print("---------------------------")
        print("añadir cliente")
        print("---------------------------")
        rol = input("Ingrese el rol del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        correo = input("Ingrese el correro electronico del cliente: ")
        contreasena = input("Ingrese la contraseña del cliente: ")
        lista_clientes.nuevo_registroXML(rol, nombre, apellido, telefono, correo, contreasena)
        print("Cliente agregado correctamente.")
        Menu_Administrador()
    
    elif opcion == "6":
        print("---------------------------")
        print("Eliminar Cliente")
        print("---------------------------")
        lista_clientes.Imprimir()
        dato = input("Ingrese el correo del cliente a eliminar: ")
        lugar = int(input("Ingrese la posicion del cliente que desea eliminar: "))
        lista_clientes.eliminar_nodo(dato)
        lista_clientes.eliminar_elemento_xml(lugar)
        print("Cliente eliminado correctamente")
        Menu_Administrador()
        
    elif opcion == "7":
        print("---------------------------")
        print("Editar salas")
        print("---------------------------")
        lista_salas.imprimir_lista()
        posicion = input("Ingrese la posicion de la sala que desea editar: ")
        sala = input("Ingrese el nuevo numero de la sala: ")
        asientos = input("Ingrese el nuevo numero de asientos: ")
        lista_salas.editarXML_Salas(posicion, sala, asientos)
        lista_salas.imprimir_lista()

    elif opcion == "8":
        print("---------------------------")
        print("añadir salas")
        print("---------------------------")
        sala = input("Ingrese el numero de la sala: ")
        asientos = input("Ingrese el numero de asientos: ")
        lista_salas.nuevo_registroXML_Sala(sala, asientos)
        print("Sala agregada correctamente.")
        Menu_Administrador()
        
    elif opcion == "9":
        print("---------------------------")
        print("Eliminar salas")
        print("---------------------------")
        lista_salas.imprimir_lista()
        salita = int(input("Ingrese la posicion de la sala que desea eliminar: "))
        codigo = input("Ingrese el numero de la sala que desea eliminar: ")
        numero=salita-1
        lista_salas.eliminar_elemento_xml_sala(numero)
        lista_salas.eliminar_elemento(codigo)
        print("Sala eliminada correctamente.")
        lista_salas.imprimir_lista()
        Menu_Administrador()

    elif opcion == "10":
        print("---------------------------")
        print("Editar peliculas")
        print("---------------------------")
        lista_Genero.imprimir_pelicula()
        tittle = input("Ingrese el nombre de la pelicula que desea eliminar: ")
        nuevo_titulo= input("Ingrese el nuevo nombre de la pelicula: ")
        nuevo_director= input("Ingrese el nuevo director de la pelicula: ")
        nuevo_anio= input("Ingrese el nuevo año de la pelicula: ")
        nuevo_fecha= input("Ingrese la nueva fecha de la pelicula: ")
        nuevo_hora= input("Ingrese la nueva hora de la pelicula: ")
        lista_Genero.editar_pelicula_por_titulo(tittle, nuevo_titulo,  nuevo_director, nuevo_anio, nuevo_fecha, nuevo_hora)
        print("pelicula Editada con exito")

    elif opcion == "11":
        print("---------------------------")
        print("añadir peliculas")
        print("---------------------------")
        nuevo_genero = input("Ingrese el genero de la nueva pelicula: ")
        nuevo_titulo= input("Ingrese el nuevo nombre de la pelicula: ")
        nuevo_director= input("Ingrese el nuevo director de la pelicula: ")
        nuevo_anio= input("Ingrese el nuevo año de la pelicula: ")
        nuevo_fecha= input("Ingrese la nueva fecha de la pelicula: ")
        nuevo_hora= input("Ingrese la nueva hora de la pelicula: ")
        lista_Genero.añadir_pelicula(nuevo_genero, nuevo_titulo, nuevo_director, nuevo_anio, nuevo_fecha, nuevo_hora)
        print("pelicula añadida con exito")

    elif opcion == "12":
        print("---------------------------")
        print("Eliminar peliculas")
        print("---------------------------")
        lista_Genero.imprimir_pelicula()
        titulo = input("Ingrese el nombre de la pelicula que desea eliminar: ")
        lista_Genero.eliminar_pelicula_por_titulo(titulo)
        lista_Genero.eliminar_elemento(titulo)
        print("Pelicula eliminada con exito")

    elif opcion == "13":
        print("---------------------------")
        print("Salir")
        print("---------------------------")
        Menu()

    else:
        print("---------------------------")
        print("Opcion invalida")
        print("---------------------------")
        Menu_Administrador()

def comprar_voletos():
    print("---------------------------")
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
    if existe_sala.sala == sla:
        print(" El momto total es de:")
        monto = int(noVoletos)*42
        print(str(monto) + " Q ")
        print("Ingrese sus datos de facturacion: ")
        nombre = input("Ingrese su nombre: ")
        nit = input("Ingrese su NIT si no cuenta con un nit ingrese C/F: ")
        codigo_voleto ="USACIPC2_201901472_0"
        datos= [posicion.titulo, noVoletos, sla, monto, nombre, nit, codigo_voleto]
        codigo_voleto = codigo_voleto + str(contador)
        contador = contador + 1
        Voletos.append(datos)
        print("Compra realizada con exito")
    else:
        print("La sala ingresada no existe")
    Menu_Cliente()

def historial_voletos():
    print("---------------------------")
    if Voletos is None:
        print("no hay voletos comprados")
    else:
        for voleto in Voletos:
            print(voleto)
    Menu_Cliente()

        





Menu()