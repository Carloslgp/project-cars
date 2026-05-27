from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QStackedWidget

from src.ui.InputScreen import InputScreen
from src.ui.SimulationScreen import SimulationScreen


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project Cars")

        self.main_layout = QVBoxLayout()

        self.stack = QStackedWidget()
        self.main_layout.addWidget(self.stack)


        self.input_screen = InputScreen()
        self.input_screen.run_clicked.connect(self.handle_run)


        self.simulation_screen = SimulationScreen()
        self.simulation_screen.back_clicked.connect(self.handle_change_to_form)


        self.stack.addWidget(self.simulation_screen)
        self.stack.addWidget(self.input_screen)

        self.stack.setCurrentWidget(self.input_screen)


        self.setLayout(self.main_layout)

    def handle_run(self, car_1_values, car_2_values):
        print(f"Recebi do carro 1: {car_1_values}")
        print(f"Recebi do carro 2: {car_2_values}")
        self.stack.setCurrentWidget(self.simulation_screen)

    def handle_change_to_form(self):
        self.stack.setCurrentWidget(self.input_screen)