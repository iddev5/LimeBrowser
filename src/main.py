import sys;
from lime import LimeBrowser;
from PyQt5.QtWidgets import QApplication;

def main():
	app = QApplication(sys.argv);
	lime = LimeBrowser(app);
	return app.exec_();

if __name__ == "__main__":
	main();
