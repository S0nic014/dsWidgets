import logging
from PySide2 import QtWidgets


class StatusLogger(logging.Handler):
    def __init__(self, level="DEBUG", parent=None, timeout=3000):
        super().__init__(level)
        self.widget = QtWidgets.QStatusBar(parent)
        self.timeout = timeout

    def emit(self, record: logging.LogRecord):
        msg = self.format(record)
        self.widget.showMessage(msg, self.timeout)
