'''
Created on 6 dec. 2012

@author: Floppy
'''

from PySide.QtCore import Qt, QAbstractTableModel, QModelIndex
from CurseCSV import ClientData
from utilities import getAddOnList, checkUpdate

class AddOnModel(QAbstractTableModel):
    '''
    AddOnModel class provide the data model of addons
    '''
    
    def __init__(self, addons, latestVersions, parent=None):
        QAbstractTableModel.__init__(self, parent)        
        self.addons = addons
        self.latestVersions = latestVersions
        self.parent = parent
        
                                   
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if section == 0:
                    return "AddOn"
                elif section == 1:
                    return "Version"
                elif section == 2:
                    return "Latest version"
                else :
                    return None
            
#    def index(self, row, column, parent):
#        if self.hasIndex(row, column, parent):
#            return  self.createIndex(row, column, 0)
#        
#        return QModelIndex()
#    
#    def parent(self, index):
#        return QModelIndex()

    def rowCount(self, parent=QModelIndex()):
        return len(self.addons)

    def columnCount(self, parent=QModelIndex()):
        return 3

    def flags(self, index):        
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsDragEnabled


#    def setData(self, index, value, role=Qt.EditRole):
#        if (index.isValid() and role == Qt.EditRole):
#            pluginKey = self.addons.plugins[index.column()]
#            self.addons.moduleList[index.row()].pluginDict[pluginKey] = value
#            self.dataChanged.emit(index, index)
#            return True
#        
#        return False

    def data(self, index, role):
        if not index.isValid(): 
            return None
        
        addonName = self.addons[index.row()]
                
        if role == Qt.DisplayRole:
            if index.column() == 0:                           
                return addonName
            elif index.column() == 1:
                
                if ClientData.hasKey(addonName):
                    currentversion = ClientData.value(addonName)[0]
                else :
                    currentversion = "N/A"
                    
                return currentversion
            else :
                return self.latestVersions[index.row()]
            
#        elif role == Qt.EditRole:
#            if index.column() == 0:                           
#                return self.addons[fileId]['filename']
#            elif index.column() == 1:
#                return self.addons[fileId]['dlUrl']
#            else :
#                return self.addons[fileId]['deleteUrl']
            
            
        return None