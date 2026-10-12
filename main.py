
from deposito_strumenti import DepositoStrumenti
from datetime import datetime


def menu():
    print("\n--- MENU DEPOSITO STRUMENTI ---")
    print("1. Modifica nome del responsabile del deposito")
    print("2. Carica strumenti da file")
    print("3. Aggiungi un nuovo strumento")
    print("4. Visualizza strumenti ordinati per marca")
    print("5. Presta uno strumento")
    print("6. Termina prestito strumento")
    print("7. Esci")

    return input("Scegli un'opzione >> ").strip()


def main():
    deposito = DepositoStrumenti(
        "Deposito Strumenti Civico",
        "Alessandro Visconti"
    )

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_responsabile = input(
                "Inserisci il nuovo responsabile: "
            ).strip()

            if nuovo_responsabile:
                deposito.responsabile = nuovo_responsabile
                print("Responsabile aggiornato.")
            else:
                print("Nome non valido.")

        elif scelta == "2":
            file_path = input(
                "Inserisci il percorso del file CSV: "
            ).strip()

            risultato = deposito.carica_file_strumenti(file_path)

            if risultato:
                print("Caricamento completato.")
                print("Strumenti presenti:", len(deposito.strumenti))

        elif scelta == "3":
            tipo = input("Tipo di strumento: ").strip()
            marca = input("Marca: ").strip()

            try:
                anno_acquisto = int(input("Anno di acquisto: ").strip())
                valore = float(input("Valore in euro: ").strip())
            except ValueError:
                print("Inserisci un anno e un valore validi.")
                continue

            if not tipo or not marca or anno_acquisto <= 0 or valore < 0:
                print("Dati non validi.")
                continue

            strumento = deposito.aggiungi_strumento(
                tipo, marca, anno_acquisto, valore
            )

            print("Strumento aggiunto:", strumento)

        elif scelta == "4":
            strumenti = deposito.strumenti_ordinati_per_marca()

            if len(strumenti) == 0:
                print("Non ci sono strumenti nel deposito.")
            else:
                for strumento in strumenti:
                    print(strumento)

        elif scelta == "5":
            id_strumento = input("ID dello strumento: ").strip()
            cognome_allievo = input("Cognome dell'allievo: ").strip()

            if not cognome_allievo:
                print("Cognome non valido.")
                continue

            data = datetime.now().date()

            prestito = deposito.nuovo_prestito(
                data, id_strumento, cognome_allievo
            )

            if prestito is not None:
                print("Prestito registrato:", prestito)

        elif scelta == "6":
            id_prestito = input(
                "ID del prestito da terminare: "
            ).strip()

            risultato = deposito.termina_prestito(id_prestito)

            if risultato:
                print("Prestito terminato con successo.")

        elif scelta == "7":
            print("Uscita dal programma.")
            break

        else:
            print("Opzione non valida.")


if __name__ == "__main__":
    main()
