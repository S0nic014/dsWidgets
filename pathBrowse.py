import logging
from PySide2 import QtWidgets
from PySide2 import QtCore


LOGGER = logging.getLogger(__name__)


class BrowsePath(QtWidgets.QWidget):
    def __init__(self,
                 parent=None,
                 mode="dir",
                 lable_text="",
                 default_path="",
                 button_text="",
                 button_icon="",
                 file_dialog_title="Select",
                 filters=""):

        super().__init__(parent)
        self.label_text = lable_text
        self.defaut_path = default_path
        self.button_icon = button_icon
        self.button_text = button_text
        self.file_dialog_title = file_dialog_title
        self.filters = filters
        self.mode = mode

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.label = QtWidgets.QLabel(self.label_text)
        self.path_line_edit = QtWidgets.QLineEdit(self.defaut_path)
        self.browse_button = QtWidgets.QPushButton(text=self.button_text)
        if self.button_icon:
            self.browse_button.setIcon(self.button_icon)

    def create_layouts(self):
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.path_line_edit)
        self.main_layout.addWidget(self.browse_button)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)

    def create_connections(self):
        if self.mode == "dir":
            self.browse_button.clicked.connect(self.get_existing_dir)
        elif self.mode == "openFile":
            self.browse_button.clicked.connect(self.get_existing_file)
        elif self.mode == "saveFile":
            self.browse_button.clicked.connect(self.get_new_file)
        else:
            LOGGER.error("Invalid browse widget mode. Should be one of: 'dir', 'openFile', 'saveFile'", exc_info=1)

    @QtCore.Slot()
    def get_existing_dir(self):
        result = QtWidgets.QFileDialog.getExistingDirectory(self, self.file_dialog_title, self.path_line_edit.text())
        if not result:
            return
        self.path_line_edit.setText(result)

    @QtCore.Slot()
    def get_existing_file(self):
        result = QtWidgets.QFileDialog.getOpenFileName(self, self.file_dialog_title, self.path_line_edit.text(), self.filters)[0]
        if not result:
            return
        self.path_line_edit.setText(result)

    @QtCore.Slot()
    def get_new_file(self):
        result = QtWidgets.QFileDialog.getSaveFileName(self, self.file_dialog_title, self.path_line_edit.text(), self.filters)[0]
        if not result:
            return
        self.path_line_edit.setText(result)

    def get_path(self) -> str:
        return self.path_line_edit.text()
