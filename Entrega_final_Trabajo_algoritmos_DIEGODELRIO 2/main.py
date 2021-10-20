try:
    from Usuario import Usuario
    from Cripto import Criptomoneda
    from Cuenta import Cuenta
    from Generos import EnumSexo
    import datetime 
    from CSV import leerCriptomoneda, leerCuenta, leerUsuario, leerTransaccion
    import Administrador
    import Cliente
    import Utilidades
    from Transferencias import Transferencia

except ImportError as IE:
    print(IE, "No se ha podido importar el modulo.")
    raise IE

#FUNCIONES QUE USO EN EL MAIN
def GuardarUsuarios(lista):
    f1 = open("InfoUsuarios.csv", "w")
    for usuario in lista:
        usuario.guardar_usuario(f1)

def GuardarCuentas(lista1):
    f2 = open("InfoCuentas.csv", "w")
    for cuenta in lista1:
        cuenta.guardar_cuenta(f2)

def GuardarCriptos(lista2):
    f3 = open("InfoCriptomonedas.csv", "w")
    for cripto in lista2:
        cripto.guardar_cripto(f3)

def GuardarTransaccion(lista3):
    f4 = open("InfoTransfers.csv", "w")
    for trans in lista3:
        if isinstance(trans, Transferencia):
            trans.guardar_transferencia(f4)
        else:
            raise Utilidades.TransferenciaTypeError("Tiene que ser una transferencia")
            
def get_referecias_usuarios(lista):
    '''
    Funcion que devuelve la referencia de cada uno de los usuarios.
    '''
    lista_referencias = []
    for usuario in lista:
        lista_referencias.append(usuario.get_id())
    if len(lista_referencias) >= 0:
        return lista_referencias
    else:
        return ('No hay codigos de referencia que listar.')

                            
def get_usuarios_descendente(lista):
    '''
    Funcion que devuelve la referencia de cada uno de los usuarios.
    '''
    lista_users = []
    for usuario in lista:
        lista_users.append(usuario.get_id())
    if len(lista_users) >= 0:
        lista_users.sort(reverse = True)
        return lista_users
    else:
        return ('No hay codigos de referencia que listar.')

def get_usuario_memoria_from_list(lista,referencia):
    '''
    Metodo para obtener un usuario de una lista indicando su id.
    '''
    for usuario in lista:
        if referencia == usuario.get_id():
            contraseña = str(input("Introduzca la contraseña: "))
            if usuario.get_contraseña() == contraseña:
                print("\nHa seleccionado a " + str(usuario.get_nombre()))
                return usuario
            else:
                print("La contraseña introducida no es correcta.")

def get_usuario_from_list(lista,referencia):
    '''
    Metodo para obtener un usuario de una lista indicando su id.
    '''
    for usuario in lista:
        if usuario.get_id() == referencia:
            print("\nHa seleccionado a " + str(usuario.get_nombre()))
            return usuario


def get_nombres_cripto(lista):
    '''
    Funcion para obtener los nombres de las monedas.
    '''
    nombres = []
    for cripto in lista:
        nombres.append(cripto.get_nombre())
    if len(nombres) >= 0:
        return nombres
    else:
        return("No hay ninguna cripto.")

def get_fee_cripto(lista, moneda):
    '''
    Funcion para obtener los id's de las monedas.
    '''
    for cripto in lista:
        if moneda == cripto.get_nombre():
            return cripto.get_precioTransaccion()
            
def dolares_a_cripto(moneda, cantidad, lista):
    '''
    Funcion para transformar la cantidad en $ a cantidad de criptos.

    :param moneda: str que se corresponde con el nombre de la cripto.

    :param cantidad: cantidad de criptos

    :param lista: lista de criptomonedas actualizada en caso de haber añadido una cripto nueva.

    return: la cantidad de criptos real tras hacer la conversion.
    '''
    if (not isinstance(cantidad,float) or not isinstance(cantidad,int)) and not isinstance(moneda,str):
        raise ValueError ('La cantidad tiene que ser un entero o decimal.')
    if isinstance(moneda, str):
        for cripto in lista:
                if moneda == cripto.get_nombre():
                    cantidad_real = cantidad/cripto.get_valorUSD()
                    return cantidad_real
    
    else:
        raise ValueError ('Los nombres de las monedas son BITCOIN, ETHER y XRP; revisa que lo introdujiste bien.')
    
def cripto_a_dolar(moneda, cantidad, lista):
    '''
    Funcion para transformar la cantidad de criptos en $.

    :param moneda: str que se corresponde con el nombre de la cripto.

    :param cantidad: cantidad de criptos

    :param lista: lista de criptomonedas actualizada en caso de haber añadido una cripto nueva.

    return: la cantidad de dolares real tras hacer la conversion.
    '''
    if (not isinstance(cantidad,float) or not isinstance(cantidad,int)) and not isinstance(moneda,str):
        raise ValueError ('La cantidad tiene que ser un entero o decimal.')
    if isinstance(moneda, str):
        for cripto in lista:
                if moneda == cripto.get_nombre():
                    cantidad_real = cantidad * cripto.get_valorUSD()
                    return cantidad_real

    else:
        raise ValueError ('Los nombres de las monedas son BITCOIN, ETHER y XRP; revisa que lo introdujiste bien.')

#MAIN

def main():
    Usuario_memoria = None
    #FUSIONO TODOS LOS CSV PARA QUE EN EL USUARIO APAREZCAN LAS CUENTAS.
    lista_criptos = leerCriptomoneda('InfoCriptomonedas.csv')
    cuentass = leerCuenta("InfoCuentas.csv")
    usuarioss = leerUsuario("InfoUsuarios.csv")
    transfers = leerTransaccion("InfoTransfers.csv")
    #Proceso para crear los usuarios añadiendoles a cada usuario su cuenta correspondiente.
    Usuarios_lista = []
    Cuentas_lista = []
    Cripto_lista = []
    Transferencia_lista = []
    Cuentas_Usuario_1 = []
    Cuentas_Usuario_2 = []
    Cuentas_Usuario_3 = []
    Cuentas_Usuario_4 = []
    Cuentas_Usuario_5 = []
    Cuentas_Usuario_6 = []
    
    for cuenta in cuentass:
        for trans in transfers:
            if cuenta.get_usuario() == trans.get_origen():
                if cuenta.get_moneda() == trans.get_cripto():
                    cuenta.get_transacciones().append(trans)
                    Transferencia_lista.append(trans)

    #print(Transferencia_lista)
            
    for cripto in lista_criptos:
        Cripto_lista.append(cripto)

    for cuenta in cuentass:
        if cuenta.get_usuario() == 1:
            Cuentas_Usuario_1.append(cuenta)
        elif cuenta.get_usuario() == 2:
            Cuentas_Usuario_2.append(cuenta)
        elif cuenta.get_usuario() == 3:
            Cuentas_Usuario_3.append(cuenta)
        elif cuenta.get_usuario() == 4:
            Cuentas_Usuario_4.append(cuenta)
        elif cuenta.get_usuario() == 5:
            Cuentas_Usuario_5.append(cuenta)
        elif cuenta.get_usuario() == 6:
            Cuentas_Usuario_6.append(cuenta)
        Cuentas_lista.append(cuenta)

    for usuario in usuarioss:
        if usuario.get_id() == 1:
            usuario.set_lista_cuenta(Cuentas_Usuario_1)
        elif usuario.get_id() == 2:
            usuario.set_lista_cuenta(Cuentas_Usuario_2)
        elif usuario.get_id() == 3:
            usuario.set_lista_cuenta(Cuentas_Usuario_3)
        elif usuario.get_id() == 4:
            usuario.set_lista_cuenta(Cuentas_Usuario_4)
        elif usuario.get_id() == 5:
            usuario.set_lista_cuenta(Cuentas_Usuario_5)
        elif usuario.get_id() == 6:
            usuario.set_lista_cuenta(Cuentas_Usuario_6)
        Usuarios_lista.append(usuario)
    
    print(get_usuarios_descendente(Usuarios_lista))
    
    
    print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")
    opcion = int(input("Introduzca una opcion: "))
    while opcion != 13:

        if opcion == 1:
            print("------------------EJERCICIO 1-------------------")
            print("\nListar la informacion de todos los tipos de criptomoneda.")#Hacer CSV 
            
            try:
                for cripto in Cripto_lista:
                    print("\n", cripto)

            except Exception as e:
                print("Error en el ejercicio 1.")
                print(e)

            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")
            opcion = int(input("Introduzca una opcion: "))
        
        elif opcion == 2:
            print("------------------EJERCICIO 2-------------------")
            print("\nInsertar una nueva criptomoneda")
            try:
                if Usuario_memoria == None:
                    print("Debe cargar antes un usuario en memoria.")
                elif str(type(Usuario_memoria).__name__) == "Administrador":
                    NombreCripto = str(input("Introduzca el nombre de la cripto que desea añadir: "))
                    NuevoValor = float(input("Introduzca el valor en USD de la cripto: "))
                    NuevoPrecio = float(input("Introduzca el precio de las transacciones: "))
                    Contratos = bool(input("Introduzca si se crean contratos o no (True/False): "))
                    Nuevas_maxUnis = int(input("Introduzca el volumen de oferta de la criptomoneda: "))

                    Usuario_memoria.crear_cripto(NombreCripto, NuevoValor, NuevoPrecio, Contratos, Nuevas_maxUnis, Cripto_lista, NuevoID = 1)

                else:
                    print("Usted no es un Administrador.")
            except Exception as e:
                print("Error en el ejercicio 2")
                print(e)
            

            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))

        elif opcion == 3:
            print("------------------EJERCICIO 3-------------------")#Hacer CSV
            print("\nListar todos los usuarios y sus ID's.")
            try:
                print("ID " + "Nombre y apellido ")
                for usuario in Usuarios_lista:
                    nombre = usuario.get_nombre()
                    apellido = usuario.get_apellido()
                    ids = usuario.get_id()
                    print(str(ids) + " " +  str(nombre) + " " + str(apellido))
            except Exception as e:
                print("Error en el ejercicio 3.")
                print(e)

            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))

        elif opcion == 4:
            print("------------------EJERCICIO 4-------------------")#Hacer CSV
            print("\nCargar usuario en memoria.")

            try:
                print("LISTADO DE ID'S DE LOS USUARIOS EXISTENTES: ")
                print(get_referecias_usuarios(Usuarios_lista))

                eleccion = int(input("\nIntroduzca el ID del usuario que desea cargar: "))
                usuario_seleccionado = eleccion
    
                Usuario_memoria = get_usuario_memoria_from_list(Usuarios_lista, usuario_seleccionado)
                
            except Exception as e:
                print("Error en el ejercicio 4.")
                print(e)

            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))

        elif opcion == 5:
            print("------------------EJERCICIO 5-------------------")
            print("\nCrear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor.")
            try:
                if Usuario_memoria != None:
                    if str(type(Usuario_memoria).__name__) == "Administrador":
                        
                        nuevo_id = int(input("Introduzca el ID: "))
                        nuevo_nombre = str(input("Introduzca el nombre: "))
                        nuevo_apellido = str(input("Introduzca el apellido: "))
                        nuevo_nif = str(input("Introduzca los 8 digitos y la letra de su DNI: "))
                        nueva_nacionalidad = str(input("Introduzca su nacionalidad: "))
                        nuevo_cumple = datetime.datetime.strptime(input("Introduzca la fecha de su nacimiento en formato yyyy/mm/dd: "), '%Y/%m/%d').date()
                        nuevo_registro = datetime.datetime.strptime(input("Introduzca la fecha del dia de hoy en formato yyyy/mm/dd: "), '%Y/%m/%d').date()
                        nuevo_sexo = EnumSexo.str_a_genero(input("Introduzca el sexo(Hombre o Mujer): "))
                        nueva_contraseña = str(input("Introduzca la contraseña que desee: "))
                        pregunta = str(input("El nuevo usuario desea que sea un Cliente o un Administrador: "))
                    
                        if pregunta.upper() == "ADMINISTRADOR":
                            nuevo_usuario = Administrador.Administrador(nuevo_id, nuevo_nombre, nuevo_apellido, nuevo_nif, nueva_nacionalidad, nuevo_sexo, nuevo_cumple, nuevo_registro, nueva_contraseña)
                            nuevo_usuario_id = nuevo_usuario.get_id()
                        elif pregunta.upper() == "CLIENTE":
                            nuevo_usuario = Cliente.Cliente(nuevo_id, nuevo_nombre, nuevo_apellido, nuevo_nif, nueva_nacionalidad, nuevo_sexo, nuevo_cumple, nuevo_registro, nueva_contraseña)
                            nuevo_usuario_id = nuevo_usuario.get_id()
                
                        cripto_a_ingresar = str(input("Introduzca el nombre de la criptomoneda que desee ingresar (BITCOIN/ETHER/XRP): "))
                        cripto_elegida = cripto_a_ingresar.upper()
                        cantidad = float(input("Introduzca la cantidad de dinero que quiere ingresar de " + str(cripto_a_ingresar) + ": "))
                            
                        nueva_cuenta = nuevo_usuario.crear_cuenta(cripto_elegida, nuevo_usuario_id, NuevaCantidad= dolares_a_cripto(cripto_elegida, cantidad, Cripto_lista))
                        print("Usuario creado correctamente.")
                
                        Usuarios_lista.append(nuevo_usuario)
                        Cuentas_lista.append(nueva_cuenta)
                
                    elif str(type(Usuario_memoria).__name__) == "Cliente":
                    
                        nuevo_id = int(input("Introduzca el ID: "))
                        nuevo_nombre = str(input("Introduzca el nombre: "))
                        nuevo_apellido = str(input("Introduzca el apellido: "))
                        nuevo_nif = str(input("Introduzca los 8 digitos y la letra de su DNI: "))
                        nueva_nacionalidad = str(input("Introduzca su nacionalidad: "))
                        nuevo_cumple = datetime.datetime.strptime(input("Introduzca la fecha de su nacimiento en formato yyyy/mm/dd: "), '%Y/%m/%d').date()
                        nuevo_registro = datetime.datetime.strptime(input("Introduzca la fecha del dia de hoy en formato yyyy/mm/dd: "), '%Y/%m/%d').date()
                        nuevo_sexo = EnumSexo.str_a_genero(input("Introduzca el sexo(Hombre o Mujer): "))
                        nueva_contraseña = str(input("Introduzca la contraseña que desee: "))
                    
                        nuevo_usuario = Cliente.Cliente(nuevo_id, nuevo_nombre, nuevo_apellido, nuevo_nif, nueva_nacionalidad, nuevo_sexo, nuevo_cumple, nuevo_registro, nueva_contraseña)
                        nuevo_usuario_id = nuevo_usuario.get_id()
                
                        cripto_a_ingresar = str(input("Introduzca el nombre de la criptomoneda que desee ingresar (BITCOIN/ETHER/XRP): "))
                        cripto_elegida = cripto_a_ingresar.upper()
                        cantidad = float(input("Introduzca la cantidad de dinero que quiere ingresar de " + str(cripto_a_ingresar) + ": "))
                            
                        nueva_cuenta = nuevo_usuario.crear_cuenta(cripto_elegida, nuevo_usuario_id, NuevaCantidad= dolares_a_cripto(cripto_elegida, cantidad, Cripto_lista))
                        print("Usuario creado correctamente.")
                
                        Usuarios_lista.append(nuevo_usuario)
                        Cuentas_lista.append(nueva_cuenta)

                else:
                    print("Debe cargar un usuario en memoria.")
            
            except Exception as e:
                print("Error en el ejercicio 5.")
                print(e)

            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))
        
        elif opcion == 6:
            print("------------------EJERCICIO 6-------------------")
            print("\nAñadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP")
            try:
                if Usuario_memoria != None:
                    if str(type(Usuario_memoria).__name__) == "Administrador":
                        nuevo_nombre = str(input("Introduzca el nombre: "))
                        nuevo_apellido = str(input("Introduzca el apellido: "))
                        nuevo_cumple = datetime.datetime.strptime(input("Introduzca la fecha de nacimiento formato yyyy/mm/dd: "), '%Y/%m/%d').date()
                        pregunta = str(input("El nuevo usuario desea que sea un Cliente o un Administrador: "))
                    
                        if pregunta.upper() == "ADMINISTRADOR":
                            nuevo_usuario = Administrador.Administrador(1, nuevo_nombre, nuevo_apellido, NIF= None, nacionalidad = None, sexo = None, fecha_nacimiento = nuevo_cumple, fecha_registro = None, contraseña = None)
                            id_usuario = nuevo_usuario.get_id()
                        elif pregunta.upper() == "CLIENTE":
                            nuevo_usuario = Cliente.Cliente(1, nuevo_nombre, nuevo_apellido, NIF= None, nacionalidad = None, sexo = None, fecha_nacimiento = nuevo_cumple, fecha_registro = None, contraseña = None)
                            id_usuario = nuevo_usuario.get_id()

            
                        Cripto_a_regalar = Criptomoneda(3, "XRP", 0.537562, 0.00001, True, 100000000000)
                        nombre_cripto = Cripto_a_regalar.get_nombre()
                
                        valor = dolares_a_cripto(nombre_cripto, 10, Cripto_lista)
                        nueva_cuenta = nuevo_usuario.crear_cuenta(nombre_cripto, id_usuario ,NuevaCantidad = valor)
                        print("Usuario creado correctamente.")
                            
                        Usuarios_lista.append(nuevo_usuario)
                        Cuentas_lista.append(nueva_cuenta)
                
                    elif str(type(Usuario_memoria).__name__) == "Cliente":
                        nuevo_nombre = str(input("Introduzca el nombre: "))
                        nuevo_apellido = str(input("Introduzca el apellido: "))
                        nuevo_cumple = datetime.datetime.strptime(input("Introduzca la fecha de nacimiento formato yyyy/mm/dd: "), '%Y/%m/%d').date()
                        nuevo_usuario = Cliente.Cliente(1, nuevo_nombre, nuevo_apellido, NIF= None, nacionalidad = None, sexo = None, fecha_nacimiento = nuevo_cumple, fecha_registro = None, contraseña = None)
                        id_usuario = nuevo_usuario.get_id()

            
                        Cripto_a_regalar = Criptomoneda(3, "XRP", 0.537562, 0.00001, True, 100000000000)
                        nombre_cripto = Cripto_a_regalar.get_nombre()
                
                        valor = dolares_a_cripto(nombre_cripto, 10, Cripto_lista)
                        nueva_cuenta = nuevo_usuario.crear_cuenta(nombre_cripto, id_usuario ,NuevaCantidad = valor)
                        print("Usuario creado correctamente.")
                            
                        Usuarios_lista.append(nuevo_usuario)
                        Cuentas_lista.append(nueva_cuenta)
                
                else:
                    print("Debe cargar un usuario en memoria.")

            except Exception as e:
                print("Error en el ejercicio 6.")
                print(e)
                
            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))
        
        elif opcion == 7:
            print("------------------EJERCICIO 7-------------------")
            print("\nRealizar un ingreso de una criptomoneda existente.")
            try:
                if Usuario_memoria != None:
                    print("\nEl usuario en memoria es: ")
                    print(Usuario_memoria.get_nombre())
                    pregunta = str(input("Mostrar las monedas por el orden de ID o por orden alfabetico segun el nombre de la cripto(ID/ALFABETICO): "))
                    print("CUENTAS QUE TIENE EL USUARIO " + str(Usuario_memoria.get_id()) + ": ")
                    if pregunta.upper() == "ID":
                        print(Usuario_memoria.get_moneda_from_cuenta())
                    elif pregunta.upper() == "ALFABETICO":  
                        print(Usuario_memoria.get_moneda_sorted())
                        
                    print("\nNOMBRES DE LAS CRIPTOMONEDAS EXISTENTES: ")
                    print("Nombre: " + str((get_nombres_cripto(Cripto_lista))))

                    cripto_elegida = str(input("\nIntroduzca el nombre de la criptomoneda que desee: "))
                    eleccion_cripto = cripto_elegida.upper()

                    pregunta = input("Tiene ya una cuenta con la criptomoneda seleccionada (si/no): ")
                    if pregunta == "si" or pregunta == "Si" or pregunta == "SI":
                        amount = float(input("Introduzca la cantidad que desea ingresar en USD de la cripto " + str(eleccion_cripto) + ": "))
                        Usuario_memoria.depostiar_dinero(eleccion_cripto, dolares_a_cripto(eleccion_cripto, amount, Cripto_lista))
                        #print(Usuario_memoria)
                        print("Ingreso realizado con exito.")
                    
                    elif pregunta == "no" or pregunta == "No" or pregunta == "NO":
                        print("Ya que no posee una cuenta con dicha criptomoneda, se la vamos a crear.")
                        amount1 = float(input("Introduzca la cantidad que desea ingresar en USD de la cripto " + str(eleccion_cripto) + " en su nueva cuenta: "))
                        Usuario_memoria.crear_cuenta(eleccion_cripto, Usuario_memoria.get_id(), NuevaCantidad= dolares_a_cripto(eleccion_cripto, amount1, Cripto_lista))
                        print("La cuenta ha sido creada.")
                        #print(Usuario_memoria)
                        print("Ingreso realizado con exito.")
                
                else:
                    print("Debe cargar un usuario en memoria.")
                          
            except Exception as e:
                print("Error en el ejercicio 7.")
                print(e)
            
            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))
    
        elif opcion == 8:
            print("------------------EJERCICIO 8-------------------")
            print("\nRealizar una retirada de una cantidad de dinero de una criptomoneda.")
            try:
                if Usuario_memoria != None:
                    pregunta = str(input("Mostrar las monedas por el orden de ID o por orden alfabetico segun el nombre de la cripto(ID/ALFABETICO): "))
                    print("CUENTAS QUE TIENE EL USUARIO " + str(Usuario_memoria.get_id()) + ": ")
                    if pregunta.upper() == "ID":
                        print(Usuario_memoria.get_moneda_from_cuenta())
                    elif pregunta.upper() == "ALFABETICO":  
                        print(Usuario_memoria.get_moneda_sorted())
                    
                    cripto_elegida = str(input("\nIntroduzca el nombre de la criptomoneda que desee retirar (BITCOIN/ETHER/XRP): "))
                    eleccion_cripto = cripto_elegida.upper()

                    for cuenta in Usuario_memoria.get_lista_cuentas():
                        if eleccion_cripto == cuenta.get_moneda():
                            print("La cantidad que posee de la cripto seleccionada es de " + str(cuenta.get_cantidad()))
                            amount = float(input("Introduzca la cantidad que desea retirar de la cripto " + str(eleccion_cripto) + ": "))
                            Usuario_memoria.retirar_dinero(eleccion_cripto, amount)
                            valor = cripto_a_dolar(eleccion_cripto,amount, Cripto_lista)
                            print("La conversion es, para una cantidad de " + str(amount) + " " + eleccion_cripto + " obtiene " + str(valor)+"$.")
                
                else: 
                    print("Debe cargar un usuario en memoria.")
            
            except Exception as e:
                print("Error en el ejercicio 8.") 
                print(e)
                      

            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))
    
        elif opcion == 9:
            print("------------------EJERCICIO 9-------------------")
            print("\nModificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro.")
            try:
                if Usuario_memoria != None:
                    if str(type(Usuario_memoria).__name__) == "Administrador":
                        if isinstance(Usuario_memoria, Administrador.Administrador): 
                            for usuario in Usuarios_lista:
                                ids = usuario.get_id()
                                nombre = usuario.get_nombre()
                                apellido = usuario.get_apellido()
                                print("ID: " + str(ids) + " " +"Nombre: " + str(nombre) + " " + str(apellido))
                        
                            usuario_origen = int(input("Introduzca el ID del usuario que desea modificar: "))
                            origen = get_usuario_from_list(Usuarios_lista, usuario_origen)
                            #print(origen)
            
                            nuevo_nombre = str(input("Introduzca el nuevo nombre: "))
                            nuevo_apellido = str(input("Introduzca el nuevo apellido: "))
                            nuevo_cumple = datetime.datetime.strptime(input("Introduzca la nueva fecha de nacimiento en formato yyyy/mm/dd: "), '%Y/%m/%d').date()
                            nuevo_sexo = EnumSexo.str_a_genero(input("Introduzca el nuevo sexo(Hombre o Mujer): "))
                            nueva_nacionalidad = str(input("Introduce la nueva nacionalidad: "))
                            Usuario_memoria.modificar_usuario(nuevo_nombre, nuevo_apellido, nuevo_cumple, nuevo_sexo, nueva_nacionalidad, origen)
                            print("Usuario modificado con exito.")
                    
                        else:
                            raise Utilidades.UsuarioTypeError("El Usuario en memoria a de ser un administrador.")
                
                    elif str(type(Usuario_memoria).__name__) == "Cliente":
                        print("Usuario seleccionado: ")
                        print(Usuario_memoria)
                        print("\n")
                        nuevo_nombre = str(input("Introduzca el nuevo nombre: "))
                        nuevo_apellido = str(input("Introduzca el nuevo apellido: "))
                        nuevo_cumple = datetime.datetime.strptime(input("Introduzca la nueva fecha de nacimiento en formato yyyy/mm/dd: "), '%Y/%m/%d').date()
                        nuevo_sexo = EnumSexo.str_a_genero(input("Introduzca el nuevo sexo(Hombre o Mujer): "))
                        nueva_nacionalidad = str(input("Introduce la nueva nacionalidad: "))
                        Usuario_memoria.modificar_usuario(nuevo_nombre, nuevo_apellido, nuevo_cumple, nuevo_sexo, nueva_nacionalidad)
                        print("Usuario modificado: ")
                
                else:
                    print("Debe cargar un usuario en memoria.")

            except Exception as e:
                print("Error en el ejercicio 9.")
                print(e)
            
            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))

        elif opcion == 10:
            print("------------------EJERCICIO 10-------------------")
            print("\nRealizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio.")
            try:
                if Usuario_memoria != None:
                    if str(type(Usuario_memoria).__name__) == "Administrador": 
                        if isinstance(Usuario_memoria, Administrador.Administrador):
                            for usuario in Usuarios_lista:
                                ids = usuario.get_id()
                                nombre = usuario.get_nombre()
                                apellido = usuario.get_apellido()
                                print("ID: " + str(ids) + " " +"Nombre: " + str(nombre) + " " + str(apellido))
                    
                            usuario_origen = int(input("Introduzca el ID del usuario que realiza la transferencia: "))
                            origen = get_usuario_from_list(Usuarios_lista, usuario_origen)
                            print(origen.get_lista_cuentas())

                            usuario_destino = int(input("Introduzca el ID del usuario al que le quiera transferir el dinero: "))
                            destino = get_usuario_from_list(Usuarios_lista, usuario_destino)
                            print(destino.get_lista_cuentas())

                            print("CUENTAS QUE TIENE EL USUARIO " + str(Usuario_memoria.get_id()) + ": ")
                            for cuenta in Usuario_memoria.get_lista_cuentas():
                                print("Tiene " + str(cuenta.get_cantidad()) + " "+cuenta.get_moneda())


                            Moneda = str(input("Introduzca el nombre de la mondea que desea transferir: "))
                            cantidad = int(input("Introduzca la cantidad que desea transferir: "))

                            Usuario_memoria.transferencia(destino, cantidad, Moneda, origen)
                            print("Transferencia realizada con exito.")
                
                    elif str(type(Usuario_memoria).__name__) == "Cliente": 
                        
                        for usuario in Usuarios_lista:
                            ids = usuario.get_id()
                            nombre = usuario.get_nombre()
                            apellido = usuario.get_apellido()
                            print("ID: " + str(ids) + " " +"Nombre: " + str(nombre) + " " + str(apellido))

                        print("CUENTAS QUE TIENE EL USUARIO " + str(Usuario_memoria.get_id()) + ": ")
                        for cuenta in Usuario_memoria.get_lista_cuentas():
                            print("Tiene " + str(cuenta.get_cantidad()) + " "+cuenta.get_moneda())
                        
                        Moneda = str(input("\nIntroduzca el nombre de la mondea que desea transferir: "))
                        usuario_destino = int(input("Introduzca el ID del usuario al que le quiera transferir el dinero: "))
                        destino = get_usuario_from_list(Usuarios_lista, usuario_destino)
                        print(destino.get_lista_cuentas())
        
                        cantidad = float(input("Introduzca la cantidad de criptos que desea transferir: "))

                        Usuario_memoria.transferencia(destino, cantidad, Moneda)
                        print("Transferencia realizada con exito.")

                else:
                    print("Debe cargar un usuario en memoria.")

            except Exception as e:
                print("Error en el ejercicio 10.")
                print(e)  
            
            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))

        elif opcion == 11:
            print("------------------EJERCICIO 11-------------------")
            print("\nVer información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10.")
            try:
                if Usuario_memoria != None:
                    print(Usuario_memoria)
                    print("\nCuentas del usuario: ")
                    print(Usuario_memoria.ids_cuentas())
                    referencias = int(input("Introduzca la referencia de la cuenta que desea visualizar: "))
                    print(Usuario_memoria.get_informacion(referencias))
                    
                    valor_cripto = cripto_a_dolar(Usuario_memoria.get_informacion(referencias).get_moneda(), Usuario_memoria.get_informacion(referencias).get_cantidad(), Cripto_lista)
                    print("\nLa cantidad de " + str(Usuario_memoria.get_informacion(referencias).get_moneda()) + " que posee es de " + str(Usuario_memoria.get_informacion(referencias).get_cantidad()) + ", esto se traduce en " + str(valor_cripto) + " $")
                    
                    print("\nTransferencias realizadas con esta cuenta:")
                    print(Usuario_memoria.get_informacion(referencias).ids_transferencias())
                    trans = int(input("Introduzca el ID de la transferencia que desea visualizar: "))
                    transferencia = Usuario_memoria.get_informacion(referencias).get_informacion_transferencias(trans)
                    print(transferencia)
                    if transferencia not in Transferencia_lista:
                        Transferencia_lista.append(transferencia)
                    print("\nEl precio de la transaccion fue de: " + str(get_fee_cripto(Cripto_lista, Usuario_memoria.get_informacion(referencias).get_moneda())))
                    valor_cripto1 = cripto_a_dolar(Usuario_memoria.get_informacion(referencias).get_moneda(), transferencia.get_cantidad(), Cripto_lista)
                    print("La cantidad de " + str(Usuario_memoria.get_informacion(referencias).get_moneda()) + " que fue transferida " + str(transferencia.get_cantidad()) + ", esto se traduce en " + str(valor_cripto1) + " $")
                
                else:
                    print("Debe cargar un usuario en memoria.")


            except Exception as e:
                print("Error en el ejercicio 11.")
                print(e)               
            
            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))
    
        elif opcion == 12:
            print("------------------EJERCICIO 12-------------------")
            print("\nGuardar la información actual.")
            try:
                GuardarUsuarios(Usuarios_lista)
                print("\nInformacion Usuario guardada con exito.")
            except Exception as e:
                print("Error al guardar Usuarios")
                print(e)
            
            try:
                GuardarCuentas(Cuentas_lista)
                print("\nInformacion Cuentes guardada con exito.")
            except Exception as e:
                print("Error al guardar Cuentas")
                print(e)
            try:
                GuardarCriptos(Cripto_lista)
                print("\nInformacion Criptos guardada con exito.")
            except Exception as e:
                print("Error al guardar Criptos")
                print(e)
            try:
                GuardarTransaccion(Transferencia_lista)
                print("\nInformacion Transferencias guardada con exito.")
            except Exception as e:
                print("Error al guardar Transferencias")
                print(e)

            print("\n")
            print("Opciones: \n1.Listar la informacion de todos los tipos de criptomoneda. \n2.Insertar una nueva criptomoneda. \n3.Listar todos los usuarios y sus ID's. \n4.Cargar usuario en memoria. \n5.Crear un usuario nuevo indicando sus datos, el primer ingreso de una criptomoneda y su valor. \n6.Añadir un nuevo usuario indicando su nombre, apellidos y fecha de nacimiento,regalando al usuario una cantidad de 10 dólares americanos en XRP  \n7.Realizar un ingreso de una criptomoneda existente. \n8.Realizar una retirada de una cantidad de dinero de una criptomoneda. \n9.Modificar la información del usuario (todos los campos a excepción del documento de identidad, el ID de usuario y la fecha de registro. \n10.Realizar una transacción de un usuario origen a un usuario destino. Se deben listar los usuarios al inicio. \n11.Ver información detallada de un usuario, con el número de unidades de cada criptomoneda y el valor en $ de cada una de ellas en el momento de hacer la consulta, así como el histórico de transacciones de las últimas 10. \n12.Guardar la información actual en memoria de todas las criptomonedas, los usuarios y la información financiera de cada usuario. \n13.Salir.")    
            opcion = int(input("Introduzca una opcion: "))

        elif opcion == 13:
            print("Ha salido.")

if __name__ == "__main__":
    main()

    
