# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(938, 571)
        self.Play = QtWidgets.QWidget(Dialog)
        self.Play.setGeometry(QtCore.QRect(-10, 0, 951, 571))
        self.Play.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix/play_24px.png);\n"
"image: url(:/icons/pause_24px.png);\n"
"")
        self.Play.setObjectName("Play")
        self.widget_2 = QtWidgets.QWidget(self.Play)
        self.widget_2.setGeometry(QtCore.QRect(10, 0, 201, 571))
        self.widget_2.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"image: url(:/newPrefix/module_80px.png);")
        self.widget_2.setObjectName("widget_2")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 181, 121))
        self.label_7.setStyleSheet("image: url(:/newPrefix/module_8px.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(30, 40, 161, 41))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Poppins\";")
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(30, 210, 151, 21))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 127);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(40, 310, 121, 41))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Poppins\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(50, 370, 91, 81))
        self.label_10.setStyleSheet("image: url(:/newPrefix/up_down_arrow_80px.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 480, 151, 21))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 127);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(3, "")
        self.label_2 = QtWidgets.QLabel(self.Play)
        self.label_2.setGeometry(QtCore.QRect(330, 30, 401, 81))
        self.label_2.setStyleSheet("font: 87 36pt \"Poppins\";\n"
"color: rgb(0, 0, 127);\n"
"")
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.Play)
        self.progressBar.setGeometry(QtCore.QRect(230, 140, 661, 31))
        self.progressBar.setStyleSheet("\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.widget = QtWidgets.QWidget(self.Play)
        self.widget.setGeometry(QtCore.QRect(219, 239, 691, 311))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(-10, 0, 701, 361))
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgb(200, 195, 193);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.label = QtWidgets.QLabel(self.Play)
        self.label.setGeometry(QtCore.QRect(780, 60, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.Play)
        self.label_3.setGeometry(QtCore.QRect(720, 10, 181, 121))
        self.label_3.setStyleSheet("image: url(:/newPrefix/laptop_96px.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Play)
        self.label_4.setGeometry(QtCore.QRect(740, 180, 41, 31))
        self.label_4.setStyleSheet("image: url(:/newPrefix/pause_24px.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Play)
        self.label_5.setGeometry(QtCore.QRect(770, 180, 61, 31))
        self.label_5.setStyleSheet("image: url(:/newPrefix/stop_24px.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Play)
        self.label_6.setGeometry(QtCore.QRect(830, 180, 31, 31))
        self.label_6.setStyleSheet("image: url(:/newPrefix/play_30px.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "Select Algorithm"))
        self.comboBox.setItemText(0, _translate("Dialog", "Insertion Sort"))
        self.comboBox.setItemText(1, _translate("Dialog", "Merge Sort"))
        self.comboBox.setItemText(2, _translate("Dialog", "Bubble Sort"))
        self.comboBox.setItemText(3, _translate("Dialog", "Etc"))
        self.label_9.setText(_translate("Dialog", "Sort Algorithm"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Ascending Order"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Descending Order"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Etc"))
        self.label_2.setText(_translate("Dialog", "Laptop Scraper"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Description"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Rating"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Review"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Size"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Discount"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Old Price"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
