class Client:
    def __init__(self, id: int, nom: str, adreça: str, telèfon: str, correu_electrònic: str):
        self.id = id
        self.nom = nom
        self.adreça = adreça
        self.telèfon = telèfon
        self.correu_electrònic = correu_electrònic

class UsuariWeb:
    def __init__(self, id: int, inici_sessió: str, contrasenya: str, estat: str):
        self.id = id
        self.inici_sessió = inici_sessió
        self.contrasenya = contrasenya
        self.estat = estat

class CarroCompra:
    def __init__(self, id: int, id_usuari: int, data_creació: str):
        self.id = id
        self.id_usuari = id_usuari
        self.data_creació = data_creació

class Producte:
    def __init__(self, id: int, codi: str, nom: str, proveïdor: str):
        self.id = id
        self.codi = codi
        self.nom = nom
        self.proveïdor = proveïdor

class Factura:
    def __init__(self, id: int, id_usuari: int, adreça_facturació: str, data_emissió: str, data_tancament: str, pagament: str):
        self.id = id
        self.id_usuari = id_usuari
        self.adreça_facturació = adreça_facturació
        self.data_emissió = data_emissió
        self.data_tancament = data_tancament
        self.pagament = pagament

class ElementLinia:
    def __init__(self, id: int, id_producte: int, quantitat: int, preu: float):
        self.id = id
        self.id_producte = id_producte
        self.quantitat = quantitat
        self.preu = preu

class Comanda:
    def __init__(self, id: int, id_element_linia: int, data_creació: str, data_enviament: str, destinació: str, import_: float, estat: str):
        self.id = id
        self.id_element_linia = id_element_linia
        self.data_creació = data_creació
        self.data_enviament = data_enviament
        self.destinació = destinació
        self.import_ = import_
        self.estat = estat

