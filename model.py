from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO

        cnx = get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)  #restituisce righe come dizionari
        query = """SELECT codice, tipo, marca, anno_acquisto, valore, disponibile
                   FROM strumento"""

        result = []
        try:
            cursor.execute(query)   # per far eseguire cursore
            for row in cursor:
                # Creo l'oggetto Strumento usando i dati della riga del database
                strumento = Strumento(
                    codice=row["codice"],
                    tipo=row["tipo"],
                    marca=row["marca"],
                    anno_acquisto=row["anno_acquisto"],
                    valore=row["valore"],
                    disponibile=row["disponibile"]
                )
                result.append(strumento)

            cursor.close()   # RICORDA
            cnx.close()
            return result
        except Exception as e:
            print(f"Errore durante la lettura degli strumenti: {e}")
            cursor.close()
            cnx.close()
            return None

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO

        cnx = get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)
        # Uso istruzione parametrica: segnaposto %s
        query = """SELECT codice, tipo, marca, anno_acquisto, valore, disponibile
                   FROM strumento
                   WHERE tipo = %s"""

        result = []
        try:
            # Passo il parametro dentro una tupla come secondo argomento di execute
            cursor.execute(query, (tipo,))  # la virgola serve per dire che è una tupla, ovvero quello che si aspetta!
            for row in cursor:
                strumento = Strumento(
                    codice=row["codice"],
                    tipo=row["tipo"],
                    marca=row["marca"],
                    anno_acquisto=row["anno_acquisto"],
                    valore=row["valore"],
                    disponibile=row["disponibile"]
                )
                result.append(strumento)

            cursor.close()
            cnx.close()
            return result
        except Exception as e:
            print(f"Errore durante la ricerca degli strumenti: {e}")
            cursor.close()
            cnx.close()
            return None
