try:
    from Generos import EnumSexo, SexoTypeError
    from datetime import date, datetime
    import random
    from Utilidades import UsuarioTypeError, NotFoundException, RepitedCuenta
    import Cuenta
    from Cripto import Criptomoneda
    import csv
    import os.path
    

except ImportError as IE:
    print(IE, "No se ha podido importar el modulo.")
    raise IE

class Usuario:
    '''
    Clase que hace referencia al usuario.
    '''
    lista_usuarios = []
    IdUsuarios = 0
    def __init__(self, id = None, nombre = None, apellido = None, NIF = None, nacionalidad = None, sexo = None, fecha_nacimiento = None, fecha_registro = None, contraseña = None):
        '''
        Construcror de la clase Usuario.

        Atributos
        ---
        :param id: Numero entero que indica el id del usuario.

        :param nombre: String que muestra el nombre del usuario.

        :param apellido: String que muestra el apellido del usuario.
        
        :param NIF: Numero entero que muestra el dni del usuario.

        :param nacionalidad: String que muestra la nacionalidad del usuario.

        :param sexo: Enumeracion que muestra el genero del usuario.
        
        :param fecha_nacimiento: Fecha que muestra el dia de nacimiento del usuario.
        
        :param fecha_registro: Fecha que muestra la fecha de registro del usuario.

        '''
        
        if not isinstance(id, int):
            raise UsuarioTypeError("El id a de ser un entero.")
        elif (id <= Usuario.IdUsuarios):
            self.__id = Usuario.IdUsuarios + 1
            Usuario.IdUsuarios += 1
        else:
            self.__id = id
            Usuario.IdUsuarios = id

        if nombre == None:
            self.__nombre = Usuario.__nombre_random()
        elif isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise UsuarioTypeError("El nombre ha de ser una string.")

        if apellido == None:
            self.__apellido = Usuario.__apellido_random()
        elif isinstance(apellido, str):
            self.__apellido = apellido
        else:
            raise UsuarioTypeError("El apellido ha de ser una string.")
        
        if NIF == None:
            self.__NIF = Usuario.__NIF_random()
        elif isinstance(NIF, str):
            self.__NIF = NIF
        else:
            raise UsuarioTypeError("El NIF ha de ser una string debido a la letra final.")

        if nacionalidad == None:
            self.__nacionalidad = Usuario.__nacionalidad_random()
        elif isinstance(nacionalidad, str):
            self.__nacionalidad = nacionalidad
        else:
            raise UsuarioTypeError("La nacionalidad ha de ser una string.")
        
        if sexo == None:
            self.__sexo = Usuario.__sexo_random()
        elif isinstance(sexo, EnumSexo):
            self.__sexo = sexo
        else:
            raise SexoTypeError("El sexo ha de ser un enum.")

        if fecha_nacimiento == None:
            self.__fecha_nacimiento = date.today()
        elif isinstance(fecha_nacimiento, date):
            self.__fecha_nacimiento = fecha_nacimiento
        else:
            raise UsuarioTypeError("FECHA NO VALIDA")

        if fecha_registro == None:
            self.__fecha_registro = date.today()
        elif isinstance(fecha_registro, date):
            self.__fecha_registro = fecha_registro
        else:
            raise UsuarioTypeError("FECHA NO VALIDA")
        
        if contraseña == None:
            self.__contraseña = Usuario.__contraseña_random()
        elif isinstance(contraseña, str):
            self.__contraseña = contraseña
        else:
            raise UsuarioTypeError("CONTRASEÑA NO VALIDA")
        
        self.__lista_cuentas = []

    #SETTERS DE LA CLASE USUARIO
        
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise UsuarioTypeError("El nombre introducido en el set ha de ser una string.")

    def set_apellido(self, apellido):
        if isinstance(apellido, str):
            self.__apellido = apellido
        else:
            raise UsuarioTypeError("El apellido introducido en el set ha de ser una string.")
    
    def set_NIF(self, NIF):
        if isinstance(NIF, str):
            self.__NIF = NIF
        else:
            raise UsuarioTypeError("El NIF introducid0 en el set ha de ser un string debido a la letra final.")
    
    def set_nacionalidad(self, nacionalidad):
        if isinstance(nacionalidad, str):
            self.__nacionalidad = nacionalidad
        else:
            raise UsuarioTypeError("La nacionalidad introducida en el set ha de ser un string.")
    
    def set_sexo(self, sexo):
        if isinstance(sexo, EnumSexo):
            self.__sexo = sexo
        else:
            raise SexoTypeError("El sexo introducido en el set a de ser Hombre o Mujer.")
    
    def set_fecha_nacimiento(self, fecha_nacimiento):
        if isinstance(fecha_nacimiento, date):
            self.__fecha_nacimiento = fecha_nacimiento
        else:
            raise UsuarioTypeError("La fecha de nacimiento introducida en el set tiene que ser una fecha")

    def set_fecha_registro(self, fecha_registro):
        if isinstance(fecha_registro, date):
            self.__fecha_registro = fecha_registro
        else:
            raise UsuarioTypeError("La fecha de registro introducida en el set ha de ser una fecha.")
    
    def set_lista_cuenta(self, lista_cuentas):
        if isinstance(lista_cuentas, list):
            self.__lista_cuentas = lista_cuentas
        else:
            raise UsuarioTypeError("La lista de cuentas introducida en el set tiene que ser una lista.")
        
    def set_contraseña(self, contraseña):
        if isinstance(contraseña, str):
            self.__contraseña = contraseña
        else:
            raise UsuarioTypeError("La contraseña introducida en el set ha de ser tipo string.")

    #GETTERS DE LA CLASE USUSARIO

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido

    def get_NIF(self):
        return self.__NIF
    
    def get_nacionalidad(self):
        return self.__nacionalidad
    
    def get_sexo(self):
        return self.__sexo
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    def get_fecha_registro(self):
        return self.__fecha_registro

    def get_lista_cuentas(self):
        return self.__lista_cuentas
    
    def get_contraseña(self):
        return self.__contraseña

    #METODOS DE LA CLASE USUARIO

    def crear_cuenta(self, NuevaCripto, idUsuario, nuevoid = None, NuevaCantidad = None, fechaInicio = None):
        '''
        Metodo de la clase Usuario para crear una cuenta.

        :param NuevaCripto: hace referencia al nombre de la cripto que se desea ingresar en la cuenta.

        :param idUsuario: hace referencia al id del usuario propietario de la cuenta.

        :param nuevoid: hace referencia al id que va a tener la cuenta, por defecto es None.

        :param NuevaCantidad: hace referencia a la cantidad que se va ingresar en la nueva cuenta, por defecto es 0.0.

        :param fechaInicio: hace referencia a la fecha en la que se crea la cuenta.
        
        No devuelve nada, sino que se añade la cuenta a la lista de cuentas del usuario.
        '''
        try:
            cuenta1 = Cuenta.Cuenta(nuevoid, idUsuario, NuevaCripto, NuevaCantidad, fechaInicio)
            for criptoInCuenta in self.__lista_cuentas:
                if(criptoInCuenta.get_moneda() == NuevaCripto):
                    raise RepitedCuenta("El usuario ya tiene una cuenta del tipo: " + str(NuevaCripto))

            self.__lista_cuentas.append(cuenta1)
            return cuenta1
        except Exception as e:
            raise e
    
    def depostiar_dinero(self, Moneda, Cantidad):
        '''
        Metodo de la clase Usuario para depositar una cantidad de dinero de una criptomoneda en una cuenta.

        :param Moneda: hace referencia al nombre de la criptomoneda que se desea retirar.

        :param Cantidad: hace referencia a la cantidad que se desea retirar.

        No se devuelve nada, sino que este metodo llama al metodo de la clase Cuenta que se corresponde con el de ingresar dinero.
        '''
        found = False
        if isinstance(Cantidad, (float, int)) and Cantidad > 0:
            for cuenta in self.__lista_cuentas:
                if isinstance(cuenta, Cuenta.Cuenta):
                    if(cuenta.get_moneda() == Moneda):
                        cuenta.Ingresar_dinero(Cantidad)
                        found = True
                else:
                    raise UsuarioTypeError("La cuenta a la que quiere ingresar dinero tiene que existir.")
            if found == False:
                raise NotFoundException("El usuario no tiene una cuenta de: " + str(Moneda))        
        else:
            raise UsuarioTypeError("La cantidad a ingresar tiene que ser un numero entero o decimal mayor que 0. ")

    def retirar_dinero(self, Moneda, Cantidad):
        '''
        Metodo de la clase Usuario para retirar una cantidad de dinero de una criptomoneda en una cuenta.

        :param Moneda: hace referencia al nombre de la criptomoneda que se desea retirar.

        :param Cantidad: hace referencia a la cantidad que se desea retirar.

        No se devuelve nada, sino que este metodo llama al metodo de la clase Cuenta que se corresponde con el de retirar dinero.
        '''
        found = False
        if isinstance(Cantidad, (int, float)):
            for cuenta in self.__lista_cuentas:
                if isinstance(cuenta, Cuenta.Cuenta):
                    if(cuenta.get_moneda() == Moneda):
                        cuenta.Retirar_dinero(Cantidad)
                        found = True
                else:
                    raise UsuarioTypeError("La cuenta desde la que quiere sacar dinero tiene que existir.")
            if not found:
                raise NotFoundException("El usuario no tiene una cuenta de: " + str(Moneda))        
        else:
            raise UsuarioTypeError("La cantidad a retirar tiene que ser un numero entero o decimal mayor que 0.")  
        
        

    
    def transferencia(self, other, cantidad, Moneda):
        '''
        Metodo de la clase Usuario para realizar un traspaso de una cantidad de dinero a otro usuario.

        :param other: Hace referenica a otro Usuario existente.

        :param cantidad: Numero entero o decimal que hace referencia a la cantidad a transferir.

        No devuelve nada, sino que llama a la funcion de transferencia de la clase cuenta.
        '''
        if isinstance(cantidad, (float, int)):
            if isinstance(Moneda, str):
                if isinstance(other, Usuario):
                    for i in self.__lista_cuentas:
                        if i.get_moneda() == Moneda:
                            if isinstance(i, Cuenta.Cuenta):
                                for j in other.__lista_cuentas:
                                    if isinstance(j, Cuenta.Cuenta):
                                        if (i.get_moneda() == j.get_moneda()):
                                            i.transferencia(j, cantidad)
                                                
                                        else:
                                            print("El usuario de destino no posee esta criptomoneda.")
                                    else:
                                        raise(UsuarioTypeError("La cuenta a la que va a transferir dinero tiene que existir."))
                            else:
                                raise UsuarioTypeError("La cuenta desde la va a transferir dinero tiene que existir..")
                else:
                    raise UsuarioTypeError("Al que le va a enviar dinero tiene que ser un usuario existente.")
            else:
                raise UsuarioTypeError("Tienes que indicar la moneda mediante el nombre para iniciar la transaccion.")
        else:
            raise UsuarioTypeError("La cantidad tiene que ser un numero decimal o entero mayor que 0.")
            
    def eliminar_cuenta(self, currency):
        '''
        Metodo de la clase Usuario para eliminar una cuenta.

        :param currency: Hace referencia a el nombre de la criptomoneda.

        No devuelve nada, se elimina la cuenta directamente.
        '''
        try:
            if isinstance(currency, str):
                for cuenta in self.__lista_cuentas:
                    if isinstance(cuenta, Cuenta.Cuenta):
                        if (cuenta.get_moneda() == currency):
                            self.__lista_cuentas.remove(cuenta)
            
        except Exception as e:
            raise e

    def modificar_usuario(self, nuevo_nombre, nuevo_apellido, nuevo_cumple, nuevo_sexo, nueva_nacionalidad):
        '''
        Metodo de la clase Usuario para modificar un usuario

        :param nuevo_nombre: nuevo nombre que va a tomar el usuario.

        :param nuevo_apellido: nuevo apellido que va a tomar el usuario.

        :param nuevo_cumple: hace referencia a la nueva fecha de nacimiento del usuario.

        :param nuevo_sexo: hace referencia a el nuevo sexo que recibe el usuario.

        :param nueva_nacionalidad: hace referencia a la nueva nacionalidad del usuario.

        :return el usuario modificado.
        '''
        self.set_nombre(nuevo_nombre)
        self.set_apellido(nuevo_apellido)
        self.set_fecha_nacimiento(nuevo_cumple)
        self.set_sexo(nuevo_sexo)
        self.set_nacionalidad(nueva_nacionalidad)
        return self

    def ids_cuentas(self):
        '''
        Metodo de la clase Usuario para conseguir los ids de la cuentas de un usuario.

        :return una lista con los id's de las cuentas del usuario.
        '''
        referencias_cuentas = []
        for cuenta in self.get_lista_cuentas():
            referencias_cuentas.append(cuenta.get_id())
        if len(referencias_cuentas) >= 0:
            return referencias_cuentas
        else:
            return("Este usuario no tiene ninguna cuenta.")
    
    def get_informacion(self, id_cuenta):
        '''
        Metodo de la clase Usuario que accede a la cuenta del usuario a traves de la referencia del user.

        :param id_cuenta: hace referencia a el id de la cuenta que posee el usuario.

        :return la informacion de la cuenta.
        '''

        referencia = self.ids_cuentas()
        if not isinstance(id_cuenta, int):
            raise UsuarioTypeError("La referencia de la cuenta a de ser un entero.")
        elif id_cuenta not in referencia:
            raise UsuarioTypeError("La cuenta no la tiene el usuario.")
        else:
            for cuenta in self.get_lista_cuentas():
                if cuenta.get_id() == id_cuenta:
                    return cuenta
    
    def get_moneda_from_cuenta(self):
        '''
        Metodo de la clase Usuario que crea un diccionario con el id y la moneda de cada cuenta.

        Clave: el id de la cuenta del usuario.

        valor: el nombre de la moneda que tiene la cuenta.

        :return el diccionario.
        '''
        dict_nombres = {}
        for cuenta in self.get_lista_cuentas():
            dict_nombres[cuenta.get_id()] = cuenta.get_moneda()
        return dict_nombres
    
    def get_moneda_sorted(self):
        '''
        Metodo de la clase Usuario que crea un diccionario con el id y la moneda de cada cuenta.

        Clave: el nombre de la moneda que tiene la cuenta.

        valor: el id de la cuenta del usuario.

        :return los valores del diccionario ordenados.
        '''
        lista_ids = {}
        for cuenta in self.get_lista_cuentas():
            lista_ids[cuenta.get_moneda()] = cuenta.get_id()
        moneda = sorted(lista_ids)
        return moneda


    def guardar_usuario(self, ruta):
        ruta.write(str(self.__id) + ", " + str(self.__nombre) + "," + str(self.__apellido) + "," + str(self.__NIF) + "," + str(self.__nacionalidad) + "," + str(self.__sexo) + "," +  str(datetime.strftime(self.__fecha_nacimiento, '%Y/%m/%d'))  + "," + str(datetime.strftime(self.__fecha_registro, '%Y/%m/%d'))+ "," + str(self.__contraseña) + "," + str(type(self).__name__) + "\n")

    def __str__(self):
        return ('\nID: ' + str(self.__id) + '\n Nombre: ' + str(self.__nombre) + '\n Apellido: ' + str(self.__apellido) + '\n NIF: ' + str(self.__NIF) + '\n Nacionalidad: ' + str(self.__nacionalidad) + '\n sexo: ' + str(self.__sexo) + '\n Fecha nacimiento: ' + str(self.__fecha_nacimiento) + '\n Fecha registro ' + str(self.__fecha_registro) + '\n Lista_cuentas: ' + str(self.__lista_cuentas))

    def __repr__(self):
        return self.__str__().replace("\n","") + "\n"

    def text(self):
        text = ""
        text += "\nID usuario: " + self.__id
        text += "\nNombre: " + self.__nombre
        text += "\nApellidos: " + self.__apellido
        text += "\nNIF: " + self.__NIF
        text += "\nNacionalidad: " + self.__nacionalidad
        text += "\nGenero: " + self.__sexo
        text += "\nFecha de nacimiento: " + self.__fecha_nacimiento
        text += "\nFecha de registro: " + self.__fecha_registro  
        text += "\nLista de Usuarios: " + self.__lista_cuentas
        return text
    
    @staticmethod
    def __nombre_random():
        listaNombres = ['Diego','Jorge','Julian','Pablo','Benigno','Arantxa','Leo','Sergio','Araceli','Sabrina']
        return random.choice(listaNombres)

    @staticmethod
    def __apellido_random():
        listaApellidos = ['Del Rio','Rodriguez','Fernandez','Magadan','Pis','Arriondo','Del Bosque','Ramos','Ronaldo','Messi']
        return random.choice(listaApellidos)

    @staticmethod
    def __NIF_random():
        listaNIF = ['56473839M','63928361J','63018374H','63928105T','43726590J','14395739I','43829506Y','53647886M','56674893R','46677862T']
        return random.choice(listaNIF)

    @staticmethod
    def __nacionalidad_random():
        listaNacionalidades = ['España','Colombia','Alemania','Inglaterra','Brasil','USA','Argelia','Vietnam','Tailandia','Japon','Francia','Italia']
        return random.choice(listaNacionalidades)
    
    @staticmethod
    def __sexo_random():
        listaSexos = [EnumSexo.HOMBRE,EnumSexo.MUJER]
        return random.choice(listaSexos)
    
    @staticmethod
    def __contraseña_random():
        listaContraseñas = ["asdf123", "MacarronesConTomate1", "JamonIberico0", "Sol23", "Algoritmos4", "Algoritmos5", "BEST_30SS"]
        return random.choice(listaContraseñas)

def main():
    import Usuario

    Usuario1 = Usuario.Usuario(1, "Diego", "Del Rio", "5377689R", "España", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(), datetime.strptime('2020/12/25', '%Y/%m/%d').date(), "Contraseña1")
    #print(Usuario1)
    identificadorUser = Usuario1.get_id()

    CriptoUsuario = Criptomoneda(1,"BITCOIN", 8617.17, 0.00000001, True, 21000000)
    identificadorCriptomo = CriptoUsuario.get_nombre()

    #Esta cripto la creo para luego eliminarla en el metodo eliminar_cuenta.
    Cripto_a_eliminar = Criptomoneda(2, "ETHER", 212.27, 5.429, True, 100000000)
    identificadorCriptomoDELETE = Cripto_a_eliminar.get_nombre()

    Usuario2 = Usuario.Usuario(2, "Jose", "Lega", "5377689R", "Mozambique", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(), datetime.strptime('2020/12/25', '%Y/%m/%d').date(), "Contraseña2")
    identificadorUser2 = Usuario2.get_id()

    CriptoUsuario2 = Criptomoneda(1,"BITCOIN", 8617.17, 0.00000001, True, 21000000)
    identificadorCriptomo2 = CriptoUsuario2.get_nombre()

    #Creo una cuenta al usuario dos para asi poder hacer los test de transferencia.
    Usuario2.crear_cuenta(identificadorCriptomo2, identificadorUser2, NuevaCantidad=200.0)
    
    try:
        #Creo dos cuentas, la cuenta que tiene como identificador DELETE es para usarla en el metodo eliminar_cuenta.
        Usuario1.crear_cuenta(identificadorCriptomoDELETE, identificadorUser, NuevaCantidad=150.0)
        Usuario1.crear_cuenta(identificadorCriptomo, identificadorUser, NuevaCantidad=200.0)
        print("Test crear cuenta PASADO!!")
        #print(Usuario1)
    except Exception as e:
        print("Test crear cuenta FAILED!!")
        raise e

    try:
        Usuario1.depostiar_dinero(identificadorCriptomo, 10)
        print("Test depositar dinero PASADO!!")
        #print(Usuario1.get_lista_cuentas())
    except Exception as e:
        print("Test depositar dinero FAILED!! ")
        print(e)
    
    try:
        Usuario1.retirar_dinero(identificadorCriptomo, 5)
        print("Test retirar dinero PASADO!!")
        #print(Usuario1.get_lista_cuentas())
    except Exception as e:
        print("Test retirar dinero FAILED!! ")
        print(e)

    try:
        Usuario1.transferencia(Usuario2, 50.0, "BITCOIN")
        print("Test transferencia PASADO!!")
        #print(Usuario1.get_lista_cuentas())
        #print(Usuario2.get_lista_cuentas())    
    except Exception as e:
        print("Test transferencia FAILED!! ")
        raise e

    try:
        Usuario1.eliminar_cuenta(identificadorCriptomoDELETE)
        print("Test eliminar cuenta PASADO!!")
        #print(Usuario1.get_lista_cuentas())
    except Exception as e:
        print("Test eliminar cuenta FAILED!! ")
        raise e    

if __name__ == "__main__":
    main()