# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class PxUILayout(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 330)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(755, 330))
        MainWindow.setMaximumSize(QtCore.QSize(755, 330))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 230, 241, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.buttonsLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.importButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.importButton.setObjectName("importButton")
        self.buttonsLayout.addWidget(self.importButton)
        self.exportButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exportButton.setObjectName("exportButton")
        self.buttonsLayout.addWidget(self.exportButton)
        self.deleteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.importButton.setObjectName("deleteButton")
        self.buttonsLayout.addWidget(self.deleteButton)
        self.fileTable = QtWidgets.QTableWidget(self.centralwidget)
        self.fileTable.setGeometry(QtCore.QRect(0, 1, 541, 221))
        self.fileTable.setObjectName("fileTable")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(550, 0, 201, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ExportTypeLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.ExportTypeLayout.setContentsMargins(0, 0, 0, 0)
        self.ExportTypeLayout.setObjectName("ExportTypeLayout")
        self.ExportTypeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ExportTypeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ExportTypeLabel.setObjectName("ExportTypeLabel")
        self.ExportTypeLayout.addWidget(self.ExportTypeLabel)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ExportTypeLayout.addWidget(self.line)
        self.ButtonsLayout = QtWidgets.QHBoxLayout()
        self.ButtonsLayout.setObjectName("ButtonsLayout")
        self.txtButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.txtButton.setChecked(True)
        self.txtButton.setObjectName("txtButton")
        self.ButtonsLayout.addWidget(self.txtButton)
        self.csvButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.csvButton.setObjectName("csvButton")
        self.ButtonsLayout.addWidget(self.csvButton)
        self.xlsxButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.xlsxButton.setObjectName("xlsxButton")
        self.ButtonsLayout.addWidget(self.xlsxButton)
        self.ExportTypeLayout.addLayout(self.ButtonsLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(550, 80, 201, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.namespaceLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.namespaceLayout.setContentsMargins(0, 0, 0, 0)
        self.namespaceLayout.setObjectName("namespaceLayout")
        self.namespaceLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.namespaceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.namespaceLabel.setObjectName("namespaceLabel")
        self.namespaceLayout.addWidget(self.namespaceLabel)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.namespaceLayout.addWidget(self.line_2)
        self.defaultButton = QtWidgets.QRadioButton(
            self.verticalLayoutWidget_2)
        self.defaultButton.setChecked(True)
        self.defaultButton.setObjectName("defaultButton")
        self.namespaceLayout.addWidget(self.defaultButton)
        self.englishButton = QtWidgets.QRadioButton(
            self.verticalLayoutWidget_2)
        self.englishButton.setObjectName("englishButton")
        self.namespaceLayout.addWidget(self.englishButton)
        self.russianButton = QtWidgets.QRadioButton(
            self.verticalLayoutWidget_2)
        self.russianButton.setObjectName("russianButton")
        self.namespaceLayout.addWidget(self.russianButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 32))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.progressBar = QtWidgets.QProgressBar(self)
        self.statusbar.addPermanentWidget(self.progressBar)
        self.progressBar.hide()
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDeleteItem = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionDeleteItem")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionDeleteItem)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PxParser"))
        self.importButton.setText(_translate("MainWindow", "Import"))
        self.exportButton.setText(_translate("MainWindow", "Export"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.ExportTypeLabel.setText(
            _translate("MainWindow", "Export file type"))
        self.txtButton.setText(_translate("MainWindow", ".txt"))
        self.csvButton.setText(_translate("MainWindow", ".csv"))
        self.xlsxButton.setText(_translate("MainWindow", ".xlsx"))
        self.namespaceLabel.setText(
            _translate("MainWindow", "Namespace locale"))
        self.defaultButton.setText(_translate("MainWindow", "Default"))
        self.englishButton.setText(_translate("MainWindow", "English"))
        self.russianButton.setText(_translate("MainWindow", "Russian"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionDeleteItem.setText(_translate("MainWindow", "Delete item"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


class UIController(QtWidgets.QMainWindow, PxUILayout):

    export_file_type = 'txt'
    file_list = set()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_actions()
        self.setup_buttons()
        self.setup_table()

    def setup_actions(self):
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Quit PxParser')
        self.actionExit.triggered.connect(self.close)

        self.actionImport.setShortcut('Ctrl+I')
        self.actionImport.setStatusTip('Import file')
        self.actionImport.triggered.connect(self.import_file)

        self.actionExport.setShortcut('Ctrl+E')
        self.actionExport.setStatusTip('Export files')
        self.actionExport.triggered.connect(self.export)

        self.actionDeleteItem.setShortcut('Del')
        self.actionDeleteItem.setStatusTip('Delete selected files')
        self.actionDeleteItem.triggered.connect(self.table_remove_selected_item)

    def setup_buttons(self):
        self.importButton.clicked.connect(self.import_file)
        self.importButton.setStatusTip('Import file')
        self.exportButton.clicked.connect(self.export)
        self.exportButton.setStatusTip('Export files')
        self.deleteButton.clicked.connect(self.table_remove_selected_item)
        self.deleteButton.setStatusTip('Delete selected files')

    def setup_table(self):
        self.fileTable.setColumnCount(1)
        header = self.fileTable.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.fileTable.setHorizontalHeaderLabels(['File path'])
    
    def table_add_item(self, item):
        rowPosition = self.fileTable.rowCount()
        self.fileTable.insertRow(rowPosition)
        self.fileTable.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(item))

    def table_remove_selected_item(self):
        items_to_remove = self.fileTable.selectedItems()
        for item in items_to_remove:
            self.file_list.remove(item.text())
            self.fileTable.removeRow(item.row())
    
    def get_file_path(self):
        return QtWidgets.QFileDialog.getOpenFileName(self, 'Select file',
                                                     '.', "Log files (*.bin *.ulg)")[0]

    def export(self):
        export_as = self.get_selected_file_type()
        self.progressBar.show()
        self.table_remove_selected_item()

    def import_file(self):
        file_path = self.get_file_path()
        if file_path not in self.file_list:
            self.table_add_item(file_path)
            self.file_list.add(file_path)


    def get_selected_file_type(self):
        if self.txtButton.isChecked():
            self.export_file_type = 'txt'
        elif self.csvButton.isChecked():
            self.export_file_type = 'csv'
        elif self.xlsxButton.isChecked():
            self.export_file_type = 'xlsx'


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UIController()
    window.statusBar().showMessage('Ready')
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
