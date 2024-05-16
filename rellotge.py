class EstatMostraHoraMinuts:
    def mostrar_hora_minuts(self):
        print("Mostra la hora i els minuts")
        return AjustarRellotge()

class AjustarRellotge:
    def __init__(self):
        self.estat = EstatAjustarHora()

class EstatAjustarHora:
    def pampallugues_hora(self):
        print("La hora fa pampallugues")
        return EstatCanviarHora()

class EstatCanviarHora:
    def canviar_hora(self):
        print("Canvia l'hora")
        return EstatAjustarMinuts()

class EstatAjustarMinuts:
    def pampallugues_minuts(self):
        print("Els minuts fa pampallugues")
        return EstatCanviarMinuts()

class EstatCanviarMinuts:
    def canviar_minuts(self):
        print("Canvia minuts")
        return None  # Regresa al estado inicial

# Prueba del funcionamiento
reloj = EstatMostraHoraMinuts()
estado_actual = reloj.mostrar_hora_minuts()
estado_actual = estado_actual.pampallugues_hora()
estado_actual = estado_actual.canviar_hora()
estado_actual = estado_actual.pampallugues_minuts()
estado_actual = estado_actual.canviar_minuts()
