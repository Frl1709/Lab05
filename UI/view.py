import flet as ft
from model.model import Model as m



class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.btn_search = None
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None
        self.txt_corso = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        """#ROW with some controls
        # text field for the name
        self.txt_name = ft.TextField(
            label="Name",
            width=200,
            hint_text="Insert a your name"
        )

        # button for the "hello" reply
        self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)
        row1 = ft.Row([self.txt_name, self.btn_hello],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
"""
        # ROW 1
        self.txt_corso = ft.Dropdown(label="Corso", hint_text="Seleziona un corso", options=self._controller.popolateDD(), width=750)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self.btn_search = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.search_students())
        row1 = ft.Row([self.txt_corso, self.btn_search], alignment=ft.MainAxisAlignment.CENTER)

        # ROW 2
        self.txt_matricola = ft.TextField(label="Matricola")
        self.txt_nome = ft.TextField(label="Nome", read_only=True)
        self.txt_cognome = ft.TextField(label="Cognome", read_only=True)
        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)

        # ROW 3
        self.btn_students = ft.ElevatedButton(text="Cerca studente")
        self.btn_corsi = ft.ElevatedButton(text="Cerca corso")
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi")
        row3 = ft.Row([self.btn_students, self.btn_corsi, self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2, row3, self.txt_result)

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
