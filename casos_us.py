class Caixer:
    def Identificador(self):
        # Para identificar al client
        pass

    def Canviar_Pin(self):
        # Para cambiar el PIN
        pass

    def Treure_Diners(self):
        # Para retirar diners
        pass

    def Consultar_Saldo(self):
        # Para consultar saldo
        pass

    def Consultar_ultims_moviments(self):
        # Para consultar los últims movimiment
        pass

    def Reposar_Diners(self):
        # Para reposar diners (domes para treballadors)
        pass


class Client:
    def __init__(self, caixer):
        self.caixer = caixer

    def realitzar_operacions(self):
        self.caixer.Identificador()
        self.caixer.Treure_Diners()
        self.caixer.Consultar_Saldo()
        self.caixer.Canvia_Pin()
        self.caixer.Consultar_ultims_moviments()


class Empleat:
    def __init__(self, caixer):
        self.caixer = caixer

    def realitzar_operacions(self):
        self.caixer.Identificador()
        self.caixer.Reposar_Diners()


    

    