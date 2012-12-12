'''
Created on 6 mai 2011

@author: F290512
'''
import os

if __name__ == '__main__':
    
    PYSIDEPATH = os.path.normpath("C:/Python27/Lib/site-packages/PySide")
    
    uiFiles = os.listdir('./forms')
    try:
        uiFiles.remove(".svn")
    except:
        pass
    
    for uiFile in uiFiles:
        uiFile = uiFile.lower()
        pyFile = "ui_" + uiFile.split(".")[0] + ".py"
        uic = PYSIDEPATH + os.path.normpath("/scripts/uic.py")
        cmd = uic + " -o \"./formsSrc/" + pyFile + "\" -x \"./forms/" + uiFile + "\""
        cmd = os.path.normpath(cmd)
        os.system(cmd) 
        
#    PYSIDEPATHTMP = "D:/Tmp/PySide-1.0.3qt473.win32-py2.7/PURELIB/PySide"
#    rcc = PYSIDEPATHTMP + os.path.normpath("/pyside-rcc.exe")
#    rcfile = os.path.normpath("../../resources/resources.qrc")
#    pyrcfile = os.path.normpath("../" + os.path.splitext(os.path.basename(rcfile))[0] + "_rc.py")
#    cmd = rcc + " " + rcfile + " -o " + pyrcfile
#    os.system(cmd)