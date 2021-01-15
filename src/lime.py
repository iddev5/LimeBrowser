from PyQt5.QtCore import *;
from PyQt5.QtWidgets import *;
from PyQt5.QtGui import *;
from PyQt5.QtWebEngineWidgets import *;

from statusbar import LimeTopbar;

class LimeBrowser:
	def __init__(self, application):
		self.application = application;
		self.window = QMainWindow();
		
		self.browser = QWebEngineView();
		self.navigate_home();
	
		self.topbar = LimeTopbar(self.window, self.browser, self);
		self.topbar.add_buttons();
		self.topbar.add_urlbar();
		
		self.window.addToolBar(self.topbar.navbar);
		self.window.setCentralWidget(self.browser);
		self.window.show();

	def openfile(self):
		filename, _ = QFileDialog.getOpenFileName(self.window, "Open file", "", "Hypertext Markup Language (*.html *.htm);;All files (*.*)");

		if filename:
			with open(filename, "r") as file:
				text = file.read();

			self.browser.setHtml(text);
			self.topbar.urlbar.setText(filename);

	def savefile(self):
		filename, _ = QFileDialog.getSaveFileName(self.window, "Save Page As", "", "Hypertext MarkupLanguage (*.html *.htm);;All files (*.*)");

		if filename:
			text = self.browser.page().toHtml();
			with open(filename, "w") as file:
				file.write(text);

	def navigate_home(self):
		self.browser.setUrl(QUrl("https://duckduckgo.com"));

	def update_title(self):
		title = self.browser.page().title();
		self.window.setWindowTitle("%s - Lime Browser" % (title));


