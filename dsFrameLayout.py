from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from maya.app.general import resourceBrowser


class FrameLayout(QtWidgets.QWidget):
    """dsFrameLayout class """
    
    def __init__(self, parent = None, title="", collapsed=True):
        super(FrameLayout, self).__init__(parent = parent)

        self._isCollapsed = collapsed
        self._titleFrame = None
        self._content = None
        self._contentLayout = None

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.addWidget(self._init_titleFrame(title, self._isCollapsed))
        self.mainLayout.addWidget(self._init_content(self._isCollapsed))
        self.mainLayout.setMargin(0)

        self._init_collapsable()

    
    def _init_titleFrame(self, title, collapsed):
        self._titleFrame = self.TitleFrame(title=title, collapsed=collapsed)

        return self._titleFrame


    def _init_content(self, collapsed):
        self._content = QtWidgets.QWidget()
        self._contentLayout = QtWidgets.QVBoxLayout()

        self._content.setLayout(self._contentLayout)
        self._content.setVisible(not collapsed)

        return self._content


    def _init_collapsable(self):
        QtCore.QObject.connect(self._titleFrame, QtCore.SIGNAL('clicked()'), self.toggleCollapsed)


    def toggleCollapsed(self):
        self._content.setVisible(self._isCollapsed)
        self._isCollapsed = not self._isCollapsed
        self._titleFrame._arrow.setArrow(int(self._isCollapsed))


    def addWidget(self, widget):
        self._contentLayout.addWidget(widget)

    def addLayout(self, layout):
        self._contentLayout.addLayout(layout)


    class TitleFrame(QtWidgets.QFrame):
        def __init__(self, parent=None, title="", collapsed=False):
            super(FrameLayout.TitleFrame, self).__init__(parent=parent)

            self.setMinimumHeight(24)
            self.move(QtCore.QPoint(24,0))
            self.setStyleSheet("border:1px solid rgb(41, 41, 41);")

            self._hlayout = QtWidgets.QHBoxLayout(self)
            self._hlayout.setContentsMargins(10, 0, 0, 0)
            self._hlayout.setSpacing(0)

            self._arrow = None
            self._title = None

            self._hlayout.addWidget(self._init_arrow(collapsed))
            self._hlayout.addWidget(self._init_title(title))

        def _init_arrow(self, collapsed):
            self._arrow = FrameLayout.Arrow(collapsed=collapsed)
            self._arrow.setStyleSheet("border:0px")

            return self._arrow

        def _init_title(self, title=None):
            self._title = QtWidgets.QLabel(title)
            self._title.setMinimumHeight(24)
            self._title.move(QtCore.QPoint(24,0))
            self._title.setStyleSheet("border:0px")

            return self._title

        def mousePressEvent(self, event):
            self.emit(QtCore.SIGNAL("clicked()"))

            return super(FrameLayout.TitleFrame, self).mousePressEvent(event)
            

    class Arrow(QtWidgets.QLabel):
        def __init__(self, parent=None, collapsed=False):
            super(FrameLayout.Arrow, self).__init__(parent=parent)

            self.setMaximumSize(18,24)

            #horizontal == 0
            self._arrowHorizontal = QtGui.QPixmap(":arrowRight.png")
            # vertical == 1
            self._arrowVertical = QtGui.QPixmap(":arrowDown.png")

            self._arrow = None
            self.setArrow(int(collapsed))

        def setArrow(self, arrowDir):
            if arrowDir:
                self._arrow = self._arrowHorizontal
            else:
                self._arrow = self._arrowVertical
            self.setPixmap(self._arrow)
            
    