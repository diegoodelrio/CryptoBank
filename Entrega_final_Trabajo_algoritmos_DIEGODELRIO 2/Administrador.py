import Usuario
from Generos import EnumSexo, SexoTypeError
from datetime import date, datetime
from Utilidades import UsuarioTypeError
from Utilidades import RepitedCripto
import CSV
import Cripto
import Cliente

class Administrador(Usuario.Usuario):
    '''
    Clase que representa a un tipo de usuaio, el cual es un Administrador.

    METODOS

    :__init__: constructor
    '''
    IdAdministrador = 0
    def __init__(self, id, nombre, apellido, NIF, nacionalidad, sexo, fecha_nacimiento, fecha_registro, contraseña):
        '''
        
        Constructor de la clase Administrador.

        Atributos 
        ---
        El Administrador hereda todos los atributos de la clase Usuario con super().__init__
        '''
        super().__init__(id, nombre, apellido, NIF, nacionalidad, sexo, fecha_nacimiento, fecha_registro, contraseña)
        
    
    #METODOS DE LA CLASE ADMINISTRADOR

    def transferencia(self, destino, cantidad, Moneda,origen = None):
        '''
        Metodo mediante el cual un administrador realiza una transferencia de un usuario origen a un usuario destino.

        :param origen: Se corresponde con un Usuario existente.

        :param destino: Se corresponde con otro Usuario existente, el que va a recibir el dinero.

        :param cantidad: Numero entero o decimal que se corresponde con la cantidad a transferir

        No devuelve nada, sino que llama a el metodo de la clase usuario.
        '''
        try:
            if origen != None:
                if isinstance(destino, Usuario.Usuario):
                    if isinstance(cantidad, (float, int)):
                        if isinstance(Moneda, str):
                            if isinstance(origen, Usuario.Usuario):
                                origen.transferencia(destino, cantidad, Moneda)
                            else:
                                raise (UsuarioTypeError("El origen de la transferencia tiene que ser de tipo Usuario."))
                        else:
                            raise UsuarioTypeError("La moneda se debe indicar mediante el nombre para realizar la transferencia.")
                    else:
                        raise(UsuarioTypeError("La cantidad a transferir tiene que ser un int o un float."))
                else:
                    raise(UsuarioTypeError("El destino de la trasnferecia tiene que ser de tipo Usuario."))
            else:
                if isinstance(cantidad, (float, int)):
                    if isinstance(destino, Usuario.Usuario):
                        for i in self.get_lista_cuentas():
                            for j in destino.get_lista_cuentas():
                                if (i.get_moneda() == j.get_moneda()):
                                    i.transferencia(j, cantidad)                 
                    else:
                        raise UsuarioTypeError("El otro ha de ser un usuario.")
                else:
                    raise UsuarioTypeError("La cantidad a transferir ha de ser un entero.")

        
        except Exception as e:
            raise e

    def crear_cripto(self, NombreCripto, NuevoValor, NuevoPrecio, Contratos, Nuevas_maxUnis, lista, NuevoID = None):
        '''
        Metodo de la clase Administrador para crear criptomonedas.

        :param NombreCripto: Se corresponde con el nombre de la nueva cripto.

        :param NuevoValor: Se corresponde con el valor en USD de la nueva cripto.

        :param NuevoPrecio: Se corresponde con el precio de transaccion de la nueva cripto.

        :param NombreCripto: Se corresponde con el nombre de la nueva cripto.

        :param Contratos: Se corresponde con un booleano True o False.

        :param Nuevas_maxUnis: Se corresponde con el volumen de la nueva cripto.

        :NuevoID: se corresponde con el id dado a la nueva cripto.

        :param ruta: Se corresponde con el nombre del fichero csv que contiene las criptos, este es por defecto InfoCriptomonedas.csv .

        '''
        try:
            cripto1 = Cripto.Criptomoneda(NuevoID, NombreCripto, NuevoValor, NuevoPrecio, Contratos, Nuevas_maxUnis)
            for cripto in lista:
                if (cripto.get_nombre() == cripto1.get_nombre()):
                    raise RepitedCripto("La criptomoneda " + str(cripto.get_nombre()) + " ya existe.")
            
            lista.append(cripto1)
            return cripto1
        
        except Exception as e:
            raise e
    
    def modificar_usuario(self, nuevo_nombre, nuevo_apellido, nuevo_cumple, nuevo_sexo, nueva_nacionalidad, usuario_a_modificar = None):
        '''
        Metodo de la clase Administrador para modificar un usuario.

        :param usuario_a_modificar: Se corresponde con un Usuario existente, el cual se va a modificar.

        :params modificacion: Estos son nuevo_nombre, nuevo_apellido, nuevo_cumple, nuevo_sexo, nueva_nacionalidad, que hacen referencia a los atributos del Usuario.

        Llama a la funcion de la clase Usuario.
        '''
        if usuario_a_modificar != None:
            if isinstance(usuario_a_modificar, Usuario.Usuario):
                usuario_a_modificar.modificar_usuario(nuevo_nombre,nuevo_apellido,nuevo_cumple,nuevo_sexo,nueva_nacionalidad)
            else:
                raise UsuarioTypeError("El usuario a modificar a de ser un usuario.")
        else:
            self.set_nombre(nuevo_nombre)
            self.set_apellido(nuevo_apellido)
            self.set_fecha_nacimiento(nuevo_cumple)
            self.set_sexo(nuevo_sexo)
            self.set_nacionalidad(nueva_nacionalidad)
            return self

    def __str__(self):
        return Usuario.Usuario.__str__(self) + "\n Tipo Usuario: " + str(type(self).__name__)

def main():
    
    ADMIN = Administrador(5, "ALberto", "Gil", "73898702T", "España", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(), datetime.strptime('2020/12/25', '%Y/%m/%d').date(), "ContraseñaADMIN")
    
    Usuario1 = Usuario.Usuario(1, "Diego", "Del Rio", "5377689R", "España", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(), datetime.strptime('2020/12/25', '%Y/%m/%d').date(), "Contraseña1")
    identificadorUser1 = Usuario1.get_id()
    
    Usuario2 = Usuario.Usuario(2, "Juan", "Del Rio", "5377689R", "España", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(), datetime.strptime('2020/12/25', '%Y/%m/%d').date(), "Contraseña2")
    identificadorUser2 = Usuario2.get_id()

    CriptoUsuario1 = Cripto.Criptomoneda(1,"BITCOIN", 8617.17, 0.00000001, True, 21000000)
    identificadorCriptomo = CriptoUsuario1.get_nombre()

    CriptoUsuario2 = Cripto.Criptomoneda(1,"BITCOIN", 8617.17, 0.00000001, True, 21000000)
    identificadorCriptomo2 = CriptoUsuario2.get_nombre()
    
    Usuario1.crear_cuenta(identificadorCriptomo, identificadorUser1, NuevaCantidad=200.0)
    Usuario2.crear_cuenta(identificadorCriptomo2, identificadorUser2, NuevaCantidad=200.0)
    ADMIN.crear_cuenta(identificadorCriptomo2, identificadorUser2, NuevaCantidad=100000.0)

    try:
        admin1 = Administrador(4, "Joan", "Gamper", "73898702T", "España", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(), datetime.strptime('2020/12/25', '%Y/%m/%d').date(), "ContraseñaAdmin1")
        print("Test crear Administrador PASADO!!")
    except Exception as e:
        print("Test crear Administrador FAILED!! ")
        raise e 
    
    try:
        cripto4 = admin1.crear_cripto("LITECOIN", 132.0, 0.005, False, 100000000, [], 1)
        #print(cripto4)
        print("Test crear cripto PASADO!!")
    except Exception as e:
        "Test crear cripto FAILED!!"
        raise e
    
    try:
        ADMIN.transferencia(Usuario2, 200, "BITCOIN",Usuario1)
        #print(Usuario1.get_lista_cuentas())
        #print(Usuario2.get_lista_cuentas())
        print("Test transferencia administrador entre distintos usuarios PASADO!!")
    except Exception as e:
        print("Test transferencia administrador entre distintos usuarios FAILED!!")
        raise e
    
    try:
        ADMIN.modificar_usuario("Alberto", "Gil", datetime.strptime('2001/11/06', '%Y/%m/%d').date(), EnumSexo.HOMBRE, "Peru", Usuario1)
        #print(Usuario1)
        print("Test modificar usuario PASADO!!")
    except Exception as e:
        print("Test modificar usuario FAILED!!")
        raise e
    
    try:
        ADMIN.modificar_usuario("Xavi", "Alonso", datetime.strptime('2001/11/06', '%Y/%m/%d').date(), EnumSexo.HOMBRE, "Peru", usuario_a_modificar= None)
        #print(ADMIN)
        print("Test modificar a uno mismo PASADO!!")
    except Exception as e:
        print("Test modificar a uno mismo FAILED!!")
        raise e 
    
    try:
        ADMIN.transferencia(Usuario2, 200, "BITCOIN",origen= None)
        #print(ADMIN.get_lista_cuentas())
        #print(Usuario2.get_lista_cuentas())
        print("Test transferencia del administrador a otro PASADO!!")
    except Exception as e:
        print("Test transferencia del administrador a otro FAILED!!")
        raise e
    
if __name__ == "__main__":
    main()
