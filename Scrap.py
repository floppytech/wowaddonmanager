from CurseCSV import AddOnDB
from PySide.QtCore import QUrl, Slot, Signal
from PySide.QtWebKit import QWebPage
import os
import urllib
import zipfile



__author__ = 'Floppy'

class CurseDownloader(QWebPage):

    downloadComplete = Signal()

    def __init__(self, url, parent=None):
        QWebPage.__init__(self, parent)
        self.loadFinished.connect(self.download)
        self.urlDL = url
        #self.mainFrame().load(QUrl(url))
        self.complete = False

    @Slot(bool)
    def download(self, ok):
        if ok:
            html = self.mainFrame().toHtml()
            try:
                html = str(html.encode("latin-1"))
            except UnicodeEncodeError:
                html = str(html.encode("UTF-8"))

            start = html.find("data-href")
            end = html.find('class="download-link"')

            self.url = html[start:end].replace("data-href=", "").replace('"', "")

            filename = self.url.split("/")[-1]
            urlopener = urllib.URLopener()
            print "Downloading " + filename + "..."
            urlopener.retrieve(self.url, filename)

            zipFile = zipfile.ZipFile(filename)
            zipFile.extractall("Interface/Addons/")
            zipFile.close()

            os.unlink(filename)

            self.downloadComplete.emit()

            self.complete = True

            print "download complete"

    @Slot()
    def load(self):
        self.mainFrame().load(QUrl(self.urlDL))
