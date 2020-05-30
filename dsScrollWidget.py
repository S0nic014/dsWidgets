from PySide2 import QtWidgets


class ScrollWidget(QtWidgets.QWidget):
    def __init__(self, border=0, **kwargs):
        super(ScrollWidget, self).__init__(**kwargs)
        
        self.content = QtWidgets.QWidget(self)
        self.scrollArea = QtWidgets.QScrollArea()
        
        self.scrollArea.setWidget(self.content)
        self.scrollArea.setWidgetResizable(1)
        
        self.contentLayout = QtWidgets.QVBoxLayout(self.content)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.scrollArea)
        self.setContentsMargins(0 ,0 , 0, 0)
        self.layout().setSpacing(0)
        
        if not border:
            self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
            
    def resizeEvent(self, e):
        self.scrollArea.resizeEvent(e)

        