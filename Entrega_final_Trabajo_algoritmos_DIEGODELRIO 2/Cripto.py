try:
    from Utilidades import CriptomonedaTypeError
except ImportError as IE:
    print(IE, "No se ha podido importar el modulo.")

class Criptomoneda:
    '''
    Clase criptomoneda
    '''
    IdCriptomoneda = 0
    def __init__(self, id = None, nombre = None, valor_USD = None, precio_transaccion = None, creacion_contratos = None, max_unidades = None):
        '''
        Constructor de la clase criptomoneda.

        Atributos
        ---
        :param id: Es un entero que representa el id de la criptomoneda.
        
        :param nombre: Es una string que reprensenta el nombre de la criptomoneda.
        
        :param max_unidades: Numero entero que indica la cantidad maxima de unidades de la criptomoneda.
        
        :param valor_USD: Numero decimal que representa el valor de la criptomoneda con respecto al dolar.
        
        :param precio_transaccion: Es un numero decimal que representa el precio de la transaccion.
        
        :param creacion_contratos: Es un booleano que indica si se permite o no la creacion de contratos.
         
        '''
        if not isinstance(id, int):
            raise TypeError("El id a de ser un entero.")
        else:
            if id == 0:
                self.__id = id
                Criptomoneda.IdCriptomoneda += 1
            else:
                Criptomoneda.IdCriptomoneda += 1
                self.__id = Criptomoneda.IdCriptomoneda

        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise CriptomonedaTypeError("El nombre ha de ser un string.")

        if isinstance(valor_USD, float) or isinstance(valor_USD, int):
            self.__valor_USD = valor_USD
        else:
            raise CriptomonedaTypeError("El valor ha de ser un numero decimal.")

        if isinstance(precio_transaccion, float) or isinstance(precio_transaccion, int):
            self.__precio_transaccion = precio_transaccion
        else:
            raise CriptomonedaTypeError("El precio ha de ser un numero decimal.")

        if isinstance(creacion_contratos, bool):
            self.__creacion_contratos = creacion_contratos
        else:
            raise CriptomonedaTypeError("El contraro ha de ser un booleano True o False.")
        
        if isinstance(max_unidades, int):
            if max_unidades >= 0:
                self.__max_unidades = max_unidades
            else:
                raise ValueError("El numero de unidades ha de ser mayor que 0.")
        else:
            raise CriptomonedaTypeError("El numero de unidades ha de ser un decimal.")

    
    #GETTERS DE LA CLASE CRIPTOMONEDA

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre
    
    def get_valorUSD(self):
        return self.__valor_USD
    
    def get_precioTransaccion(self):
        return self.__precio_transaccion
    
    def get_contratos(self):
        return self.__creacion_contratos
    
    def get_maxUnidades(self):
        return self.__max_unidades
    
    #SETTERS DE LA CLASE CRIPTOMONEDA

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise CriptomonedaTypeError("El nombre tiene que ser una string.")

    def set_valorUSD(self, valor_USD):
        if isinstance(valor_USD, float) or isinstance(valor_USD, int):
            self.__valor_USD = valor_USD
        else:
            raise CriptomonedaTypeError("El valor de la cripromoneda en $ ha de ser un numero decimal.")

    def set_precioTransaccion(self, precio_transaccion):
        if isinstance(precio_transaccion, float) or isinstance(precio_transaccion, int):
            self.__precio_transaccion = precio_transaccion
        else:
            raise CriptomonedaTypeError("El precio ha de ser un valor decimal.")
        
    def set_creacionContratos(self, creacion_contratos):
        if isinstance(creacion_contratos, bool):
            self.__creacion_contratos = creacion_contratos
        else:
            raise CriptomonedaTypeError("El contrato ha de ser un booleano True o False.")
        
    def set_maxUnidades(self, max_unidades):
        if isinstance(max_unidades, int):
            if max_unidades >= 0:
                self.__max_unidades = max_unidades
            else:
                raise ValueError("La cantidad de unidades ha de ser positivo.")
        else:
            raise CriptomonedaTypeError("El numero de unidades ha de ser un decimal.")
    
    #METODOS DE LA CLASE CRIPTOMONDEA

    def guardar_cripto(self, ruta):
        ruta.write(str(self.__id) + "," + str(self.__nombre) + "," + str(self.__valor_USD) + "," + str(self.__precio_transaccion) + "," + str(self.__creacion_contratos) + "," + str(self.__max_unidades) + "\n")


    def __str__(self):
        return "ID: " + str(self.__id) + "\n Nombre: " + str(self.__nombre) + "\n Valor($): " + str(self.__valor_USD) + "\n Precio: " + str(self.__precio_transaccion) + "\n Contrato(Si/No): " + str(self.__creacion_contratos) + "\n Maximas Unidades: " + str(self.__max_unidades)

    def __repr__(self):
        return self.__str__().replace("\n","") + "\n"
        
    def __hash__(self):
        '''
        Overrides the default implementation of hash
        '''
        print(self.__valor_USD, hash(self.__valor_USD))
        return hash(self.__valor_USD)
    
    def __eq__(self, other):
        '''
        Overrides the default implementation of equals
        '''
        if (other == None):
            return False
        if isinstance(other, Criptomoneda):
            if (self.get_id() == other.get_id()):
                return True
        return False

        
    def text(self):
        text = ""
        text += "ID: " + str(self.__id)
        text += "\nNombre: " + self.__nombre
        text += "\nMaximas Unidades: " + self.__max_unidades
        text += "\nValor($): " + self.__valor_USD
        text += "\nPrecio: " + self.__precio_transaccion
        text += "\nContrato: " + self.__creacion_contratos
        
        return text
    

def main():
    #TEST!!!
    #Al ejecutar error
    cripto1 = Criptomoneda(1, "Bitcoin", 8617.17, 0.00000001, True, 21000000)
    print("---------------ERROR-------------")
    try:
        malaCripto = Criptomoneda("1", "Bitcoin", 8617.17, 0.00000001, True, 21000000)
        #print(malaCripto)
    except TypeError:
        print("Se ha producido un error. Comprueba que los datos estan bien introducidos.")
    
    #Ejecutable
    print("---------------NO ERROR-------------")
    try:
        buenaCripto = Criptomoneda(1, "Bitcoin", 8617.17, 0.00000001, True, 21000000)
        #print(buenaCripto)
        print("Test pasado")
    except TypeError:
        print("Se ha producido un error. Comprueba que los datos estan bien introducidos.")

    try:
        cripto1.__hash__()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
        
    