#!/usr/bin/python

# icon.py

import sys
from PyQt4 import QtGui, QtCore




class window(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

   
			

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('greyhoundz')
        self.setWindowIcon(QtGui.QIcon('grey.jpg'))
        self.resize(250,150)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-self.width())/2, (screen.height()-self.height())/2)
        
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(0, 0, 60, 35)
        quitgeo = quit.geometry();
        quit.move((size.width()/2) - (quitgeo.width()/2), (size.height()/2) - (quitgeo.height()/2))
        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))



app = QtGui.QApplication(sys.argv)
qb = window()
qb.show()
sys.exit(app.exec_())
