# 图形化界面Pyqt5-窗口及添加控件

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel, QPushButton, QFormLayout \
    , QLineEdit , QTextEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QCheckBox, QComboBox

import sys

## 类的形式
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        ## 设置窗口大小
        self.resize(300, 100)

        # ## 设置窗口位置
        # self.move(600, 300)

        ## 设置窗口标题
        self.setWindowTitle("这是一个PyQt窗体")

        # # 文本输入控件
        # f_layout = QFormLayout()
        # user_name = QLineEdit()
        # passwoed = QLineEdit()
        # passwoed.setEchoMode(QLineEdit.Password)

        # # 多行文本输入框
        # text_input = QTextEdit()

        # f_layout.addRow(QLabel("用户名"), user_name)
        # f_layout.addRow(QLabel("密码"), passwoed)

        # f_layout.addRow(text_input)
        # self.setLayout(f_layout)

        # 单选按钮
    #     h_layout = QHBoxLayout()
    #     btn1 = QRadioButton("男")
    #     btn2 = QRadioButton("女")
    #     btn3 = QRadioButton("保密")
    #     label = QLabel("请选择性别：")

    #     btn1.toggled.connect(self.btn_click)
    #     btn2.toggled.connect(self.btn_click)
    #     btn3.clicked.connect(self.btn_click)

    #     h_layout.addWidget(label)
    #     h_layout.addWidget(btn1)
    #     h_layout.addWidget(btn2)
    #     h_layout.addWidget(btn3)

    #     self.setLayout(h_layout)

    # def btn_click(self):
    #     btn = self.sender()
    #     if btn.isChecked():
    #         msg = '你选择了：' + btn.text()
    #         print(msg)

        # 复选框
        v_layout = QVBoxLayout()
        label = QLabel("请选择你喜欢的运动：")
        s1 = QCheckBox("篮球")
        s2 = QCheckBox("足球")
        s3 = QCheckBox("羽毛球")

        s1.stateChanged.connect(self.btn_check)
        s2.stateChanged.connect(self.btn_check)
        s3.stateChanged.connect(self.btn_check)

        v_layout.addWidget(label)
        v_layout.addWidget(s1)
        v_layout.addWidget(s2)
        v_layout.addWidget(s3)

        self.setLayout(v_layout)

    def btn_check(self):
        btn = self.sender()
        msg = f'你选择了：{btn.text()},状态：{btn.isChecked()}'
        print(msg)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
