'''
Created on 6 dec. 2012

@author: Floppy
'''

from PySide.QtCore import QThread, Signal
from utilities import checkUpdate

class QCheckThread(QThread):
    
    versionChecked = Signal()
    checkComplete = Signal(list)

    def __init__(self, addons, parent = None):
        QThread.__init__(self)
        self.addons = addons
        self.parent = parent
        
        
    def run(self):
        latestVersions = []
        
        for addonName in self.addons:
            update, version = checkUpdate(addonName)
            latestVersions.append(version)
            self.versionChecked.emit()
            
        
        self.checkComplete.emit(latestVersions)
        
        self.exec_()
        
        