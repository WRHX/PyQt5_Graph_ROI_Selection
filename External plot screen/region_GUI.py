'''
This script is an example for how to create an interactive plot in a GUI,
in which the user can select a region and one can retreive the boundaries he
set.
'''

import time
import sys
import os
import numpy as np
import pyqtgraph as pg

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt

#Generated python Ui files using pyuic5 -x name.ui -o name.py
from region import Ui_MainWindow
from plotDialog import Ui_Dialog

class Dialog(Ui_Dialog):
    '''
    Make a class for the dialog window to be used to plot the data.
    This class is called in the showDialog method of the MainWindow class.
    '''
    def __init__(self,dialog):
        Ui_Dialog.__init__(self)

        #set colorscheme of plotting area of GraphicsView
        #For some reason it has to be in front of setupUi
        pg.setConfigOptions(antialias = True)
        pg.setConfigOption('background', (240,240,240))
        pg.setConfigOption('foreground', (0, 0, 0))

        self.setupUi(dialog)

        #initialize the GraphicsView (promoted to plotWidget, pyqtgraph)
        self.graphicsView.enableAutoRange()
        self.region = pg.LinearRegionItem()
        self.graphicsView.setLabel('bottom', 'domain')
        self.graphicsView.setLabel('left', 'range')
        self.graphicsView.showAxis('top', True)
        self.graphicsView.showAxis('right', True)


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent = parent)
        self.setupUi(self)

        app.aboutToQuit.connect(self.closeEvent)
        self.pushButton_plotAndSelect.clicked.connect(self.button_clicked)
        self.pushButton_getValues.clicked.connect(self.getValues)

        #we will use this to hold the external plot window.
        self.plotDialog = None

    def button_clicked(self):
        '''
        1) Generates random data points array

        '''
        self.dataArray = np.random.random_integers(1,100,1000)
        self.showDialog()
        self.plotData()

    def plotData(self):
        '''
        1) clear the data currently plotted, otherwise data is appended and screen gets full.
        2) Add the region selection item, see self.region = pg.LinearRegionItem().
        3) Plot the data set created in button_clicked.
        '''
        self.plotDialog.graphicsView.clear()
        self.plotDialog.graphicsView.addItem(self.plotDialog.region)
        self.plotDialog.region.setRegion([self.dataArray[0], self.dataArray[-1]])
        self.plotDialog.graphicsView.plot(self.dataArray)

    def getValues(self):
        a,b = self.plotDialog.region.getRegion()
        print(len(self.plotDialog.region.getRegion()))
        self.textBrowser_messages.append(str(a) + '    ' + str(b))

    def showDialog(self):
        '''
        Create a Dialog class object (pop up window to display the GraphicsView).
        self.dialog is used to avoid Dialog being removed by garbage collector (it's like a global variable).
        The structure of this code is the same as the window/QMainWindow/MainWindow structure.
        '''
        self.dialog = QDialog()
        self.plotDialog = Dialog(self.dialog) # this is the object that inherits the Ui_dialog stuff
        self.dialog.show()

    def closeEvent(self):
        print('test')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


'''
text
'''
