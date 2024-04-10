from dataclasses import *


@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    corsoDiStudio: str

    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"


