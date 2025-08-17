import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtCore import QUrl, QDir

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Chemin pour stocker les données de profil (cookies, localStorage, etc.)
        profile_path = os.path.join(os.getcwd(), "Cookies")
        profile = QWebEngineProfile("PersistentProfile", self)
        profile.setPersistentStoragePath(profile_path)
        profile.setHttpCacheMaximumSize(1024 * 1024 * 100)  # 100 Mo de cache

        # Utilise ce profil pour le QWebEngineView
        self.browser = QWebEngineView()
        self.browser.setPage(QWebEngineProfile.defaultProfile().createWebEnginePage())
        self.browser.page().profile().setPersistentStoragePath(profile_path)
        self.browser.page().profile().setHttpCacheType(QWebEngineProfile.DiskHttpCache)

        self.browser.setUrl(QUrl('https://photos.google.com/login'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
