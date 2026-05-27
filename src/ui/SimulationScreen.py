from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QStackedWidget, QLabel


class SimulationScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.simulation_layout = QHBoxLayout()

        self.simulation_label = QLabel("Simulation Results")
        self.simulation_layout.addWidget(self.simulation_label)

        self.setLayout(self.simulation_layout)

