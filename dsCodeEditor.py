from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui



class LineNumberArea(QtWidgets.QWidget):
    def __init__(self, codeEditor):
        super(LineNumberArea, self).__init__(codeEditor)

        self.codeEditor = codeEditor

    
    def sizeHint(self):
        return QtCore.QSize(self.codeEditor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event)


class CodeEditor(QtWidgets.QPlainTextEdit):
    #TODO: Syntax highlighting
    
    def __init__(self, parent=None):
        super(CodeEditor, self).__init__(parent=parent)

        self.lineNumberArea = LineNumberArea(self)
        self.lineHighlighting = True


        #CONNECTIONS
        self.connect(self, QtCore.SIGNAL('blockCountChanged(int)'), self.updateLineNumberAreaWidth)
        self.connect(self, QtCore.SIGNAL('updateRequest(QRect,int)'), self.updateLineNumberArea)
        self.connect(self, QtCore.SIGNAL('cursorPositionChanged()'), self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)


    def lineNumberAreaWidth(self):
        digits = 1
        count = max(1, self.blockCount())
        while count >= 10:
            count /= 10
            digits += 1
        space = 3 + self.fontMetrics().width('9') * digits
        
        return space


    def updateLineNumberAreaWidth(self, newBlockCount):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)


    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)


    def resizeEvent(self, event):
        super(CodeEditor, self).resizeEvent(event)

        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QtCore.QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))



    def lineNumberAreaPaintEvent(self, event):
        painter = QtGui.QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), QtCore.Qt.darkGray)

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()
        
        #Font
        height = self.fontMetrics().height()
        while block.isValid() and (top <= event.rect().bottom()):
            if block.isVisible() and (bottom >= event.rect().top()):
                number = str(blockNumber+1)
                painter.setPen(QtCore.Qt.black)
                painter.drawText(0, top, self.lineNumberArea.width(), height, QtCore.Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom  = top + self.blockBoundingRect(block).height()
            blockNumber += 1


    
    def highlightCurrentLine(self):
        extraSelections = []

        if not self.isReadOnly() and self.lineHighlighting:
            selection = QtWidgets.QTextEdit.ExtraSelection()
            lineColor = QtGui.QColor(QtCore.Qt.yellow).lighter(50)

            selection.format.setBackground(lineColor)
            selection.format.setProperty(QtGui.QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)

        self.setExtraSelections(extraSelections)




    


