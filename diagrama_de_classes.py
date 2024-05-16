class Llibres:
    def __init__(self, titol, any, categoria, autor, editorial):
        self.titol = titol
        self.any = any
        self.categoria = categoria
        self.autor = autor
        self.editorial = editorial

class Editorial:
    def __init__(self, nom, nacionalitat):
        self.nom = nom
        self.nacionalitat = nacionalitat

class Categoria:
    def __init__(self, definicio):
        self.definicio = definicio

class Autors:
    def __init__(self, nom, data_naixement):
        self.nom = nom
        self.data_naixement = data_naixement

class Copies:
    def __init__(self, codi_copia, ubicacio):
        self.codi_copia = codi_copia
        self.ubicacio = ubicacio

class Prestects:
    def __init__(self, data_inici, data_final, llibre, lector_implicat):
        self.data_inici = data_inici
        self.data_final = data_final
        self.llibre = llibre
        self.lector_implicat = lector_implicat
