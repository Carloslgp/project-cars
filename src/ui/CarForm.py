from PySide6.QtWidgets import QWidget, QLabel, QDoubleSpinBox, QVBoxLayout

class CarForm(QWidget):
    def __init__(self, car_number):
        super().__init__()

        paragrafo = QLabel(f"Carro {car_number}")

        self.accel_spin = QDoubleSpinBox()
        self.accel_spin.setRange(0, 100)
        self.accel_spin.setSingleStep(0.5)
        self.accel_spin.setSuffix(" m/s²")

        self.vel_spin = QDoubleSpinBox()
        self.vel_spin.setRange(0, 500)
        self.vel_spin.setValue(2.0)
        self.vel_spin.setSuffix(" m/s")

        layout = QVBoxLayout()

        layout.addWidget(paragrafo)

        layout.addWidget(QLabel("Base acceleration: "))
        layout.addWidget(self.accel_spin)
        layout.addWidget(QLabel("Base velocity: "))
        layout.addWidget(self.vel_spin)

        self.setLayout(layout)

