import flet as ft



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.corsi = []
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.options = None

    """def handle_hello(self, e):
        Simple function to handle a button-pressed event,
        and consequently print a message on screen
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()
"""

    def popolateDD(self):
        corsi = self._model.get_corsiM()
        self.options = [ft.dropdown.Option(key=option.codCorso, text=option.__str__()) for option in corsi]
        return self.options

    def search_students(self):
        if self._view.scelta is not None:
            self._view.txt_result.clean()
            students = self._model.get_studenti_iscritti(self._view.scelta)
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(students)} iscritti"))
            for s in students:
                self._view.txt_result.controls.append(ft.Text(f"{s.__str__()}"))
                self._view.update_page()
        else:
            self._view.create_alert("Selezionare un corso")

    def search_matricola(self):
        if self._view.txt_matricola.value is not None:
            (nome, cognome) = self._model.get_studenti_matricola(self._view.txt_matricola.value)
            self._view.txt_nome.value = nome
            self._view.txt_cognome.value = cognome
            self._view.update_page()
        else:
            self._view.create_alert("Inserire una matricola")

    def search_corsi_iscrizione(self):
        self._view.txt_result.clean()
        corsi = self._model.get_corsi_studente(self._view.txt_matricola.value)
        self._view.txt_result.controls.append(ft.Text(f"Lo studente è iscritto a {len(corsi)} corsi"))
        for c in corsi:
            self._view.txt_result.controls.append(ft.Text(f"{c.__str__()}"))
            self._view.update_page()


