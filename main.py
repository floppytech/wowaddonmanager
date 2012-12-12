import os
from PySide.QtCore import QThreadPool
from PySide.QtGui import QApplication
import sys
from CurseCSV import ClientData, AddOnDB
from Scrap import CurseDownloader
from runnable import QCurseRunnable
from utilities import getAddOnList, checkUpdate

__author__ = 'Floppy'

app = QApplication(sys.argv)

def quitter():
    app.exit()

WowPath = os.path.normpath("D:\World of Warcraft")
WowPath = os.path.join(WowPath, "Interface", "AddOns")

#ClientData()
#AddOnDB()
#
#print "max thread count " + str(QThreadPool.globalInstance().maxThreadCount())
#
#list = []
#
#for addon in getAddOnList(WowPath):
#    if AddOnDB().hasKey(addon):
#        if checkUpdate(addon)[0]:
#            list.append(CurseDownloader(AddOnDB().value(addon)[1]))
#
#print "queue created"
#
#for i in range(len(list[:-1])):
#    list[i].loadFinished.connect(list[i+1].load)
#
#list[-1].downloadComplete.connect(quitter)
#
#list[0].load()

#        QThreadPool.globalInstance().start(QCurseRunnable("OmniCC"))

#QThreadPool.globalInstance().start(QCurseRunnable("OmniCC"))

url = AddOnDB().value("ArkInventory")[1]
    
downloader = CurseDownloader(url)
downloader.load()

app.exec_()