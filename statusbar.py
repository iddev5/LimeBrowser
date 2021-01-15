import os;
from PyQt5.QtCore import *;
from PyQt5.QtWidgets import *;
from PyQt5.QtGui import *;
from PyQt5.QtWebEngineWidgets import *;

import resources;

class LimeTopbar:
	def __init__(self, window, browser, engine):
		self.window = window;
		self.browser = browser;
		self.engine = engine;

		self.navbar = QToolBar("Navigation");
		self.navbar.setIconSize(QSize(16, 16));
		self.navbar.setMovable(False);

	def add_buttons(self):
		self.back = QAction(QIcon(":/icons/arrow-left"), "Back", self.window);
		self.back.setStatusTip("Back to previous page");
		self.back.triggered.connect(self.browser.back);
		self.navbar.addAction(self.back);

		self.forw = QAction(QIcon(":/icons/arrow-right"), "Forward", self.window);
		self.forw.setStatusTip("Forward to next page");
		self.forw.triggered.connect(self.browser.forward);
		self.navbar.addAction(self.forw);

		self.reload = QAction(QIcon(":/icons/reload"), "Reload", self.window);
		self.reload.setStatusTip("Reload page");
		self.reload.triggered.connect(self.browser.reload);
		self.navbar.addAction(self.reload);

	def add_urlbar(self):
		self.urlbar = QLineEdit();
		self.urlbar.returnPressed.connect(self.navigate_url);
		self.navbar.addWidget(self.urlbar);

		self.browser.urlChanged.connect(self.update_urlbar);
		self.browser.loadStarted.connect(self.load_started);
		self.browser.loadFinished.connect(self.load_finished);

		self.menu = QAction(QIcon(":/icons/stop"), "Menu", self.window);
		self.menu.setStatusTip("Menu");
		self.menu.triggered.connect(self.menubar);
		self.navbar.addAction(self.menu);

	def menubar(self):
		self.menuopt = QMenu(self.navbar);
		self.menuopt.addAction(self.back);
		self.menuopt.addAction(self.forw);
		self.menuopt.addAction(self.reload);

		self.menuopt.addSeparator();

		self.openfile = QAction("Open file");
		self.openfile.setStatusTip("Open from file");
		self.openfile.triggered.connect(self.engine.openfile);
		self.menuopt.addAction(self.openfile);

		self.savefile = QAction("Save file");
		self.savefile.setStatusTip("Save Page to file");
		self.savefile.triggered.connect(self.engine.savefile);
		self.menuopt.addAction(self.savefile);

		self.menuopt.exec_(QCursor.pos());

	def load_started(self):
		self.reload.setIcon(QIcon(":/icons/stop"));
		self.reload.triggered.connect(self.browser.stop);
		self.reload.setStatusTip("Stop loading the page");

	def load_finished(self):
		self.reload.setIcon(QIcon(":/icons/reload.png"));
		self.reload.triggered.connect(self.browser.reload);
		self.reload.setStatusTip("Reload page");
		self.engine.update_title();

	def navigate_url(self):
		q = QUrl("https://duckduckgo.com/?q=" + self.urlbar.text().replace(" ", "+"));
		self.browser.setUrl(q);

	def update_urlbar(self, q):
		self.urlbar.setText(q.toString());
		self.urlbar.setCursorPosition(0);


