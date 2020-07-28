import logging
from PySide2 import QtWidgets
from PySide2 import QtCore


LOGGER = logging.getLogger(__name__)


class FieldSliderGroup(QtWidgets.QWidget):
    def __init__(self, parent=None,
                 data_type="int",
                 min_value=0.0,
                 max_value=1.0,
                 default_value=1.0,
                 step=1.0,
                 slider_multiplier=1.0,
                 label_text: str = ""):
        super().__init__(parent)
        # Properties
        self.data_type = data_type
        self.setMinimumSize(100, 40)

        # Build components
        self.create_widgets()
        self.create_layouts()
        self.create_connections()

        # Set values
        self.slide_multiplier = slider_multiplier
        self.label_text = label_text
        self.min_value = min_value
        self.max_value = max_value
        self.step = step

        if isinstance(default_value, str):
            if data_type == "float":
                default_value = float(default_value)
            elif data_type == "int":
                default_value = int(default_value)
        self.spin_box.setValue(default_value)

    @property
    def label_text(self):
        return self._label_text

    @label_text.setter
    def label_text(self, text):
        self._label_text = str(text)
        self.label.setText(str(text))

    @property
    def min_value(self):
        return self._min_value

    @min_value.setter
    def min_value(self, value):
        self._min_value = value
        self.spin_box.setMinimum(value)
        self.slider.setMinimum(value * self.slide_multiplier)

    @property
    def max_value(self):
        return self._max_value

    @max_value.setter
    def max_value(self, value):
        self._max_value = value
        self.spin_box.setMaximum(value)
        self.slider.setMaximum(value * self.slide_multiplier)

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value
        self.spin_box.setSingleStep(value)

    def create_widgets(self):
        if self.data_type == "float":
            self.spin_box = QtWidgets.QDoubleSpinBox()
        elif self.data_type == "int":
            self.spin_box = QtWidgets.QSpinBox()
        self.spin_box.setMinimumWidth(40)
        self.label = QtWidgets.QLabel()
        self.spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Horizontal)

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.addWidget(self.label, 0, 0)
        self.main_layout.addWidget(self.spin_box, 0, 1)
        self.main_layout.addWidget(self.slider, 0, 2)
        self.main_layout.setColumnMinimumWidth(0, 90)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)

    def create_connections(self):
        self.spin_box.valueChanged.connect(self.set_slider_value)
        self.slider.valueChanged.connect(self.set_field_value)

    @QtCore.Slot()
    def set_field_value(self, value):
        self.spin_box.setValue(value / self.slide_multiplier)

    @QtCore.Slot()
    def set_slider_value(self, value):
        self.slider.setValue(value * self.slide_multiplier)
