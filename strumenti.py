class Strumenti:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore
        self.prestito = False

    def stampati(self, s):
        print(f'{s.codice}, {s.tipo}, {s.marca}, {s.anno_acquisto}, {s.valore}')