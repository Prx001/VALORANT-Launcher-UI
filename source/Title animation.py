import sys
from PyQt5.QtCore import QRect, QEvent, QPropertyAnimation, QParallelAnimationGroup
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QFont
from Test import Ui_Form as Widget
class Form(QMainWindow):
	def __init__(self):
		super().__init__()

		self.widget = QWidget(self)
		self.initWidget = Widget()

		self.initUI()
	def initUI(self):
		self.resize(400, 720)
		self.setFixedSize(self.size())
		self.widget.move(0, 0)
		self.initWidget.setupUi(self.widget)
		self.title_move_animation = QPropertyAnimation(self.initWidget.username_label, b"geometry")
		self.title_move_animation.setDuration(200)
		self.title_move_animation.setStartValue(self.initWidget.username_label.geometry())
		self.title_move_animation.setEndValue(QRect(62, 224, 59, 8))
		self.title_move_animation2 = QPropertyAnimation(self.initWidget.label, b"geometry")
		self.title_move_animation2.setDuration(200)
		self.title_move_animation2.setStartValue(self.initWidget.label.geometry())
		self.title_move_animation2.setEndValue(QRect(56, 288, 73, 17))
		self.size_animation = QPropertyAnimation(self.initWidget.label, b"font")
		self.size_animation.setDuration(200)
		self.size_animation.setStartValue(self.initWidget.label.font())
		self.size_animation.setEndValue(QFont("Microsoft YaHei", 5))
		self.password_animations = QParallelAnimationGroup()
		self.password_animations.addAnimation(self.title_move_animation2)
		self.password_animations.addAnimation(self.size_animation)
		self.initWidget.username_line_edit.installEventFilter(self)
		self.initWidget.password_line_edit.installEventFilter(self)
		self.show()
	def eventFilter(self, object, event):
		if object == self.initWidget.username_line_edit and event.type() == QEvent.FocusIn:
			self.title_move_animation.start()
		if object == self.initWidget.password_line_edit and event.type() == QEvent.FocusIn:
			self.password_animations.start()
		return super().eventFilter(object, event)
	# def mousePressEvent(self, event):
	# 	if self.initWidget.username_line_edit.clearFocus():
	# 		print("Focused")
	# 	return super().mousePressEvent(event)
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
