import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO

    def handle_mostra_strumenti(self, e):
        """ Gestisce il click sul pulsante Mostra Strumenti """
        strumenti = self._model.get_strumenti() # chiamo model per prendere lista stumenti dal DB
        self._view.lista_strumenti.controls.clear()  #svuoto lista per evitare duplicati

        if strumenti is None or len(strumenti) == 0:
            self._view.show_alert("Nessuno strumento trovato nel database.")
            self._view.update()
            return

        # ciclo sugli strumenti e li aggiungo
        for s in strumenti:
            self._view.lista_strumenti.controls.append(
                ft.Text(
                    f"Codice: {s.codice} | Tipo: {s.tipo} | Marca: {s.marca} | Anno: {s.anno_acquisto} | Valore: {s.valore}€ | Disponibile: {s.disponibile}")
            )

        self._view.update()   # RICORDA DI AGGIORNARE!!!

    def handle_cerca_strumenti(self, e):
        """ Gestisce il click sul pulsante Cerca per tipo """

        # RICORDA: prima leggo il tipo digitato dall'utente
        tipo = self._view.input_tipo_strumento.value

        if not tipo:
            self._view.show_alert("Inserisci un tipo di strumento valido per la ricerca.")
            return

        strumenti = self._model.cerca_strumenti_per_tipo(tipo)
        #chiamo model ma ricorda di PASSARE IL TIPO!

        self._view.lista_strumenti_ricerca.controls.clear()

        if strumenti is None or len(strumenti) == 0:
            self._view.show_alert(f"Nessuno strumento trovato per il tipo: {tipo}")
            self._view.update()
            return

        for s in strumenti:
            self._view.lista_strumenti_ricerca.controls.append(
                ft.Text(
                    f"Codice: {s.codice} | Tipo: {s.tipo} | Marca: {s.marca} | Anno: {s.anno_acquisto} | Valore: {s.valore}€ | Disponibile: {s.disponibile}")
            )

        self._view.update()