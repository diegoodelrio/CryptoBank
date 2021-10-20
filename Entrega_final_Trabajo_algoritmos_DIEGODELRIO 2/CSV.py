try:
    import Cliente
    import Administrador
    from Utilidades import BadFormatError
    import csv
    from Cripto import Criptomoneda
    import Usuario
    import Cuenta
    from Generos import EnumSexo
    import datetime
    import Transferencias
except ImportError as IE:
    print(IE, "No se ha podido importar el modulo.")

def leerCriptomoneda(ruta):
    '''
    Metodo para leer el csv de las criptomonedas
    '''
    listaCriptomonedas = []

    with open(ruta, 'r') as rd:
        archivo = csv.reader(rd)

        for fila in archivo:
            try:
                id_cripto = int(fila[0])
            except Exception as e:
                raise BadFormatError("the column ID should be a integer: Check the CSV format for this program")
            
            try:
                nombre = str(fila[1])
            except Exception as e:
                raise BadFormatError("the column nombre should be a string: Check the CSV format for this program")
            
            try:
                valor = float(fila[2])
            except Exception as e:
                raise BadFormatError("the column valor should be a float: Check the CSV format for this program")
            
            try:
                precio = float(fila[3])
            except Exception as e:
                raise BadFormatError("the column precio should be a float: Check the CSV format for this program")
            
            try:
                contratos = bool(fila[4])
            except Exception as e:
                raise BadFormatError("the column contratos should be a boolean: Check the CSV format for this program")
            
            try:
                max_unis = int(fila[5])
            except Exception as e:
                raise BadFormatError("the column contratos should be a boolean: Check the CSV format for this program")

            listaCriptomonedas.append(Criptomoneda(id_cripto, nombre, valor, precio, contratos, max_unis))
    return listaCriptomonedas

def leerUsuario(ruta = "InfoUsuarios.csv"):
    '''
    Metodo para leer el csv de los usuarios
    '''
    listaUsuarios = []

    with open(ruta, 'r') as rd:
        archivo = csv.reader(rd)

        for fila in archivo:
            try:
                id_user = int(fila[0])
            except Exception as e:
                raise BadFormatError("the column ID should be a integer: Check the CSV format for this program")
            
            try:
                nombre = str(fila[1])
            except Exception as e:
                raise BadFormatError("the column nombre should be a string: Check the CSV format for this program")
            
            try:
                apellido = str(fila[2])
            except Exception as e:
                raise BadFormatError("the column apellido should be a string: Check the CSV format for this program")
            
            try:
                NIF = str(fila[3])
            except Exception as e:
                raise BadFormatError("the column NIF should be a string: Check the CSV format for this program")
            
            try:
                nacionalidad = str(fila[4])
            except Exception as e:
                raise BadFormatError("the column nacionalidad should be a string: Check the CSV format for this program")
            
            try:
                sexo = EnumSexo.str_a_genero(fila[5])
            except Exception as e:
                raise BadFormatError("the column sexo should be a ENUM: Check the CSV format for this program")
            
            try:
                fecha_nacimiento = datetime.datetime.strptime(fila[6],'%Y/%m/%d').date()
            except Exception as e:
                raise BadFormatError("the column fecha_nacimiento should be a date: Check the CSV format for this program")
            
            try:
                fecha_registro = datetime.datetime.strptime(fila[7],'%Y/%m/%d').date()
            except Exception as e:
                raise BadFormatError("the column fecha_registro should be a date: Check the CSV format for this program")
            
            try:
                contraseña = str(fila[8])
            except Exception as e:
                raise BadFormatError("the column contraseña should be a string: Check the CSV format for this program")
             
            if (fila[9]) == "Administrador":
                try:
                    usuario = Administrador.Administrador(id_user, nombre, apellido, NIF, nacionalidad, sexo, fecha_nacimiento, fecha_registro, contraseña)
                    listaUsuarios.append(usuario)
                except Exception as e:
                    raise BadFormatError("Hubo un error en alguno de los formatos al crear un Usuario.")
          

            elif (fila[9]) == "Cliente":
                try:    
                    usuario = Cliente.Cliente(id_user, nombre, apellido, NIF, nacionalidad, sexo, fecha_nacimiento, fecha_registro, contraseña)
                    listaUsuarios.append(usuario)
                except:
                    raise BadFormatError("Hubo un error en alguno de los formatos al crear un Usuario.")
            else:
                raise BadFormatError("El tipo de usuario no se corresponde ni con un Cliente ni con un Administrador, por favor reviselo.")

            #listaUsuarios.append(Usuario.Usuario(id, str(fila[1]), str(fila[2]), str(fila[3]), str(fila[4]), EnumSexo.str_a_genero(fila[5]), datetime.datetime.strptime(fila[6],'%Y/%m/%d').date(), datetime.datetime.strptime(fila[7],'%Y/%m/%d').date()))
    return listaUsuarios

def leerCuenta(ruta):
    listaCuentas = []

    with open(ruta, 'r') as rd:
        archivo = csv.reader(rd)
        
        for fila in archivo:
            try:
                id_cuenta = int(fila[0])
            except Exception as e:
                raise BadFormatError("the column ID should be a integer: Check the CSV format for this program")
            
            try:
                id_usuario = int(fila[1])
            except Exception as e:
                raise BadFormatError("the column id_usuario should be a integer: Check the CSV format for this program")

            try:
                moneda = str(fila[2])
            except Exception as e:
                raise BadFormatError("the column moneda should be a string: Check the CSV format for this program")
            
            try:
                cantidad = float(fila[3])
            except Exception as e:
                raise BadFormatError("the column cantidad should be a float: Check the CSV format for this program")
            
            try:
                fecha_inicio = datetime.datetime.strptime(fila[4],'%Y/%m/%d').date()
            except Exception as e:
                raise BadFormatError("the column fecha_inicio should be a date: Check the CSV format for this program")
            
            
            listaCuentas.append(Cuenta.Cuenta(id_cuenta, id_usuario, moneda, cantidad, fecha_inicio))
    return listaCuentas

def leerTransaccion(ruta):
    listatransacciones = []

    with open(ruta, 'r') as rd:
        archivo = csv.reader(rd)
    
        for fila in archivo:
            try:
                id_transfer = int(fila[0])
            except Exception as e:
                raise BadFormatError("the column ID should be a integer: Check the CSV format for this program")
            
            try:
                origen = int(fila[1])
            except Exception as e:
                raise BadFormatError("the column Origen should be a integer: Check the CSV format for this program")
            
            try:
                destino = int(fila[2])
            except Exception as e:
                raise BadFormatError("the column ID should be a integer: Check the CSV format for this program")

            try:
                fecha = datetime.datetime.strptime(fila[3],'%Y/%m/%d').date()
            except Exception as e:
                raise BadFormatError("the column fecha should be a date: Check the CSV format for this program")
            
            try:
                cantidad = int(fila[4])
            except Exception as e:
                raise BadFormatError("the column cantidad should be a integer: Check the CSV format for this program")
            
            try:
                cripto = str(fila[5])
            except Exception as e:
                raise BadFormatError("the column cripto should be a string: Check the CSV format for this program")


            listatransacciones.append(Transferencias.Transferencia(id_transfer, origen, destino, fecha, cantidad, cripto))
    return listatransacciones 


            
def main():
    try:
        leer = leerCriptomoneda("InfoCriptomonedas.csv")
        print("Test Criptomonedas: ")
        #En el caso de que haya algun error no se imprime nada
        for cripto in leer:
            #print("\n", cripto)
            print("Test crear Cripto PASADO!!")
    
    except:
        FileNotFoundError("El fichero de criptomonedas no se ha encontrado.")

    try:
        leer = leerUsuario("InfoUsuarios.csv")
        print("Test Usuarios: ")
        #En el caso de que haya algun error no se imprime nada
        for usuario in leer:
            #print("\n", usuario)
            print("Test crear Usuario PASADO!!")
    
    except:
        FileNotFoundError("El fichero de Usuarios no se ha encontrado.")

    try:
        leer = leerCuenta("InfoCuentas.csv")
        print("Test Cuentas: ")
        #En el caso de que haya algun error no se imprime nada
        for cuenta in leer:
            #print("\n", cuenta)
            print("Test crear Cuenta PASADO!!")

    except:
        FileNotFoundError("El fichero de Cuentas no se ha encontrado.")
    
    try:
        leer = leerTransaccion("InfoTransfers.csv")
        print("Test Transferencias: ")
        #En el caso de que haya algun error no se imprime nada
        for trans in leer:
            #print("\n", trans)
            print("Test crear Transferencias PASADO!!")

    except:
        FileNotFoundError("El fichero de Cuentas no se ha encontrado.")



if __name__ == "__main__":
    main()