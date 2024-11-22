from lab_1.ui.console_ui import run_console_ui

class Lab1Command:
    def execute(self):
        ui = run_console_ui()
        ui.run()