import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *


class MyBrowser(QWidget):

    def __init__(self, parent=None):
        super(MyBrowser, self).__init__(parent)
        self.createLayout()
        self.createConnection()

    def search(self):
        address = str(self.addressBar.text())
        if address:
            if address.find("://") == -1:
                address = "://" + address
            url = QUrl(address)
            self.webView.load(url)

    def createLayout(self):
        self.setWindowTitle("jenkin's browser")

        self.addressBar = QLineEdit()
        self.goButton = QPushButton("&Go")

        b1 = QHBoxLayout()
        b1.addWidget(self.addressBar)
        b1.addWidget(self.goButton)

        self.webView = QWebView()

        layout = QVBoxLayout()
        layout.addLayout(b1)
        layout.addWidget(self.webView)

        self.setLayout(layout)

    def createConnection(self):
        self.connect(self.addressBar, SIGNAL("returnPressed"), self.search)
        self.connect(self.addressBar, SIGNAL("returnPressed"), self.addressBar, SLOT("selectAll()"))

        self.connect(self.goButton, SIGNAL("clicked()"), self.search)
        self.connect(self.goButton, SIGNAL("clicked()"), self.addressBar, SLOT("selectAll()"))


app = QApplication(sys.argv)
browser = MyBrowser()
browser.show()

sys.exit(app.exec_())