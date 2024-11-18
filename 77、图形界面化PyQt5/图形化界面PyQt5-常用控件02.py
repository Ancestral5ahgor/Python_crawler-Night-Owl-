# 图形化界面Pyqt5-窗口及添加控件

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel, QPushButton, QFormLayout \
    , QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QCheckBox, QComboBox,QListWidget,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QFont
import sys

data_header = ['序号','代码','名称','价格','涨跌幅','涨跌额']
data_body = [['1','688628','优利德','35.22','0.2','5.87'],
             ['2','300845','捷安高科','24.36','0.2','4.06'],
             ['3','301289','维缆检测','51.85','0.172016','7.61'],
             ['4','300645','正元智慧','27.3','0.170167','3.97'],
             ['5','300248','新开普','11.39','0.152834','1.51'] 
            ]


## 类的形式
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        ## 设置窗口大小
        self.resize(700, 300)

        # ## 设置窗口位置
        # self.move(600, 300)

        ## 设置窗口标题
        self.setWindowTitle("这是一个PyQt窗体")

    #     layout = QFormLayout()
    #     listWight = QListWidget()
    #     listWight.addItem("编程")
    #     listWight.addItem("打游戏")
    #     listWight.addItems(['追剧','赚钱'])

    #     listWight.currentItemChanged.connect(self.list_selected)

    #     label = QLabel("请选择你喜欢的事情：")
        
    #     layout.addRow(label,listWight)

    #     self.setLayout(layout)

    # def list_selected(self,item):
    #     print(f"你选择了：{item.text()}")

    #     # 下拉列表控件
    #     layout = QFormLayout()
    #     combo_list = QComboBox()
    #     combo_list.addItem("编程")
    #     combo_list.addItem("打游戏")
    #     combo_list.addItems(['追剧','赚钱'])

    #     label = QLabel("请选择你喜欢的事情：")
    #     layout.addRow(label,combo_list)

    #     combo_list.currentIndexChanged.connect(self.combo_selected)

    #     self.setLayout(layout)

    # def combo_selected(self,idx):
    #     item = self.sender()
    #     print(f"你选择了：{item.currentText()},索引值是：{idx}")   
          
          
        # 表格控件
        layout = QVBoxLayout()
        # 创建一个对象
        table = QTableWidget()
        # 设置行数
        table.setRowCount(len(data_body))
        # 设置列数
        table.setColumnCount(len(data_header))
        # 设置字体
        table.setFont(QFont("宋体",12))
        # 设置表头
        table.setHorizontalHeaderLabels(data_header)
        # 设置表格内容
        for row in range(len(data_body)):
            for col in range(len(data_header)):
                data_item = QTableWidgetItem(data_body[row][col])
                table.setItem(row,col,data_item)

        table.itemSelectionChanged.connect(self.table_changed)

        layout.addWidget(table)
        self.setLayout(layout)

    def table_changed(self):
        table = self.sender()
        select_row = table.currentRow()
        print(f"你选择了第{select_row}行,内容是：{data_body[select_row]}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
