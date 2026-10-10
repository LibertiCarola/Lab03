from strumenti import Strumenti
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.counter = 0
        self.deposito = {}

        self.CountP = 0
        self.registro_prestiti = {}

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        path = file_path.split('\\')
        # print(path)
        nome_file = path[-1]
        file = open(f'{nome_file}', 'r')
        # rimuovere intestazione
        # file.readline()
        # lettura file
        for line in file:
            line = line.rstrip()
            riga = line.split(',') # ottengo una lista con tutte le informazioni dello strumento in ordine
                                             # codice,  tipo,    marca,  anno_acquisto, valore
            self.deposito[riga[0]] = Strumenti(riga[0], riga[1], riga[2], riga[3], riga[4])                             # stiamo salvando ciascun oggetto nel dizionario con il codice come chiave
        self.counter = len(self.deposito)
        print('file caricato correttamente')
        return self.deposito, self.counter # aggiornamento elementi globali

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        self.counter = self.counter + 1
        codice = 'S' + str(self.counter)                                                                                # deposito
        strum = Strumenti(codice, tipo, marca, anno_acquisto, valore)                                                   # [CodS][CodS, tipo, marca, anno_acquisto, valore, prestito]
        self.deposito[codice] = strum
        return strum


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""           # dep è una tupla (chiave,lista)
        codice_strumenti_ordinati = dict(sorted(self.deposito.items(), key=lambda dep: (dep[1].marca, dep[1].tipo)))                 # !!! condizioni ordinamento
        strumenti_ordinati = []
        for cod in codice_strumenti_ordinati:
            c = self.deposito[cod]
            s = (cod, c.marca, c.tipo, c.anno_acquisto, c.valore)
            strumenti_ordinati.append(s)
        return strumenti_ordinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        CodS = self.deposito[id_strumento]
        if not CodS.prestito:
        # aggiornamento counter CodP
            self.CountP = self.CountP + 1                                                                                   # registro_prestiti
            CodP = 'P' + str(self.CountP)
            prest = [CodP, data, CodS.codice, CodS.tipo, cognome_allievo]                               # [CodP][CodP, data, CodS, tipo, cognome]
            self.registro_prestiti[CodP] = prest
        # aggiornamento status strumento
            CodS.prestito = True
            print('Prestito registrato correttamente:')
            return prest
        else:
            print('Lo strumento è già stato preso in prestito')
            return None


    def termina_prestito(self, id_prestito): #id_prestito è una stringa, deve diventare una classe
        """Termina un prestito in atto"""
        if id_prestito in self.registro_prestiti:
            CodP = self.registro_prestiti[id_prestito][0] #CodP
            CodS = self.registro_prestiti[CodP][2]  # stringa di lista
            classe_strumento = self.deposito[CodS]
            classe_strumento.prestito = False
            print(f'Conclusione prestito {CodP} avenuta correttamente')
            return (CodS, classe_strumento.tipo)
        else:
            return None

