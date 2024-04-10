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
        student = self._model.get_studenti_iscritti(self._view.txt_corso.value)
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(student)} iscritti"))
        for s in student:
            self._view.txt_result.controls.append(ft.Text(f"{s.__str__()}"))
            self._view.update_page()
