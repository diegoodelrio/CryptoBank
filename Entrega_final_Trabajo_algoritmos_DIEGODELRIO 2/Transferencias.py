try:
    import datetime
    import os.path
    import Utilidades
    import csv

except ImportError as IE:
    print(IE, "No se ha podido importar el modulo.")

class Transferencia:
    '''
    Clase que hace referencia a las Transacciones.
    '''
    IdTransferencia = 0
    def __init__(self, id_transaccion = None, origen = None, destinatario = None, fecha = None, cantidad = None, cripto = None):
        '''
        '''
        if not isinstance(id_transaccion, int):
            raise Utilidades.TransferenciaTypeError("El id a de ser un entero.")
        elif (id_transaccion <= Transferencia.IdTransferencia):
            self.__id = Transferencia.IdTransferencia + 1
            Transferencia.IdTransferencia += 1
        else:
            self.__id = id_transaccion
            Transferencia.IdTransferencia = id_transaccion

        if isinstance(origen, int):
            self.__origen = origen
        else:
            raise Utilidades.TransferenciaTypeError("El origen ha de ser un usuario existente.")
        
        if isinstance(destinatario, int):
            self.__destinatario = destinatario
        else:
            raise Utilidades.TransferenciaTypeError("El destino ha de ser un usuario existente.")
        
        if fecha == None:
            self.__fecha = datetime.date.today()
        elif isinstance(fecha, datetime.date):
            self.__fecha = fecha
        else:
            raise Utilidades.TransferenciaTypeError("FECHA NO VALIDA")

        if isinstance(cantidad, float) or isinstance(cantidad, int):
            self.__cantidad = cantidad
        else:
            raise Utilidades.TransferenciaTypeError("La cantidad ha de ser un numero decimal")
        
        if isinstance(cripto, str):
            self.__cripto = cripto
        else:
            raise Utilidades.TransferenciaTypeError("La moneda ha de ser una criptomoneda existente.")
        
    #SETTERS DE LA CLASE TRANSFERENCIA

    def set_origen(self, origen):
        if isinstance(origen, int):
            self.__origen = origen
        else:
            raise Utilidades.TransferenciaTypeError("El origen ha de ser un usuario existente.")
    
    def set_destino(self, destinatario):
        if isinstance(destinatario, int):
            self.__destinatario = destinatario
        else:
            raise Utilidades.TransferenciaTypeError("El destino ha de ser un usuario existente.")

    def set_fecha(self, fecha):
        if isinstance(fecha, datetime.date):
            self.__fecha = fecha
        else:
            raise Utilidades.TransferenciaTypeError("FECHA NO VALIDA")
    
    def set_cantidad(self, cantidad):
        if isinstance(cantidad, float) or isinstance(cantidad, int):
            self.__cantidad = cantidad
        else:
            raise Utilidades.TransferenciaTypeError("La cantidad ha de ser un numero decimal")
        
    def set_cripto(self, cripto):
        if isinstance(cripto, str):
            self.__cripto = cripto
        else:
            raise Utilidades.TransferenciaTypeError("La moneda ha de ser una criptomoneda existente.")
    
    #GETTERS DE LA CLASE TRANSFERENCIA

    def get_id(self):
        return self.__id
    
    def get_origen(self):
        return self.__origen
    
    def get_destino(self):
        return self.__destinatario
    
    def get_fecha(self):
        return self.__fecha
    
    def get_cantidad(self):
        return self.__cantidad
    
    def get_cripto(self):
        return self.__cripto

    #METODOS DE LA CLASE TRANSFERENCIA
    def guardar_transferencia(self, ruta):
        ruta.write(str(self.__id) + "," + str(self.__origen) + "," + str(self.__destinatario) + "," + str(datetime.datetime.strftime(self.__fecha, '%Y/%m/%d')) + "," + str(self.__cantidad) + "," + str(self.__cripto) + "\n")

    def __str__(self):
        return ('\nID: ' + str(self.__id) + '\n Usuario origen: ' + str(self.__origen) + '\n Usuario destino: ' + str(self.__destinatario) + '\n Criptomoneda transferida: ' + str(self.__cripto) + '\n Cantidad: ' + str(self.__cantidad) + "\n Fecha de transaccion: " + str(self.__fecha))
    
    def __repr__(self):
        return self.__str__().replace("\n","") + "\n"

def main():
    try:
        trans1 = Transferencia(1, 1, 2, datetime.datetime.strptime('2000/11/06', '%Y/%m/%d').date(), 100, "BITCOIN")
        #print(trans1)
        print("Test creacion de transferencia PASADO!!")
    
    except Exception as e:
        print("Test creacion de transferencia FAILED!!")
        print(e)
    
if __name__ == "__main__":
    main()
    



    

    