from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QStackedWidget, QLabel
from PySide6.QtCore import Signal

from pyvistaqt import QtInteractor
import pyvista as pv


class SimulationScreen(QWidget):
    back_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.simulation_layout = QVBoxLayout()

        self.plotter = QtInteractor(self)
        self.simulation_layout.addWidget(self.plotter)

        self.back_button = QPushButton("Back")
        self.simulation_layout.addWidget(self.back_button)

        self.back_button.clicked.connect(self.change_to_form)

        cubo = pv.Cube()
        self.plotter.add_mesh(cubo, color="red")

        self.setLayout(self.simulation_layout)

    def change_to_form(self):
        self.back_clicked.emit()
