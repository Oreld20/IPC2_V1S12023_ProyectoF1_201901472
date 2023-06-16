from lista_enlazada import ListaEnlazada
from lista_doblecircular import ListaDoblementeEnlazadaCircular
from lista_doblenlazada import ListaDoblementeEnlazada
import xml.etree.ElementTree as ET
from clientes import Clientes
contador=1
Voletos=[]
favoritas=[]
asientos1=[]
lista_clientes = ListaEnlazada()
lista_Genero = ListaDoblementeEnlazadaCircular()
lista_salas = ListaDoblementeEnlazada()
objeto = Clientes("administrador","Oreld", "Ardon", "41445281", "eliotorel10@gmail.com", "201901472")
lista_clientes.add(objeto)

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
        Menu()
    
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
    
    if nodo_usuarios.rol =="administrador":
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

def añadir_favoritos():
    lista_Genero.imprimir_Categoria()
    print("---------------------------")
    print("si desea agreagra una pelicula a favoritos escriba el nombre de la pelicula")
    decision = input("De lo contrario escriba no para volver al menu anterior: ")
    if decision == "no":
        Menu_Cliente()
    else:
     nombre=lista_Genero.buscar_elemento(decision)
     favoritas.append(nombre.dato.titulo)
     añadir_favoritos()

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
        añadir_favoritos()
        
    elif opcion == "2":
        print("---------------------------")
        print("Listado de peliculas favoritas")
        print("---------------------------")
        if favoritas is None:
            print("no hay peliculas favoritas")
        else:
            for elementos in favoritas:
                print(elementos)
        
    elif opcion == "3":
        print("---------------------------")
        print("Comprar voletos")
        print("---------------------------")
        otra_compra_voletos()
    
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
        Menu_Cliente()

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
    print("13. Añadir nueva categoria")
    print("14. Editar categoria")
    print("15. Eliminar categoria")
    print("16. Volver")
    opcion = 0
    opcion = input("Ingrese el numero correspondiente a la opcion: ")
    
    if opcion == "1":
        print("---------------------------")
        print("Cargando XML de Clientes...")
        print("---------------------------")
        lista_clientes.CargarXML(1)
        lista_clientes.Imprimir()
        Menu_Administrador()
    
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
        lista_clientes.eliminar_nodo(dato)
        lista_clientes.eliminar_elemento_xml(dato)
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
        Menu_Administrador()

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
        codigo = input("Ingrese el numero de la sala que desea eliminar: ")
        lista_salas.eliminar_sala_nombre(codigo)
        lista_salas.eliminar_elemento(codigo)
        print("Sala eliminada correctamente.")
        lista_salas.imprimir_lista()
        Menu_Administrador()

    elif opcion == "10":
        print("---------------------------")
        print("Editar peliculas")
        print("---------------------------")
        lista_Genero.imprimir_pelicula()
        tittle = input("Ingrese el nombre de la pelicula que desea editar: ")
        nuevo_titulo= input("Ingrese el nuevo nombre de la pelicula: ")
        nuevo_director= input("Ingrese el nuevo director de la pelicula: ")
        nuevo_anio= input("Ingrese el nuevo año de la pelicula: ")
        nuevo_fecha= input("Ingrese la nueva fecha de la pelicula: ")
        nuevo_hora= input("Ingrese la nueva hora de la pelicula: ")
        lista_Genero.editar_pelicula_por_titulo(tittle, nuevo_titulo,  nuevo_director, nuevo_anio, nuevo_fecha, nuevo_hora)
        print("pelicula Editada con exito")
        Menu_Administrador()

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
        Menu_Administrador()

    elif opcion == "12":
        print("---------------------------")
        print("Eliminar peliculas")
        print("---------------------------")
        lista_Genero.imprimir_pelicula()
        titulo = input("Ingrese el nombre de la pelicula que desea eliminar: ")
        lista_Genero.eliminar_pelicula_por_titulo(titulo)
        lista_Genero.CargarXML_Categorias()
        print("Pelicula eliminada con exito")
        Menu_Administrador()

    elif opcion == "13":
        print("---------------------------")
        print("Añadir nueva categoria")
        print("---------------------------")
        categoria = input("Ingrese la nueva categoria: ")
        lista_Genero.agregar_categoria_xml(categoria)
        print("categoria añadida con exito")
        Menu_Administrador()

    elif opcion == "14":
        print("---------------------------")
        print("Editar una categoria")
        print("---------------------------")
        name = input("Ingrese el nombre de la categoria a editar: ")
        nuevo= input("Ingrese el nuevo nombre de la categoria: ")
        lista_Genero.editar_categoria_xml(name, nuevo)
        lista_Genero.CargarXML_Categorias()
        print("Categoria editada con exito")
        Menu_Administrador()
        
    elif opcion == "15":
        print("---------------------------")
        print("Eliminar una categoria")
        print("---------------------------")
        nombre_cate = input("Ingrese el nombre de la categoria a eliminar: ")
        lista_Genero.eliminar_categoria_xml(nombre_cate)
        lista_Genero.CargarXML_Categorias()
        print("Categoria eliminada con exito")
        Menu_Administrador()

    elif opcion == "16":
        print("---------------------------")
        print("Volver")
        print("---------------------------")
        Menu()
        
    else:
        print("---------------------------")
        print("Opcion invalida")
        print("---------------------------")
        Menu_Administrador()

def historial_voletos():
    print("---------------------------")
    if Voletos is None:
        print("no hay voletos comprados")
    else:
        for voleto in Voletos:
            print(voleto)
    Menu_Cliente()

def otra_compra_voletos():
    print("---------------------------")
    print("Lista de peliculas: ")
    print("---------------------------")
    lista_Genero.imprimir_Categoria()
    asientos2=[]
    global contador
    decision = input("Escriba el nombre de la pelicula que desea adquirir: ")
    pelicula = lista_Genero.buscar_elemento(decision)
    numero_Voletos= input("Ingrese la cantidad de voletos que desea adquirir: ")
    print("Lista de salas disponibles: ")
    lista_salas.imprimir_lista()
    sala = input("Ingrese el numero de sala en la que desea ver la pelicula: ")
    existe_sala = lista_salas.buscar_elemento(sala)
    if existe_sala.sala == sala:
         for _ in range(int(numero_Voletos)):
            asiento = input("Ingrese el número de asiento: ")
            if int(asiento) <= int(existe_sala.asientos):
                for butacas in asientos1:
                    if asiento == butacas:
                        print(f"El asiento {asiento} esta ocupado")
                        otra_compra_voletos()
                    else:
                        asientos1.append(asiento)
                        asientos2.append(asiento)
            else:
                print("El asiento seleccionado esta fuera de rango")
                otra_compra_voletos()                
    else:
        print("La sala ingresada no existe")
        otra_compra_voletos()
    monto = int(numero_Voletos)*42
    print("Ingrese sus datos de facturacion: ")
    nombre = input("Ingrese su nombre: ")
    nit = input("Ingrese su NIT si no cuenta con un nit ingrese C/F: ")
    direccion= input("Ingrese su direccion: ")
    numero_boleto = f"#USACIPC2_201901472_{contador}"
    datos= [pelicula.dato.titulo, numero_Voletos, existe_sala.sala, print(asientos2),  monto, nombre, nit, direccion,  numero_boleto]
    Voletos.append(datos)
    contador += 1
    print("Compra realizada con exito")
    Menu_Cliente()

Menu()