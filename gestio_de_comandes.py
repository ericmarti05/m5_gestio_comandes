class Client:
    def __init__(self, id, nom, adreça, telefon, email):
        self.id = id
        self.nom = nom
        self.adreça = adreça
        self.phone = telefon 
        self.email = email

    def usuari(self, login, password, estat):
        return usuari_web(login, password, estat)


class usuari_web:
    def __init__(self, id, login, password, estat):
        self.id = id
        self.login = login
        self.password = password
        self.estat = estat

    def set_estat(self, estat):
        self.estat = estat


class Producte:
    def __init__(self, id, codi, nom, proveidor):
        self.id = id
        self.codi = codi
        self.nom = nom
        self.proveidor = proveidor


class carro:
    def __init__(self, id, customer_id, estat):
        self.id = id
        self.customer_id = customer_id
        self.estat = estat


class factura:
    def __init__(self, id, customer_id, estat):
        self.id = id
        self.customer_id = customer_id
        self.estat = estat


class linia_comanda:
    def __init__(self, id, factura_id, producte_id, quantitat, preu):
        self.id = id
        self.factura_id = factura_id
        self.producte_id = producte_id
        self.quantitat = quantitat
        self.preu = preu


class ordre_enviament:
    def __init__(self, id, factura_id, estat):
        self.id = id
        self.factura_id = factura_id
        self.estat = estat


class ordre:
    def __init__(self, id, ordre_id, producte_id, quantitat):
        self.id = id
        self.ordre_id = ordre_id
        self.producte_id = producte_id
        self.quantitat = quantitat
