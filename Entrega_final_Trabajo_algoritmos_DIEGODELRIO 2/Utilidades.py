try:
    from Generos import EnumSexo
    
except ImportError as IE:
    print(IE, "No se ha podido importar el modulo.")



def str_a_genero(item):
    '''
    Funcion que convierte una string en un genero.
    '''
    if isinstance(item, str):
        item = item.upper()
        if item == "HOMBRE" or item == "MASCULINO":
            return EnumSexo.HOMBRE
        elif item == "MUJER" or item == "FEMENINO":
            return EnumSexo.MUJER

def buscarElementoEnLista(elemento, lista_elementos):
    found = False
    for elementInList in lista_elementos:
        if(elemento == elementInList):
            found = True
            return elemento
    if not found:
        raise NotFoundException("Elemento no encontrado.")


class CriptomonedaTypeError(Exception):
    '''
    Raised when the Criptomoneda class is wrong
    '''
    pass

class UsuarioTypeError(Exception):
    """
    Raised when the Usuario class is wrong
    """
    pass

class CuentaTypeError(Exception):
    """
    Raised when the Cuenta class is wrong
    """
    pass

class NotFoundException(Exception):
    """
    Raised when the element in list cannot be found
    """
    pass

class RepitedCuenta(Exception):
    """
    Raised when the Cuenta is repited 
    """
    pass

class RepitedCripto(Exception):
    """
    Raised when the Cripto is repited 
    """
    pass

class BadFormatError(Exception):
    """
    Raised when the format is not correct. 
    """
    pass

class TransferenciaTypeError(Exception):
    """
    Raised when the Transferencia class is wrong
    """
    pass


def main():
    try:
        prueba = str_a_genero("HOMBRE")
        #print(repr(prueba))
        #print(type(prueba))
        print("Test 1 pasado!!")
    except:
        raise TypeError("Algo ha salido mal.")

    try:
        mi_lista = [1, 4, 5, 8, 2, 6, 5]
        elemento_a_buscar = 8
        elementFound = buscarElementoEnLista(elemento_a_buscar, mi_lista)
        print("Test 2 pasado!!")
    except NotFoundException:
        print("Test 2 failed!!")

    try:
        mi_lista = [1, 4, 5, 8, 2, 6, 5]
        elemento_a_buscar = 3
        elementFound = buscarElementoEnLista(elemento_a_buscar, mi_lista)
        print("Test 3 FAILED!!")
    except NotFoundException as nfe:
        print("Test 3 PASADO!!")
        #print(nfe)


if __name__ == "__main__":
    main()
