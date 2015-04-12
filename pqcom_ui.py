# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pqcom.ui'
#
# Created: Mon Apr 13 00:19:41 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 504)
        MainWindow.setBaseSize(QtCore.QSize(640, 504))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.recvTextEdit = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recvTextEdit.sizePolicy().hasHeightForWidth())
        self.recvTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono")
        self.recvTextEdit.setFont(font)
        self.recvTextEdit.setReadOnly(True)
        self.recvTextEdit.setObjectName("recvTextEdit")
        self.verticalLayout.addWidget(self.recvTextEdit)
        self.sendPlainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendPlainTextEdit.sizePolicy().hasHeightForWidth())
        self.sendPlainTextEdit.setSizePolicy(sizePolicy)
        self.sendPlainTextEdit.setMinimumSize(QtCore.QSize(0, 32))
        self.sendPlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 128))
        self.sendPlainTextEdit.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono")
        self.sendPlainTextEdit.setFont(font)
        self.sendPlainTextEdit.setObjectName("sendPlainTextEdit")
        self.verticalLayout.addWidget(self.sendPlainTextEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.normalRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.normalRadioButton.setChecked(True)
        self.normalRadioButton.setObjectName("normalRadioButton")
        self.horizontalLayout.addWidget(self.normalRadioButton)
        self.hexRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.hexRadioButton.setObjectName("hexRadioButton")
        self.horizontalLayout.addWidget(self.hexRadioButton)
        self.extendRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.extendRadioButton.setObjectName("extendRadioButton")
        self.horizontalLayout.addWidget(self.extendRadioButton)
        self.historyButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historyButton.sizePolicy().hasHeightForWidth())
        self.historyButton.setSizePolicy(sizePolicy)
        self.historyButton.setObjectName("historyButton")
        self.horizontalLayout.addWidget(self.historyButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.periodSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.periodSpinBox.setEnabled(True)
        self.periodSpinBox.setDecimals(3)
        self.periodSpinBox.setProperty("value", 1.0)
        self.periodSpinBox.setObjectName("periodSpinBox")
        self.horizontalLayout.addWidget(self.periodSpinBox)
        self.repeatCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.repeatCheckBox.setObjectName("repeatCheckBox")
        self.horizontalLayout.addWidget(self.repeatCheckBox)
        self.sendButton = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setMinimumSize(QtCore.QSize(64, 20))
        self.sendButton.setStyleSheet("border: 1px outset rgb(29, 153, 243);")
        self.sendButton.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.sendButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.sendButton.setAutoRaise(True)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSetup = QtGui.QAction(MainWindow)
        self.actionSetup.setObjectName("actionSetup")
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionHex = QtGui.QAction(MainWindow)
        self.actionHex.setCheckable(True)
        self.actionHex.setVisible(True)
        self.actionHex.setObjectName("actionHex")
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setCheckable(True)
        self.actionRun.setObjectName("actionRun")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionSetup)
        self.toolBar.addAction(self.actionHex)
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.sendPlainTextEdit, self.sendButton)
        MainWindow.setTabOrder(self.sendButton, self.repeatCheckBox)
        MainWindow.setTabOrder(self.repeatCheckBox, self.periodSpinBox)
        MainWindow.setTabOrder(self.periodSpinBox, self.historyButton)
        MainWindow.setTabOrder(self.historyButton, self.extendRadioButton)
        MainWindow.setTabOrder(self.extendRadioButton, self.hexRadioButton)
        MainWindow.setTabOrder(self.hexRadioButton, self.normalRadioButton)
        MainWindow.setTabOrder(self.normalRadioButton, self.recvTextEdit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pqcom", None, QtGui.QApplication.UnicodeUTF8))
        self.normalRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.hexRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Hex", None, QtGui.QApplication.UnicodeUTF8))
        self.extendRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Extend", None, QtGui.QApplication.UnicodeUTF8))
        self.historyButton.setText(QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.periodSpinBox.setSuffix(QtGui.QApplication.translate("MainWindow", "s", None, QtGui.QApplication.UnicodeUTF8))
        self.repeatCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Repeat", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("MainWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSetup.setText(QtGui.QApplication.translate("MainWindow", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setToolTip(QtGui.QApplication.translate("MainWindow", "New Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHex.setText(QtGui.QApplication.translate("MainWindow", "Hex", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHex.setToolTip(QtGui.QApplication.translate("MainWindow", "View HEX format data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setToolTip(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setToolTip(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))

