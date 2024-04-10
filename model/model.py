from database import corso_DAO as c
from database import studente_DAO as s


class Model:
    def __init__(self):
        self.corsi = []
        self.studenti = []
        self.studentiIscritti = []

    def get_corsiM(self):
        self.corsi = c.get_corsi()
        return self.corsi

    def get_studentiM(self):
        self.studenti = s.get_studente()
        return self.studenti

    def get_studenti_iscritti(self, cod):
        self.studentiIscritti = c.get_studenti_corso(cod)
        return self.studentiIscritti
