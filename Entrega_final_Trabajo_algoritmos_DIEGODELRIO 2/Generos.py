try:
    import enum
    
except ImportError as IE:
    print(IE, "No se ha podido importar el modulo.")
    
class EnumSexo(enum.Enum):
    '''
    Clase que indica el sexo de los usuarios.
    '''
    HOMBRE = 0
    MUJER = 1

    def __str__ (self):
        return str(self.name) + ' ' + str(self.value)
    
    @staticmethod
    def str_a_genero (cadenaInput):
        cadenaInput = cadenaInput.upper()
        if (cadenaInput == 'MASCULINO' or cadenaInput == 'HOMBRE' or cadenaInput == 'VARÓN'):
            return EnumSexo.HOMBRE
        #Falta femenino y la excepcion
        if (cadenaInput == 'FEMENINO' or cadenaInput == 'CHICA' or cadenaInput == 'MUJER'):
            return EnumSexo.MUJER

class SexoTypeError(Exception):
    "Raised when the sexo type is wron"
    pass

def main():

    print(repr(EnumSexo.HOMBRE))
    print(EnumSexo.MUJER)

if __name__ == "__main__":
    main()