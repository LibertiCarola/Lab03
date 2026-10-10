class Strumenti:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore
        self.prestito = False

    def stampati(self):
        print(f'{self.codice}, {self.tipo}, {self.marca}, {self.anno_acquisto}, {self.valore}')

    def __str__(self):
        return f"{self.codice}, {self.tipo}, {self.marca}, {self.anno_acquisto}, {self.valore}"