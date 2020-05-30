import maya.cmds as mc

from maya import OpenMayaUI as omui
from PySide2 import QtCore
from shiboken2 import getCppPointer


class WorkspaceControl(object):

    def __init__(self, name):
        self.name = name
        self.widget = None

    def create(self, label, widget, uiScript=None):
        mc.workspaceControl(self.name, label=label)
        if uiScript:
            mc.workspaceControl(self.name, e=1, uiScript=uiScript)

        self.addWidgetToLayout(widget)
        self.setVisible(True)

    def restore(self, widget):
        self.addWidgetToLayout(widget)

    def addWidgetToLayout(self, widget):
        if widget:
            self.widget = widget
            self.widget.setAttribute(QtCore.Qt.WA_DontCreateNativeAncestors)

        workspaceControlPtr = long(omui.MQtUtil_findControl(self.name))
        widgetPtr = long(getCppPointer(self.widget)[0])
        omui.MQtUtil_addWidgetToMayaLayout(widgetPtr, workspaceControlPtr)

    def exists(self):
        return mc.workspaceControl(self.name, q=1, ex=1)

    def isVisible(self):
        return mc.workspaceControl(self.name, q=1, visible=1)

    def setVisible(self, visible):
        if visible:
            mc.workspaceControl(self.name, e=1, restore=1)
        else:
            mc.workspaceControl(self.name, e=1, visible=False)

    def label(self):
        mc.workspaceControl(self.name, q=1, label=1)

    def setLabel(self, label):
        mc.workspaceControl(self.name, e=1, label=label)

    def isFloating(self):
        return mc.workspaceControl(self.name, q=1, floating=1)

    def isCollapsed(self):
        return mc.workspaceControl(self.name, q=1, collapse=1)

    def dockToControl(self, control, position):
        mc.workspaceControl(self.name, dtc=[control, position], e=1)

    def dockToMainWindow(self, position, tabbed=False):
        mc.workspaceControl(self.name, dtm=[position, tabbed], e=1, )

    def dockToPanel(self, control, position, tabbed=False):
        mc.workspaceControl(self.name, dtp=[control, position, tabbed], e=1)

    def tabToControl(self, control, positionIndex):
        mc.workspaceControl(self.name, tcc=[control, positionIndex], e=1)

    def setCloseCommand(self, command=None):
        mc.workspaceControl(self.name, cc=command, e=1)

    def setVisibleChangeCommand(self, command=None):
        mc.workspaceControl(self.name, vcc=command, e=1)

    def height(self):
        return mc.workspaceControl(self.name, h=1, q=1)

    def setHeight(self, value):
        mc.workspaceControl(self.name, h=value, e=1)

    def width(self):
        return mc.workspaceControl(self.name, w=1, q=1)

    def setWidth(self, value):
        mc.workspaceControl(self.name, w=value, e=1)

    def heightProperty(self):
        return mc.workspaceControl(self.name, hp=1, q=1)

    def setHeightProperty(self, hp="free"):
        mc.workspaceControl(self.name, hp=hp, e=1)

    def widthProperty(self):
        return mc.workspaceControl(self.name, wp=1, q=1)

    def setWidthProperty(self, wp="free"):
        mc.workspaceControl(self.name, wp=wp, e=1)

    def isHorizontal(self):
        return mc.workspaceControl(self.name, hr=1, q=1)

    def setHorizontal(self, value):
        mc.workspaceControl(self.name, hr=value, e=1)

    def initCallback(self):
        return mc.workspaceControl(self.name, ic=1, q=1)

    def setInitCallback(self, callback):
        return mc.workspaceControl(self.name, ic=callback, e=1)

    def isDuplicatable(self):
        return mc.workspaceControl(self.name, dup=1, q=1)

    def setDuplicatable(self, value):
        return mc.workspaceControl(self.name, dup=value, e=1)

    def setInitialHeight(self, value):
        mc.workspaceControl(self.name, ih=value, e=1)

    def setInitialWidth(self, value):
        mc.workspaceControl(self.name, iw=value, e=1)

    def resizeHeight(self, value):
        mc.workspaceControl(self.name, rsh=value, e=1)

    def resizeWidth(self, value):
        mc.workspaceControl(self.name, rsw=value, e=1)

    def tabPosition(self):
        return mc.workspaceControl(self.name, tp=1, q=1)

    def setTabPosition(self, position, changeForAll=True):
        mc.workspaceControl(self.name, tp=[position, changeForAll], e=1)

    def setRequiredPlugin(self, pluginName):
        mc.workspaceControl(self.name, rp=pluginName, e=1)

    def setRequiredControl(self, controlName):
        mc.workspaceControl(self.name, rc=controlName, e=1)
