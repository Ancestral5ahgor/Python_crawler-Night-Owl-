# 图形化界面Pyqt5-布局管理
## 水平布局、垂直布局 （ 盒子管理器 ）

from PyQt5.QtGui import QKeyEvent, QMouseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QFormLayout, QLineEdit,QLabel
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

        ## 垂直盒子
        # v_layout = QVBoxLayout()
        # ## 水平布局盒子
        # # v_layout = QHBoxLayout()
        # btn1 = QPushButton("按钮1",self)
        # btn2 = QPushButton("按钮2",self)
        # btn3 = QPushButton("按钮3",self)

        # # 按钮放入盒子
        # v_layout.addWidget(btn1)
        # v_layout.addStretch(1)
        # v_layout.addWidget(btn2)
        # v_layout.addStretch(1)
        # v_layout.addWidget(btn3)

        # self.setLayout(v_layout)

        ## 网格布局
        # grid_layout = QGridLayout()

        # btn1 = QPushButton("按钮1",self)
        # btn2 = QPushButton("按钮2",self)
        # btn3 = QPushButton("按钮3",self)
        # btn4 = QPushButton("按钮4",self)
        # btn5 = QPushButton("按钮5",self)

        # grid_layout.addWidget(btn1,0,0)
        # grid_layout.addWidget(btn2,0,1)
        # grid_layout.addWidget(btn3,0,3)
        # grid_layout.addWidget(btn4,1,0)
        # grid_layout.addWidget(btn5,1,2)

        # self.setLayout(grid_layout)

        ## 表单布局
        f_layout = QFormLayout()
        f_layout.addRow(QLabel('姓名'), QLineEdit())
        f_layout.addRow(QLabel('密码'), QLineEdit())

        h_layout = QHBoxLayout()
        btn_ok = QPushButton('确定')
        btn_cancel = QPushButton('取消')
        h_layout.addStretch(1)
        h_layout.addWidget(btn_ok)
        h_layout.addStretch(1)
        h_layout.addWidget(btn_cancel)
        h_layout.addStretch(1)
        f_layout.addRow(h_layout)

        self.setLayout(f_layout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
