
import csv


class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return (
            f"{self.codice} - {self.tipo}, {self.marca}, "
            f"anno {self.anno_acquisto}, valore {self.valore:.2f} euro"
        )


class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return (
            f"{self.codice} - Strumento {self.id_strumento}, "
            f"allievo {self.cognome_allievo}, data {self.data}"
        )


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []
        self.prestiti = []
        self.prossimo_prestito = 1

    def carica_file_strumenti(self, file_path):
        try:
            with open(file_path, "r", newline="", encoding="utf-8") as file:
                lettore = csv.reader(file)

                for riga in lettore:
                    if len(riga) != 5:
                        print("Riga del file non valida.")
                        continue

                    codice = riga[0]
                    tipo = riga[1]
                    marca = riga[2]

                    try:
                        anno_acquisto = int(riga[3])
                        valore = float(riga[4])
                    except ValueError:
                        print("Anno o valore non validi.")
                        continue

                    gia_presente = False

                    for s in self.strumenti:
                        if s.codice == codice:
                            gia_presente = True
                            break

                    if not gia_presente:
                        strumento = Strumento(
                            codice, tipo, marca, anno_acquisto, valore
                        )
                        self.strumenti.append(strumento)

            return True

        except FileNotFoundError:
            print("Errore: file non trovato.")
            return False

        except OSError:
            print("Errore durante l'apertura del file.")
            return False

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        numero = 0

        for s in self.strumenti:
            if s.codice.startswith("S") and s.codice[1:].isdigit():
                numero_strumento = int(s.codice[1:])

                if numero_strumento > numero:
                    numero = numero_strumento

        codice = f"S{numero + 1}"

        strumento = Strumento(
            codice, tipo, marca, anno_acquisto, valore
        )

        self.strumenti.append(strumento)

        return strumento

    def strumenti_ordinati_per_marca(self):
        return sorted(
            self.strumenti,
            key=lambda s: s.marca.lower()
        )

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        strumento_esistente = False

        for s in self.strumenti:
            if s.codice == id_strumento:
                strumento_esistente = True
                break

        if not strumento_esistente:
            print("Errore: lo strumento non esiste.")
            return None

        gia_in_prestito = False

        for p in self.prestiti:
            if p.id_strumento == id_strumento:
                gia_in_prestito = True
                break

        if gia_in_prestito:
            print("Errore: lo strumento è già in prestito.")
            return None

        codice = f"P{self.prossimo_prestito}"
        self.prossimo_prestito += 1

        prestito = Prestito(
            codice, data, id_strumento, cognome_allievo
        )

        self.prestiti.append(prestito)

        return prestito

    def termina_prestito(self, id_prestito):
        for prestito in self.prestiti:
            if prestito.codice == id_prestito:
                self.prestiti.remove(prestito)
                return True

        print("Errore: il prestito non esiste.")
        return False
