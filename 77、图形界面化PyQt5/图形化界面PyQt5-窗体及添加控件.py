# 图形化界面Pyqt5-窗口及添加控件

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel, QPushButton
import sys

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
