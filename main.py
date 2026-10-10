from deposito_strumenti import DepositoStrumenti
from strumenti import Strumenti
from datetime import datetime

def menu():
    print("\n--- MENU DEPOSITO STRUMENTI ---")
    print("1. Modifica nome del responsabile del deposito")
    print("2. Carica strumenti da file")
    print("3. Aggiungi un nuovo strumento (da tastiera)")
    print("4. Visualizza strumenti ordinati per marca")
    print("5. Presta uno strumento")
    print("6. Termina prestito strumento")
    print("7. Esci")
    return input("Scegli un'opzione >> ")

def main():
    deposito = DepositoStrumenti("Deposito Strumenti Civico", "Alessandro Visconti")

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_responsabile = input("Inserisci il nuovo responsabile: ")
            deposito.responsabile = nuovo_responsabile
            print(f"il nuovo responsabile del '{deposito.nome}' è {deposito.responsabile}")

        elif scelta == "2":
            while True:
                try:
                    file_path = input("Inserisci il path del file da caricare: ").strip()
                    deposito.carica_file_strumenti(file_path)
                    break
                except Exception as e:
                    print(e)

        elif scelta == "3":
            tipo = input("Tipo di strumento: ")
            marca = input("Marca: ")
            try:
                anno_acquisto = int(input("Anno di acquisto: ").strip())
                valore = float(input("Valore (euro): ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno e valore.")
                continue
            strumento = deposito.aggiungi_strumento(tipo, marca, anno_acquisto, valore)
            print('Strumento aggiunto: ')
            strumento.stampati()                                                                                        # stiamo richiamando il metodo 'stampati' di Strumenti sull'oggetto strumento
            # print(strumento)                                                                                          # sono due formule equivalenti, questa si riferisce a __str__ in strumenti.py

            #print(f"Strumento aggiunto: {strumento}")

        elif scelta == "4":
            strumenti_ordinati = deposito.strumenti_ordinati_per_marca()
            for s in strumenti_ordinati:
                print(f'- {s}')

        elif scelta == "5":
            id_strumento = input("ID strumento: ")
            codiceS = deposito.check_cod(id_strumento)                                                                  # controllo validità codice
            cognome_allievo = input("Cognome allievo: ")
            data = datetime.now().date()
            try:
                prestito = deposito.nuovo_prestito(data, codiceS, cognome_allievo)
                print(prestito)
            except Exception as e:
                print(e)

        elif scelta == "6":
            id_prestito = input("ID prestito da terminare: ")
            codiceP = deposito.check_cod(id_prestito)                                                                   # controllo validità codice
            try:
                strumento_restituito = deposito.termina_prestito(codiceP)
                print(f"Hai restituito lo strumento {strumento_restituito}")
            except Exception as e:
                print(e, '\n Si è verificato un errore, riprova')

        elif scelta == "7":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida!")

if __name__ == "__main__":
    main()
