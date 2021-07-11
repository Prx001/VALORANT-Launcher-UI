import sys

from PyQt5.QtCore import Qt, QPoint, QRect, QPropertyAnimation, QBasicTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QDesktopWidget

from Widget1 import Ui_Form as Widget_1
from Widget3 import Ui_Form as Widget_2



class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.widget1 = Widget_1()
		self.widget2 = Widget_2()
		self.left = QWidget(self)
		self.left.move(0, 0)
		self.widget1.valorant_logo = QLabel(self.left)
		self.widget1.valorant_logo.setGeometry(QRect(168, -51, 66, 61))
		self.widget1.valorant_logo.setStyleSheet("border-image: url(:/widgets/widgets/VALORANT.png);")
		self.widget1.valorant_logo.setText("")
		self.valorant_logo_animation = QPropertyAnimation(self.widget1.valorant_logo, b"geometry")
		self.valorant_logo_animation.setDuration(1000)
		self.valorant_logo_animation.setStartValue(self.widget1.valorant_logo.geometry())
		self.valorant_logo_animation.setEndValue(QRect(168, 51, 66, 61))
		self.right = QWidget(self)
		self.right.move(400, 0)
		self.initUI()

	def initUI(self):
		self.resize(1280, 720)
		self.move_to_center()
		self.setFixedSize(self.size())
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.widget1.setupUi(self.left)
		self.riot_games_logo_animation = QPropertyAnimation(self.widget1.riot_games_logo, b"geometry")
		self.riot_games_logo_animation.setDuration(1000)
		self.riot_games_logo_animation.setStartValue(self.widget1.riot_games_logo.geometry())
		self.riot_games_logo_animation.setEndValue(QRect(138, -51, 126, 61))
		self.widget2.setupUi(self.right)
		self.timer = QBasicTimer()
		self.second = 0
		self.show()
		self.timer.start(1000, self)
	def timerEvent(self, time_event):
		if self.second == 2:
			self.riot_games_logo_animation.start()
		if self.second == 4:
			self.valorant_logo_animation.start()
			del self.widget1.riot_games_logo
			self.timer.stop()
		self.second += 1
		return super().timerEvent(time_event)
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
