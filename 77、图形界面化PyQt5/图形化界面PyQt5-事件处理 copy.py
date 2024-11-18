# 图形化界面Pyqt5-事件处理
## 信号（点击）与槽（事件处理者）

from PyQt5.QtGui import QKeyEvent, QMouseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel, QPushButton
import sys
from PyQt5.QtCore import Qt

## 类的形式
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        ## 设置窗口大小
        self.resize(400, 300)

        ## 设置窗口位置
        self.move(600, 300)

        ## 设置窗口标题
        self.setWindowTitle("这是一个PyQt窗体")

        # 创建标签
        self.label = QLabel(self)
        self.label.setText("这是一个标签")

        self.label.move(100, 200)

        # 创建按钮
        self.button = QPushButton(self)
        self.button.setText("按钮")
        self.button.move(250,200)

        # self.button.clicked.connect(self.btn_click)

    ## 改写鼠标事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText("鼠标左键被按下")
        elif event.button() == Qt.RightButton:
            self.label.setText("鼠标右键被按下")
        else:
            self.label.setText("鼠标未被按下")    
        # print("鼠标被按下")

    ## 鼠标释放
    def mouseReleaseEvent(self, event):
        self.label.setText("鼠标被释放")

    ## 槽函数
    # def btn_click(self):
    #     self.label.setText("按钮被点击了")

    ## 改写键盘按下及释放事件
    def keyPressEvent(self, event):
        self.label.setText("键盘被按下")

    def keyReleaseEvent(self, event):
        self.label.setText("键盘被释放")  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
