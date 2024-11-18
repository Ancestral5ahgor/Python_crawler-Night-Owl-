
import requests
import os
import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 370)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        #固定行高
        # self.listWidget.setFixedHeight(250)
        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Player"))
        self.label.setText(_translate("MainWindow", "请输入要下载的音乐"))

        self.pushButton.setText(_translate("MainWindow", "搜索"))
        self.pushButton.clicked.connect(MainWindow.btn_serch)

        self.pushButton_2.setText(_translate("MainWindow", "上一页"))
        self.pushButton_2.clicked.connect(MainWindow.prev_page)

        self.pushButton_3.setText(_translate("MainWindow", "播放/暂停"))
        self.pushButton_3.clicked.connect(MainWindow.play_pause)

        self.pushButton_4.setText(_translate("MainWindow", "下一页"))
        self.pushButton_4.clicked.connect(MainWindow.next_page)

        self.pushButton_5.setText(_translate("MainWindow", "清空"))
        self.pushButton_5.clicked.connect(MainWindow.btn_clear)

        # 双击下载
        self.listWidget.itemDoubleClicked.connect(MainWindow.download)

        

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.page = 1
        self.dict = {}
        self.current_page = 0
        self.items_per_page = 10
        self.items = []
        self.media_player = QMediaPlayer()  # 初始化媒体播放器
        self.is_playing = False  # 播放状态

    def updateList(self):
        self.ui.listWidget.clear()
        start_index = self.current_page * self.items_per_page
        end_index = start_index + self.items_per_page
        # 只添加当前页需要显示的项
        self.ui.listWidget.addItems([item[0] for item in self.track_list[start_index:end_index]])

    def btn_serch(self):
        text = self.ui.lineEdit.text()
        # print("点击搜索按钮了,获取的文本是:{}".format(text))
        from get_music_info import get_music
        track_info,success_flag = get_music(text)
        if success_flag:
            # print(track_info)
            self.track_list = []  # 初始化列表
            for track in track_info:
                title = track[0]
                download_url = track[1]
                listen_url = track[2]
                display_item = f'{title}'
                # print(display_item)
                # self.dict[display_item] = download_url,listen_url
                self.track_list.append((display_item, download_url, listen_url))  # 添加元组到列表

                self.current_page = 0 
                self.updateList()
                # self.ui.listWidget.addItem(display_item)

    def download(self,item):
        key = item.text()
        filename = re.sub(r'[^\u4e00-\u9fa5]', '', key)
        # print(filename)
            # 限制文件名长度，避免过长的路径
        filename = filename[:100]
        download_url = self.dict[key]
        # print(download_url)

        msg = QMessageBox.information(self,"下载提示:",f"是否下载{key}",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if msg == QMessageBox.Yes:
            try:
                # 请求音乐内容
                # print(download_url[0])
                response = requests.get(download_url[0], stream=True)
                if response.status_code != 200:
                    raise Exception(f"下载失败，状态码：{response.status_code}")
                
                # 检查 MIME 类型
                content_type = response.headers.get('Content-Type', '')
                if 'audio/mpeg' not in content_type:
                    raise ValueError("下载的文件不是有效的音频格式")

                # music_content = requests.get(download_url[0]).content
                download_path = 'D:\\Code\\DarkCatPython\\WebCrawler\\PyQt5案例-音乐下载器\\音乐下载'
                
                if not os.path.exists(download_path):
                    os.makedirs(download_path)
                # 根据下载内容的类型设置文件扩展名（假设为 mp3）
                filename_with_extension = f"{filename}.mp3"    
                file_path = os.path.join(download_path,filename_with_extension)
                #写入文件
                with open(file_path,'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                    # f.write(music_content)
                QMessageBox.warning(self,"下载提示:",f"下载成功")
            except Exception as e:
                print(e)
                QMessageBox.warning(self,"下载提示:",f"下载失败，此链接失效，请选择其他路径")

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.updateList()            

    def play_pause(self):
        selected_item = self.ui.listWidget.currentItem()
        if selected_item is None:
            return  # 如果没有选中项，直接返回

        # 获取选中项的标题和对应的 listen_url
        selected_title = selected_item.text()
        track_info = next((track for track in self.track_list if track[0] == selected_title), None)

        if track_info is not None:
            listen_url = track_info[2]  # 获取 listen_url
            # print(listen_url)
            
            if not self.is_playing:
                # 播放音乐
                self.media_player.setMedia(QMediaContent(QUrl(listen_url)))
                self.media_player.play()
                self.is_playing = True
            else:
                # 暂停音乐
                self.media_player.pause()
                self.is_playing = False

    def next_page(self):
        if (self.current_page + 1) * self.items_per_page < len(self.track_list):
            self.current_page += 1
            self.updateList()

    def btn_clear(self):
        self.ui.listWidget.clear()
        self.ui.music_lsit = []
        self.ui.lineEdit.clear()
        # self.updateList()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    myWin = MyMainWindow()
    # myWin.setupUi(MainWindow)
    myWin.show()
    sys.exit(app.exec_())

