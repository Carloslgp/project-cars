from PySide6.QtWidgets import QWidget, QLabel, QDoubleSpinBox, QVBoxLayout, QFileDialog, QPushButton


class CarForm(QWidget):
    def __init__(self, car_number):
        super().__init__()

        self.file_path = None

        paragrafo = QLabel(f"Carro {car_number}")


        self.accel_spin = QDoubleSpinBox()
        self.accel_spin.setRange(0, 100)
        self.accel_spin.setValue(2.0)
        self.accel_spin.setSingleStep(0.5)
        self.accel_spin.setSuffix(" m/s²")

        self.vel_spin = QDoubleSpinBox()
        self.vel_spin.setRange(0, 500)
        self.vel_spin.setValue(2.0)
        self.vel_spin.setSuffix(" m/s")


        self.select_file_button = QPushButton("Select 3d file")
        self.select_file_button.clicked.connect(self.get_3dobject_path)


        layout = QVBoxLayout()

        layout.addWidget(paragrafo)

        layout.addWidget(self.select_file_button)

        layout.addWidget(QLabel("Base acceleration: "))
        layout.addWidget(self.accel_spin)
        layout.addWidget(QLabel("Base velocity: "))
        layout.addWidget(self.vel_spin)


        self.setLayout(layout)

    def get_values(self):
        return {
            "acceleration": self.accel_spin.value(),
            "velocity": self.vel_spin.value(),
            "path": self.file_path
        }
    def get_3dobject_path(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar modelo do carro",
            "",
            "Modelos 3D (*.obj *.stl *.glb *.gltf)"
        )

        if path:
            self.file_path = path




