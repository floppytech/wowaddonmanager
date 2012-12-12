'''
Created on 6 dec. 2012

@author: Floppy
'''

from PySide.QtCore import Slot
from PySide.QtGui import QApplication, QMainWindow, QProgressBar, QSpacerItem
from addonmodel import AddOnModel
from formsSrc.ui_mainwindow import Ui_MainWindow
from utilities import getAddOnList, checkUpdate
import os
import sys
from qcheckthread import QCheckThread

class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        Ui_MainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.progressBar = QProgressBar()
        self.progressBar.setMaximumWidth(100)
        self.statusbar.addPermanentWidget(self.progressBar)
        
        self.initData()
        
        self.connects()
        
    def connects(self):
        self.checkThread.checkComplete.connect(self.updateView)
        self.checkThread.versionChecked.connect(self.progressCheck)
#        self.actionQuit.triggered.connect(self.close)
        
    def initData(self):
        WowPath = os.path.normpath("D:\World of Warcraft")
        WowPath = os.path.join(WowPath, "Interface", "AddOns")
        
        self.addons = getAddOnList(WowPath)
        
        self.progressBar.setRange(0, len(self.addons))
        self.progressBar.setValue(0)
        self.progressBar.show()
        
        self.a = 0
        
        self.checkThread = QCheckThread(self.addons)
        self.checkThread.start()
        
        self.statusbar.showMessage("Checking for update")
        
        
    @Slot(list)
    def updateView(self, latestVersions):
        self.statusbar.showMessage("Checking complete", 30000)
        self.tableViewAddOn.setModel(AddOnModel(self.addons, latestVersions))
        self.tableViewAddOn.resizeColumnsToContents()
        self.progressBar.hide()
        self.checkThread.quit()
        
    @Slot()
    def progressCheck(self):
        self.progressBar.setValue(self.progressBar.value() + 1)
    
    @Slot()
    def closeEvent(self, *args, **kwargs):
        self.checkThread.quit()
        return QMainWindow.closeEvent(self, *args, **kwargs)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()        
    frame.show()        
    sys.exit(app.exec_())