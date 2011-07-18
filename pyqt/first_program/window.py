#!/usr/bin/python

# icon.py

import sys
from PyQt4 import QtGui, QtCore





class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
class QuitButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('greyhoundz')
        self.setWindowIcon(QtGui.QIcon('grey.jpg'))
        
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 60, 35)

        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))



app = QtGui.QApplication(sys.argv)
qb = QuitButton()
icon = Icon()
qb.show()
icon.show()
sys.exit(app.exec_())
