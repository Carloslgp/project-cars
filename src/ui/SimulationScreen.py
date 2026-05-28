from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QStackedWidget, QLabel
from PySide6.QtCore import Signal

from pyvistaqt import QtInteractor
import pyvista as pv


class SimulationScreen(QWidget):
    back_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.car1 = {
            "acceleration": "",
            "velocity":  "",
            "path": ""
        }

        self.car2 = {
            "acceleration": "",
            "velocity": "",
            "path": ""
        }


        self.simulation_layout = QVBoxLayout()

        self.plotter = QtInteractor(self)
        self.simulation_layout.addWidget(self.plotter)

        self.back_button = QPushButton("Back")
        self.simulation_layout.addWidget(self.back_button)

        self.back_button.clicked.connect(self.change_to_form)


        self.setLayout(self.simulation_layout)

    def load_scene(self):
        self.plotter.clear()
        self.actors = {}  # guarda referência pra animar depois

        cars = [("car1", self.car1, 0.0), ("car2", self.car2, 3.0)]  # offset em Y

        for name, car, y_offset in cars:
            path = car.get("path")
            if not path:
                continue

            if path.lower().endswith((".glb", ".gltf")):
                # glTF não dá actor direto; carrega e move o que entrou
                before = set(self.plotter.renderer.actors.keys())
                self.plotter.import_gltf(path)
                after = set(self.plotter.renderer.actors.keys())
                for key in (after - before):
                    self.plotter.renderer.actors[key].position = (0, y_offset, 0)
            else:
                mesh = pv.read(path)
                actor = self.plotter.add_mesh(mesh, name=name)
                actor.position = (0, y_offset, 0)
                self.actors[name] = actor

        self.plotter.reset_camera()

    def change_to_form(self):
        self.back_clicked.emit()
