# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphicalview.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class Ui_Dialog(object):
    def graphical():
        labels = 'Python', 'C++', 'Ruby', 'Java'
        sizes = [215, 130, 245, 210]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0.1, 0, 0, 0)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        plt.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(848, 566)
        self.lbl_module = QtWidgets.QLabel(Dialog)
        self.lbl_module.setGeometry(QtCore.QRect(490, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_module.setFont(font)
        self.lbl_module.setObjectName("lbl_module")
        self.lbl_sub = QtWidgets.QLabel(Dialog)
        self.lbl_sub.setGeometry(QtCore.QRect(270, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sub.setFont(font)
        self.lbl_sub.setObjectName("lbl_sub")
        self.lbl_qmark = QtWidgets.QLabel(Dialog)
        self.lbl_qmark.setGeometry(QtCore.QRect(620, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_qmark.setFont(font)
        self.lbl_qmark.setObjectName("lbl_qmark")
        self.combo_sem = QtWidgets.QComboBox(Dialog)
        self.combo_sem.setGeometry(QtCore.QRect(50, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sem.setFont(font)
        self.combo_sem.setObjectName("combo_sem")
        self.combo_sem.addItem("")
        self.combo_module = QtWidgets.QComboBox(Dialog)
        self.combo_module.setGeometry(QtCore.QRect(480, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_module.setFont(font)
        self.combo_module.setObjectName("combo_module")
        self.combo_module.addItem("")
        self.combo_mark = QtWidgets.QComboBox(Dialog)
        self.combo_mark.setGeometry(QtCore.QRect(610, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mark.setFont(font)
        self.combo_mark.setObjectName("combo_mark")
        self.btn_search = QtWidgets.QPushButton(Dialog)
        self.btn_search.setGeometry(QtCore.QRect(720, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.combo_sub = QtWidgets.QComboBox(Dialog)
        self.combo_sub.setGeometry(QtCore.QRect(160, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sub.setFont(font)
        self.combo_sub.setObjectName("combo_sub")
        self.lb_sem = QtWidgets.QLabel(Dialog)
        self.lb_sem.setGeometry(QtCore.QRect(50, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_sem.setFont(font)
        self.lb_sem.setObjectName("lb_sem")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_module.setText(_translate("Dialog", "Module"))
        self.lbl_sub.setText(_translate("Dialog", "Subject"))
        self.lbl_qmark.setText(_translate("Dialog", "Mark"))
        self.combo_sem.setItemText(0, _translate("Dialog", "S1"))
        self.combo_module.setItemText(0, _translate("Dialog", "Module 1"))
        self.btn_search.setText(_translate("Dialog", "Search"))
        self.lb_sem.setText(_translate("Dialog", "Semester"))


        #self.MyUI()
        sm = [1,2,3]
        fig = p.figure()

        ax = fig.add_subplot(111)
        ax.bar(range(len(sm)),sm,align='center')
        ax.set_xticks(range(len(sm)))


        canvas = FigureCanvas(fig)
        canvas.setParent(parent)
    #p.setParent(self)
        canvas.draw()
        fig.setParent(parent)
        #print "parent is ", parent, canvas.parent()

    p.show()

    def MyUI(self):

        canvas = Canvas(self, width=8, height=4)
        canvas.move(0,0)

class Canvas(FigureCanvas):
    def __init__(self, parent = None, width =5, height = 5, dpi =100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        FigureCanvas.setParent(parent)


        self.plot()

    def plot(self):
        x = np.array([50, 30, 25])

        labels = ['Apples', 'Bananas', 'Melons']
        ax = self.figure.add_subplot(111)

        ax.pie(x, labels=labels)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    #graphical()
    sys.exit(app.exec_())

