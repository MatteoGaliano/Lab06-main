class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore, disponibile=True):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valore = float(valore)
        self.disponibile = disponibile

    def __eq__(self, other):
        return isinstance(other, Strumento) and self.codice == other.codice

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "In prestito"
        return f"{self.codice} | {self.tipo} {self.marca} ({self.anno_acquisto}) | {self.valore:.2f}€ | {stato}"

    def __repr__(self):
        stato = "Disponibile" if self.disponibile else "In prestito"
        return f"{self.codice} | {self.tipo} {self.marca} ({self.anno_acquisto}) | {self.valore:.2f}€ | {stato}"
