class Prestito:
    contatore = 1

    def __init__(self, data, id_strumento, cognome_allievo):
        self.codice = f"P{Prestito.contatore:03d}"
        Prestito.contatore += 1
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __eq__(self, other):
        return isinstance(other, Prestito) and self.codice == other.codice

    def __str__(self):
        return f"{self.codice} | avvenuto il: {self.data} | ID strumento: {self.id_strumento} | {self.cognome_allievo}"

    def __repr__(self):
        return f"{self.codice} | avvenuto il: {self.data} | ID strumento: {self.id_strumento} | {self.cognome_allievo}"
