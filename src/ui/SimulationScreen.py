from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QStackedWidget, QLabel
from PySide6.QtCore import Signal


class SimulationScreen(QWidget):
    back_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.simulation_layout = QHBoxLayout()

        self.simulation_label = QLabel("Simulation Results")
        self.simulation_layout.addWidget(self.simulation_label)

        self.back_button = QPushButton("Back")
        self.simulation_layout.addWidget(self.back_button)

        self.back_button.clicked.connect(self.change_to_form)

        self.setLayout(self.simulation_layout)

    def change_to_form(self):
        self.back_clicked.emit()
