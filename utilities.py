import csv
import os
import urllib
from BeautifulSoup import BeautifulSoup
from CurseCSV import ClientData, AddOnDB



__author__ = 'Floppy'

def getAddOnList(WowPath):
    list = [os.listdir(WowPath)[0]]
    for dirname in os.listdir(WowPath):
        if "Blizzard" not in dirname:
            if list:
                if list[-1] not in dirname:
                    list.append(dirname)
            else:
                list.append(dirname)


    #exeptions !
    if os.path.exists(os.path.join(WowPath, "sctd")):
        list.append("sctd")
    
    return list

def installAddOn(addOnName):

    url = 'http://www.curse.com/addons/wow/recount/downloads'
    opener = urllib.FancyURLopener()
    print opener.open_http(url).read()
#    remotefile = urllib.urlretrieve(url, addOnName + ".html")
#    file = urllib.urlopen(url).read()

#    print file

#    file = zipfile.ZipFile()
#    file.extractall()


def checkUpdate(addOnName):
    if not AddOnDB().hasKey(addOnName):
        print "No data for this adddon : " + addOnName
        return False, None

    if not ClientData().hasKey(addOnName):
        print "No client data for this adddon : " + addOnName
        return False, None

    url = AddOnDB().value(addOnName)[0]
    html = urllib.urlopen(url).read()

    soup = BeautifulSoup(html)

    version = soup.find('li', "newest-file").string.split(': ')[-1]

    return version != ClientData().value(addOnName)[0], version


if __name__ == "__main__":
    WowPath = os.path.normpath("D:\World of Warcraft")
    WowPath = os.path.join(WowPath, "Interface", "AddOns")

    print checkUpdate("Recount")

    print getAddOnList(WowPath)

    #installAddOn("Recount")
