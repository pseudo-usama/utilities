import os, sys, threading
import json

from PyQt5 import QtWidgets, QtWebEngineWidgets, QtWebChannel, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QUrl, QJsonValue, QTimer


class gui:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.view = QtWebEngineWidgets.QWebEngineView()

        self.backend = Backend()
        self.channel = QtWebChannel.QWebChannel()
        self.view.page().setWebChannel(self.channel)
        self.channel.registerObject("backend", self.backend)

        # Loading HTML
        CURRNET_DIR = os.path.dirname(os.path.realpath(__file__))
        self.view.load(QUrl.fromLocalFile(f'{CURRNET_DIR}/gui/index.html'))

        # Window Properties
        self.view.resize(1000, 800)
        self.view.show()
        self.view.setWindowTitle('Player')
        self.view.showMaximized()
        # self.view.setWindowIcon(QtGui.QIcon(f'{CURRNET_DIR}/gui/assets/images/favicon.ico'))


class Backend(QObject):
    @pyqtSlot(int, result=str)
    def getRef(self, x):
        print("inside getRef", x)
        return json.dumps([{
        'title': 'Hum Pagal Nahin Hai',
        'file': 'F:/songs/Hum Pagal Nahin Hai.mp3',
        'link': 'https://www.youtube.com/watch?v=___hMJ3toxM',
        'languages': ['hindi'],
        'movie': 'Humshakals',
        'tags': ['comedy', 'hindi', 'bollywood'],
    }])

    @pyqtSlot(int)
    def printRef(self, ref):
        print("inside printRef", ref)


if __name__ == '__main__':
    window = gui()
    sys.exit(window.app.exec_())
