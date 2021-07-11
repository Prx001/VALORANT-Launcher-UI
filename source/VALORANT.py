import sys
from Widget1 import Ui_Form as Widget_1
from Widget2 import Ui_Form as Widget_2
from Widget3 import Ui_Form as Widget_3
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.widget1 = Widget_1()
		self.widget2 = Widget_2()
		self.widget3 = Widget_3()
		self.left_1 = QWidget(self)
		self.left_1.move(0, 0)
		self.left_2 = QWidget(self)
		self.left_2.move(0, 0)
		self.left_2.hide()
		self.right = QWidget(self)
		self.right.move(400, 0)
		self.initUI()
	def initUI(self):
		self.resize(1280, 720)
		self.move_to_center()
		self.setFixedSize(self.size())
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.widget1.setupUi(self.left_1)
		self.widget3.setupUi(self.right)
		self.show()
	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()
	def mouseMoveEvent(self, event):
		delta = QPoint(event.globalPos() - self.oldPos)
		self.move(self.x() + delta.x(), self.y() + delta.y())
		self.oldPos = event.globalPos()
	def move_to_center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())