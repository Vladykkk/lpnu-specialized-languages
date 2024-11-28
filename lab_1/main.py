from lab_1.ui.console_ui import ui as run_ui

class Command:
    def execute(self):
        ui = run_ui()
        ui.run()