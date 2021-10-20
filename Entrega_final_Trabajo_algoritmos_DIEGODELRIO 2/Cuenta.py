try:
    from datetime import date, datetime
    from Utilidades import CuentaTypeError
    from Cripto import Criptomoneda
    import Usuario
    from Generos import EnumSexo
    import Transferencias

except ImportError as IE:
    print(IE, "No se ha podido importar el modulo.")

class Cuenta:
    '''
    Clase cuenta
    '''
    IdCuenta = 1
    def __init__(self, id = None, usuario = None, moneda = None, cantidad = None, fecha_inicio = None):
        '''
        Constructor de la clase Cuenta.

        Atributos
        ---
        :param id: Numero entero que indica el id de la cuenta.

        :param usuario: String que indica el usuario de la cuenta.
        
        :param moneda: Indica el tipo de moneda de la criptomoneda.
        
        :param cantidad: Float que indica la cantidad de dinero.
        
        :param fecha_inicio: Fecha en la que el ususario obtuvo su primer saldo de cada moneda.
        
        :param transferencia: Float que hace referencia al historial de las transacciones realizadas. 
        '''
        if isinstance(id,int):
            self.__id = id
            if (Cuenta.IdCuenta <= id):
                Cuenta.IdCuenta = id + 1
        else:
            self.__id = Cuenta.IdCuenta
            Cuenta.IdCuenta = Cuenta.IdCuenta + 1

        if isinstance(usuario, int):
            self.__usuario = usuario
        else:
            raise CuentaTypeError("El usuario ha de ser un usuario existente.")

        if isinstance(moneda, str):
            self.__moneda = moneda
        else:
            raise CuentaTypeError("La moneda ha de ser una criptomoneda existente.")
        
        if isinstance(cantidad, (float,int)):
            self.__cantidad = cantidad
        else:
            raise CuentaTypeError("La cantidad ha de ser un numero decimal")
        
        if fecha_inicio == None:
            self.__fecha_inicio = date.today()
        elif isinstance(fecha_inicio, date):
            self.__fecha_inicio = fecha_inicio
        else:
            raise CuentaTypeError("FECHA NO VALIDA")

        self.__transacciones = []

    #SETTERS DE LA CLASE CUENTA

    def set_usuario(self, usuario):
        if isinstance(usuario, int):
            self.__usuario = usuario
        else:
            raise CuentaTypeError("El usuario ha de ser un usuario existente.")
    
    def set_moneda(self, moneda):
        if isinstance(moneda, str):
            self.__moneda = moneda
        else:
            raise CuentaTypeError("La moneda ha de ser una criptomoneda existente.")
        
    def set_cantidad(self, cantidad):
        if isinstance(cantidad, (float,int)):
            self.__cantidad = cantidad
        else:
            raise CuentaTypeError("La cantidad ha de ser un numero decimal")
    
    def set_fecha_inicio(self, fecha_inicio):
        if isinstance(fecha_inicio, date):
            self.__fecha_inicio = fecha_inicio
        else:
            raise CuentaTypeError("La fecha de inicio ha de ser una fecha.")
        
    def set_transaccion(self, transaccion):
        if isinstance(transaccion, list):
            self.__transacciones = transaccion
        else:
            raise CuentaTypeError("Las transacciones añadidas tienen que ser una lista.")

    #GETTERS DE LA CLASE CUENTA

    def get_id(self):
        return self.__id
    
    def get_usuario(self):
        return self.__usuario
    
    def get_moneda(self):
        return self.__moneda
    
    def get_cantidad(self):
        return self.__cantidad
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def get_transacciones(self):
        return self.__transacciones

    #METODOS DE LA CLASE CUENTA

    def Ingresar_dinero(self, cantidad):
        '''
        Metodo de la clase Cuenta mediante la cual se ingresa dinero en la cuenta

        :param cantidad: Numero decimal o entero que se corresponde con la cantidad a ingresar

        return: True en caso de que la cantidad se haya ingresao con exito, False en caso contrario.
        '''
        if isinstance(cantidad, (float, int)):
            if (cantidad > 0):
                suma = self.__cantidad + cantidad
                self.set_cantidad(suma)
            else:
                raise ValueError("La cantidad tiene que ser mayor que 0")
        else:
            raise TypeError("La cantidad ha de ser un numero entero o decimal.")

    
    def Retirar_dinero(self, cantidad):
        '''
        Metodo de la clase Cuenta mediante la cual se retira dinero de la cuenta

        :param cantidad: Numero decimal o entero que se conrresponde con la cantidad a retirar.

        return: True en caso de que la cantidad se haya retirado con exito, False en caso contrario.
        '''
        if isinstance(cantidad, float) or isinstance(cantidad, int):
            saldo = self.__cantidad
            if cantidad > saldo:
                print("Error, la cantidad que quiere retirar excede su saldo existente.")
            elif cantidad <= saldo:
                saldo -= cantidad
                self.__cantidad = saldo
                return {True: "La cantidad " + str(cantidad) + " ha sido retirada con exito."}
        else:
            print("La cantidad debe ser un numero entero o decimal.")


    def transferencia(self, otra_cuenta, cantidad):
        '''
        Metodo de la clase cuenta para transferir una cantidad de criptomonedas de un usuario a otro

        :param otra_cuenta: Se corresponde con otra cuenta existente.

        :param cantidad: Numero entero o decimal que se corresponde con la cantidad a transferir

        :return True si la transferencia se ha realizado con exito, False en caso contrario.
        '''
        if isinstance(otra_cuenta, Cuenta):
            if isinstance(cantidad, float) or isinstance(cantidad, int):
                if cantidad <= self.__cantidad:
                    self.__cantidad -= cantidad
                    cantidad_otra_cuenta = otra_cuenta.get_cantidad()
                    otra_cuenta.set_cantidad(cantidad_otra_cuenta + cantidad)

                    nueva_trans = Transferencias.Transferencia(id_transaccion= 1, origen= self.get_id(), destinatario= otra_cuenta.get_id(), fecha= None, cantidad= cantidad, cripto=self.get_moneda())
                    self.__transacciones.append(nueva_trans)
                    return nueva_trans
                else:
                    print("La cantidad a transferir no puede exceder su saldo.")
            else:
                print("La cantidad a de ser un numero entero o decimal.")
        else:
            print("La cuenta a la que se quiere transferir dinero no existe o esta mal introducida, por favor reviselo.")

    def ids_transferencias(self):
        '''
        Metodo de la clase Cuenta para conseguir los ids de la transferencias de un usuario.

        :return una lista con los id's de las transferencias del usuario.
        '''
        ref_transferencias = []
        for transferencia in self.get_transacciones():
            ref_transferencias.append(transferencia.get_id())
        if len(ref_transferencias) >= 0:
            return ref_transferencias
        else:
            return("Este usuario no a realizado ninguna transferencia.")

    def get_informacion_transferencias(self, id_transferencia):
        '''
        Metodo de la clase Usuario que accede a la cuenta del usuario a traves de la referencia del user.

        :param id_cuenta: hace referencia a el id de la cuenta que posee el usuario.

        :return la informacion de la cuenta.
        '''

        referencia = self.ids_transferencias()
        if not isinstance(id_transferencia, int):
            raise CuentaTypeError("La referencia de la transferencia a de ser un entero.")
        elif id_transferencia not in referencia:
            raise CuentaTypeError("La transferencia no la tiene el usuario.")
        else:
            for transferencia in self.get_transacciones():
                if transferencia.get_id() == id_transferencia:
                    return transferencia


    def guardar_cuenta(self, ruta):
        ruta.write(str(self.__id) + "," + str(self.__usuario) + "," + str(self.__moneda) + "," + str(self.__cantidad) + "," + str(datetime.strftime(self.__fecha_inicio,'%Y/%m/%d')) + "\n")

    def __str__(self):
        return ('\nID: ' + str(self.__id) + '\n Usuario: ' + str(self.__usuario) + '\n Tipo de moneda: ' + str(self.__moneda) + '\n Cantidad: ' + str(self.__cantidad) + '\n Fecha de inicio: ' + str(self.__fecha_inicio) + "\n Transacciones: " + str(self.__transacciones))
    
    def __repr__(self):
        return self.__str__().replace("\n","") + "\n"
    
def main():
    CriptomonedaCuenta = Criptomoneda(1,"BITCOIN", 8617.17, 0.00000001, True, 21000000)
    identificadorCripto = CriptomonedaCuenta.get_nombre()

    UsuarioCuenta = Usuario.Usuario(1, "Juan", "Sanchez", "56774892E", "España", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(),  datetime.strptime('2020/12/25', '%Y/%m/%d').date())
    identificadorUsuario = UsuarioCuenta.get_id()

    UsuarioCuenta2 = Usuario.Usuario(1, "Jorge", "Mestillo", "78392098K", "Alemania", EnumSexo.HOMBRE, datetime.strptime('2003/12/05', '%Y/%m/%d').date(),  datetime.strptime('2020/12/25', '%Y/%m/%d').date())
    identificadorUsuario2 = UsuarioCuenta2.get_id()

    miCuenta = Cuenta(1, identificadorUsuario, identificadorCripto, 200.0, datetime.strptime('2020/12/25', '%Y/%m/%d').date())
    miCuenta2 = Cuenta(1, identificadorUsuario2, identificadorCripto, 100.0, datetime.strptime('2020/12/25', '%Y/%m/%d').date())

    try:
        miCuenta.Ingresar_dinero(200.0)
        print("Test ingresar dinero pasado!!")
        #print(miCuenta)
    except Exception as e:
        print("Test ingresar dinero failed")
        #print(e)
    
    try:
        miCuenta.Ingresar_dinero("asd")
        print("Test cantidad en str failed!!")
    except Exception as e:
        print("Test cantidad en str pasado!!")
        #print(e)
    
    try:
        miCuenta.Ingresar_dinero(-5)
        print("Test cantidad negativa failed!!")
    except Exception as e:
        print("Test cantidad cantidad negativa pasado!!")
        #print(e)

    try:
        miCuenta.Retirar_dinero(50.0)
        print("Test retirar dinero pasado!!")
        #print(miCuenta)
    except Exception as e:
        print("Test retirar dinero failed")
        print(e)

    try:
        miCuenta.transferencia(miCuenta2, 100)
        print("Test de transferencia pasado!!")
        #print(miCuenta)
        #print("\n")
        #print(miCuenta2)
    except Exception as e:
        print("Test de transferencia failed")
        print(e)  
       
if __name__ == "__main__":
    main()
    
