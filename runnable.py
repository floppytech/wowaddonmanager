from PySide.QtCore import QRunnable, Slot, QThread
from CurseCSV import AddOnDB
from Scrap import CurseDownloader
from utilities import checkUpdate

__author__ = 'Floppy'


class QCurseRunnable(QRunnable):
    def __init__(self, addOnName):
        QRunnable.__init__(self)
        self.addOnName = addOnName
        self.downloader = None
        self.setAutoDelete(False)

    def run(self):
        if AddOnDB().hasKey(self.addOnName):
            if checkUpdate(self.addOnName)[0]:
                print 'ok'
                self.downloader = CurseDownloader(AddOnDB().value(self.addOnName)[1])
                self.downloader.loadFinished.connect(self.download)
                self.downloader.load()

    def download(self, ok):
        self.downloader.download(ok)