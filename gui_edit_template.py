# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Apps\DEV\PROJECTS\KoHighlights\gui_edit_template.ui',
# licensing of 'D:\Apps\DEV\PROJECTS\KoHighlights\gui_edit_template.ui' applies.
#
# Created: Fri Oct  4 21:42:43 2024
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_EditTemplate(object):
    def setupUi(self, EditTemplate):
        EditTemplate.setObjectName("EditTemplate")
        EditTemplate.resize(500, 500)
        EditTemplate.setStyleSheet("")
        EditTemplate.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        EditTemplate.setModal(False)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(EditTemplate)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(EditTemplate)
        self.splitter.setMinimumSize(QtCore.QSize(0, 200))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.head_help_lbl = QtWidgets.QLabel(self.groupBox)
        self.head_help_lbl.setText("")
        self.head_help_lbl.setWordWrap(True)
        self.head_help_lbl.setObjectName("head_help_lbl")
        self.verticalLayout.addWidget(self.head_help_lbl)
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.head_split = QtWidgets.QSplitter(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.head_split.sizePolicy().hasHeightForWidth())
        self.head_split.setSizePolicy(sizePolicy)
        self.head_split.setOrientation(QtCore.Qt.Horizontal)
        self.head_split.setObjectName("head_split")
        self.head_edit_txt = QtWidgets.QTextEdit(self.head_split)
        self.head_edit_txt.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.head_edit_txt.setAcceptRichText(False)
        self.head_edit_txt.setObjectName("head_edit_txt")
        self.head_preview_txt = QtWidgets.QTextEdit(self.head_split)
        self.head_preview_txt.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.head_preview_txt.setReadOnly(True)
        self.head_preview_txt.setObjectName("head_preview_txt")
        self.horizontalLayout_2.addWidget(self.head_split)
        self.verticalLayout.addWidget(self.frame_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.body_help_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.body_help_lbl.setText("")
        self.body_help_lbl.setWordWrap(True)
        self.body_help_lbl.setObjectName("body_help_lbl")
        self.verticalLayout_2.addWidget(self.body_help_lbl)
        self.frame = QtWidgets.QFrame(self.groupBox_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.body_split = QtWidgets.QSplitter(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body_split.sizePolicy().hasHeightForWidth())
        self.body_split.setSizePolicy(sizePolicy)
        self.body_split.setOrientation(QtCore.Qt.Horizontal)
        self.body_split.setObjectName("body_split")
        self.body_edit_txt = QtWidgets.QTextEdit(self.body_split)
        self.body_edit_txt.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.body_edit_txt.setAcceptRichText(False)
        self.body_edit_txt.setObjectName("body_edit_txt")
        self.body_preview_txt = QtWidgets.QTextEdit(self.body_split)
        self.body_preview_txt.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.body_preview_txt.setReadOnly(True)
        self.body_preview_txt.setObjectName("body_preview_txt")
        self.horizontalLayout_3.addWidget(self.body_split)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.splitter)
        self.btn_box = QtWidgets.QFrame(EditTemplate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_box.sizePolicy().hasHeightForWidth())
        self.btn_box.setSizePolicy(sizePolicy)
        self.btn_box.setObjectName("btn_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.btn_box)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.default_btn = QtWidgets.QPushButton(self.btn_box)
        self.default_btn.setObjectName("default_btn")
        self.horizontalLayout.addWidget(self.default_btn)
        spacerItem = QtWidgets.QSpacerItem(175, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_btn = QtWidgets.QPushButton(self.btn_box)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.btn_box)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout_3.addWidget(self.btn_box)

        self.retranslateUi(EditTemplate)
        QtCore.QMetaObject.connectSlotsByName(EditTemplate)

    def retranslateUi(self, EditTemplate):
        self.groupBox.setTitle(QtWidgets.QApplication.translate("EditTemplate", "Title - Authors", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("EditTemplate", "Highlight", None, -1))
        self.default_btn.setText(QtWidgets.QApplication.translate("EditTemplate", "Default", None, -1))
        self.ok_btn.setToolTip(QtWidgets.QApplication.translate("EditTemplate", "Check online for an updated version", None, -1))
        self.ok_btn.setText(QtWidgets.QApplication.translate("EditTemplate", "OK", None, -1))
        self.cancel_btn.setText(QtWidgets.QApplication.translate("EditTemplate", "Cancel", None, -1))

import images_rc
