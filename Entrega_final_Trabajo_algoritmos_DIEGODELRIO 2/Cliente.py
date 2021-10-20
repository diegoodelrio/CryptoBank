import Usuario
from Generos import EnumSexo, SexoTypeError
from datetime import date, datetime
from Utilidades import UsuarioTypeError
import Cripto

class Cliente(Usuario.Usuario):
    '''
    Clase que representa a un tipo de usuaio, el cual es un Cliente.

    METODOS

    :__init__: constructor
    '''
    IdCliente = 0
    def __init__(self, id, nombre, apellido, NIF, nacionalidad, sexo, fecha_nacimiento, fecha_registro, contraseña):
        '''
        Constructor de la clase Cliente.

        Atributos 
        ---
        El cliente hereda todos los atributos de la clase Usuario.

        :param id_cliente: hace referencia a un id que solo pueden tener los clientes.
        '''

        super().__init__(id, nombre, apellido, NIF, nacionalidad, sexo, fecha_nacimiento, fecha_registro, contraseña)

    #METODOS DE LA CLASE CLIENTE

    def __str__(self):
        return Usuario.Usuario.__str__(self) + "\n Tipo Usuario: " + str(type(self).__name__)

    def modificar_usuario(self, nuevo_nombre, nuevo_apellido, nuevo_cumple, nuevo_sexo, nueva_nacionalidad):
        '''
        Metodo de la clase Cliente para modificarse a si mismo.
        '''
        if isinstance(self, Usuario.Usuario):
            self.set_nombre(nuevo_nombre)
            self.set_apellido(nuevo_apellido)
            self.set_fecha_nacimiento(nuevo_cumple)
            self.set_sexo(nuevo_sexo)
            self.set_nacionalidad(nueva_nacionalidad)
            return self
        else:
            raise UsuarioTypeError("El usuario a modificar tiene que ser un usuario.")
    
    def transferencia_cliente(self, destino, cantidad, Moneda):
        '''
        Metodo de la clase Cliente para realizar una transferencia.
        '''
        if isinstance(cantidad,(float,int)):
            if isinstance(destino, Usuario.Usuario):
                if isinstance(Moneda, str):
                    self.transferencia(destino, cantidad, Moneda)
                else:
                    raise UsuarioTypeError("La moneda para transferirla debe indicarla mediante el nombre.")
            else:
                raise UsuarioTypeError("El otro ha de ser un usuario.")
        else:
            raise UsuarioTypeError("La cantidad a transferir tiene que ser un entero")

def main():

    CLIENTE = Cliente(1, "Felipe II", "Borbon", "73898702T", "España", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(), datetime.strptime('2020/12/25', '%Y/%m/%d').date(), "ContraseñaCliente")

    Usuario1 = Usuario.Usuario(1, "Diego", "Del Rio", "5377689R", "España", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(), datetime.strptime('2020/12/25', '%Y/%m/%d').date(), "Contraseña1")
    identificadorUser1 = Usuario1.get_id()
    
    Usuario2 = Usuario.Usuario(2, "Juan", "Del Rio", "5377689R", "España", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(), datetime.strptime('2020/12/25', '%Y/%m/%d').date(), "Contraseña2")
    identificadorUser2 = Usuario2.get_id()

    CriptoUsuario1 = Cripto.Criptomoneda(1,"BITCOIN", 8617.17, 0.00000001, True, 21000000)
    identificadorCriptomo = CriptoUsuario1.get_nombre()

    CriptoUsuario2 = Cripto.Criptomoneda(1,"BITCOIN", 8617.17, 0.00000001, True, 21000000)
    identificadorCriptomo2 = CriptoUsuario2.get_nombre()
    
    CLIENTE.crear_cuenta(identificadorCriptomo, identificadorUser1, NuevaCantidad=200.0)
    Usuario2.crear_cuenta(identificadorCriptomo2, identificadorUser2, NuevaCantidad=200.0)

    try:
        Cliente1 = Cliente(2, "Joan", "Gamper", "73898702T", "España", EnumSexo.HOMBRE, datetime.strptime('2000/11/06', '%Y/%m/%d').date(), datetime.strptime('2020/12/25', '%Y/%m/%d').date(), "ContraseñaCliente")
        print("Test crear Cliente PASADO!!")
        #print(Cliente1)
    except Exception as e:
        print("Test crear cliente FAILED!! ")
        raise e
    
    try:
        CLIENTE.modificar_usuario("Alberto", "Gil", datetime.strptime('2001/11/06', '%Y/%m/%d').date(), EnumSexo.HOMBRE, "Peru")
        #print(CLIENTE)
        print("Test modificar cliente PASADO!!")
    except Exception as e:
        print("Test modificar cliente FAILED!! ")
        raise e

    try:
        CLIENTE.transferencia(Usuario2, 100, "BITCOIN")
        #print(CLIENTE.get_lista_cuentas())
        #print(Usuario2.get_lista_cuentas())
        print("Test transferencia de cliente PASADO!!")
    except Exception as e:
        print("Test transferencia de cliente FAILED!! ")
        raise e


if __name__ == "__main__":
    main()