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
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from region import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent = parent)


        pg.setConfigOptions(antialias = True)
        pg.setConfigOption('background', (240,240,240))
        pg.setConfigOption('foreground', (0, 0, 0))

        self.setupUi(self)
        app.aboutToQuit.connect(self.closeEvent)
        self.pushButton_plotAndSelect.clicked.connect(self.button_clicked)
        self.pushButton_getValues.clicked.connect(self.getValues)


        #initialize plot
        self.plot.enableAutoRange()
        self.region = pg.LinearRegionItem()
        self.plot.setLabel('bottom', 'domain')
        self.plot.setLabel('left', 'range')
        self.plot.showAxis('top', True)
        self.plot.showAxis('right', True)


    def plotData(self):
        '''
        1) clear the data currently plotted, otherwise data is appended and screen gets full.
        2) Add the region selection item, see self.region = pg.LinearRegionItem().
        3) Plot the data set created in button_clicked.
        '''
        self.plot.clear()
        self.plot.addItem(self.region)
        self.region.setRegion([self.dataArray[0], self.dataArray[-1]])
        self.plot.plot(self.dataArray)

    def button_clicked(self):
        '''
        1) Generates random data points array

        '''
        self.dataArray = np.random.random_integers(1,100,1000)
        self.plotData()

    def getValues(self):
        a,b = self.region.getRegion()
        print(len(self.region.getRegion()))
        self.textBrowser_messages.append(str(a) + '    ' + str(b))

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
