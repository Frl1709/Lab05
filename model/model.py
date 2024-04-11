from database import corso_DAO as c
from database import studente_DAO as s


class Model:
    def __init__(self):
        self.corsi = []
        self.studenti = []
        self.studentiIscritti = []
        self.nomeStudenteMatricola = None
        self.cognomeStudenteMatricola = None
        self.corsiIscrizione = []
        self.studenteIscritto = None
        self.corsoDiIscrizione = None

    def get_corsiM(self):
        self.corsi = c.get_corsi()
        return self.corsi

    def get_studentiM(self):
        self.studenti = s.get_studente()
        return self.studenti

    def get_studenti_iscritti(self, cod):
        self.studentiIscritti = c.get_studenti_corso(cod)
        return self.studentiIscritti

    def get_studenti_matricola(self, matricola):
        (self.nomeStudenteMatricola, self.cognomeStudenteMatricola) = s.get_studente_matricola(matricola)
        return self.nomeStudenteMatricola, self.cognomeStudenteMatricola

    def get_corsi_studente(self, matricola):
        self.corsi = s.get_corsi_iscritti(matricola)
        return self.corsi

    def iscrizione_corsi(self, matricola, codins):
        self.studenteIscritto, self.corsoDiIscrizione = c.create_iscrizione(matricola, codins)