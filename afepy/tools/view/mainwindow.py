# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Oct 11 18:32:32 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(698, 538)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Objects = QtGui.QMenu(self.menubar)
        self.menu_Objects.setTitle(QtGui.QApplication.translate("MainWindow", "&Misc objects", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Objects.setObjectName(_fromUtf8("menu_Objects"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        self.menu_Platonic_solids_2 = QtGui.QMenu(self.menubar)
        self.menu_Platonic_solids_2.setTitle(QtGui.QApplication.translate("MainWindow", "&Platonic solids", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Platonic_solids_2.setObjectName(_fromUtf8("menu_Platonic_solids_2"))
        self.menu_Geodesic_domes_2 = QtGui.QMenu(self.menubar)
        self.menu_Geodesic_domes_2.setTitle(QtGui.QApplication.translate("MainWindow", "&Geodesic domes", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Geodesic_domes_2.setObjectName(_fromUtf8("menu_Geodesic_domes_2"))
        self.menu_Rendering = QtGui.QMenu(self.menubar)
        self.menu_Rendering.setTitle(QtGui.QApplication.translate("MainWindow", "&Rendering", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Rendering.setObjectName(_fromUtf8("menu_Rendering"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setToolTip(QtGui.QApplication.translate("MainWindow", "Display the application about box", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setToolTip(QtGui.QApplication.translate("MainWindow", "Quit the application", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.actionFrom_Icosahedron_2 = QtGui.QAction(MainWindow)
        self.actionFrom_Icosahedron_2.setText(QtGui.QApplication.translate("MainWindow", "from &Icosahedron(2)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrom_Icosahedron_2.setToolTip(QtGui.QApplication.translate("MainWindow", "from Icosahedron(2)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrom_Icosahedron_2.setObjectName(_fromUtf8("actionFrom_Icosahedron_2"))
        self.action_Icosahedron = QtGui.QAction(MainWindow)
        self.action_Icosahedron.setText(QtGui.QApplication.translate("MainWindow", "&Icosahedron", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Icosahedron.setObjectName(_fromUtf8("action_Icosahedron"))
        self.action_Tetrahedron = QtGui.QAction(MainWindow)
        self.action_Tetrahedron.setText(QtGui.QApplication.translate("MainWindow", "&Tetrahedron", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Tetrahedron.setObjectName(_fromUtf8("action_Tetrahedron"))
        self.action_Cube = QtGui.QAction(MainWindow)
        self.action_Cube.setText(QtGui.QApplication.translate("MainWindow", "&Cube", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cube.setObjectName(_fromUtf8("action_Cube"))
        self.action_CubeQuad = QtGui.QAction(MainWindow)
        self.action_CubeQuad.setText(QtGui.QApplication.translate("MainWindow", "&CubeQuad", None, QtGui.QApplication.UnicodeUTF8))
        self.action_CubeQuad.setObjectName(_fromUtf8("action_CubeQuad"))
        self.action_Lot_of_Tetras = QtGui.QAction(MainWindow)
        self.action_Lot_of_Tetras.setText(QtGui.QApplication.translate("MainWindow", "&Lot of Tetras", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Lot_of_Tetras.setObjectName(_fromUtf8("action_Lot_of_Tetras"))
        self.action_Torus = QtGui.QAction(MainWindow)
        self.action_Torus.setText(QtGui.QApplication.translate("MainWindow", "&Torus", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Torus.setObjectName(_fromUtf8("action_Torus"))
        self.action_Torus2 = QtGui.QAction(MainWindow)
        self.action_Torus2.setText(QtGui.QApplication.translate("MainWindow", "&Torus2", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Torus2.setObjectName(_fromUtf8("action_Torus2"))
        self.action_Dodecahedron = QtGui.QAction(MainWindow)
        self.action_Dodecahedron.setText(QtGui.QApplication.translate("MainWindow", "&Dodecahedron", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Dodecahedron.setObjectName(_fromUtf8("action_Dodecahedron"))
        self.actionFrom_Icosahedron_4 = QtGui.QAction(MainWindow)
        self.actionFrom_Icosahedron_4.setText(QtGui.QApplication.translate("MainWindow", "from I&cosahedron(4)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrom_Icosahedron_4.setToolTip(QtGui.QApplication.translate("MainWindow", "from Icosahedron(4)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrom_Icosahedron_4.setObjectName(_fromUtf8("actionFrom_Icosahedron_4"))
        self.action_Sphere = QtGui.QAction(MainWindow)
        self.action_Sphere.setText(QtGui.QApplication.translate("MainWindow", "&Sphere", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Sphere.setObjectName(_fromUtf8("action_Sphere"))
        self.actionFrom_Tetrahedron_2 = QtGui.QAction(MainWindow)
        self.actionFrom_Tetrahedron_2.setText(QtGui.QApplication.translate("MainWindow", "from &Tetrahedron(2)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrom_Tetrahedron_2.setObjectName(_fromUtf8("actionFrom_Tetrahedron_2"))
        self.actionFrom_Tetrahedron_4 = QtGui.QAction(MainWindow)
        self.actionFrom_Tetrahedron_4.setText(QtGui.QApplication.translate("MainWindow", "from T&etrahedron(4)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrom_Tetrahedron_4.setObjectName(_fromUtf8("actionFrom_Tetrahedron_4"))
        self.action_Octahedron = QtGui.QAction(MainWindow)
        self.action_Octahedron.setText(QtGui.QApplication.translate("MainWindow", "&Octahedron", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Octahedron.setObjectName(_fromUtf8("action_Octahedron"))
        self.actionFrom_Octahedron_2 = QtGui.QAction(MainWindow)
        self.actionFrom_Octahedron_2.setText(QtGui.QApplication.translate("MainWindow", "from &Octahedron(2)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrom_Octahedron_2.setObjectName(_fromUtf8("actionFrom_Octahedron_2"))
        self.actionFrom_Octahedron_4 = QtGui.QAction(MainWindow)
        self.actionFrom_Octahedron_4.setText(QtGui.QApplication.translate("MainWindow", "from O&ctahedron(4)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrom_Octahedron_4.setToolTip(QtGui.QApplication.translate("MainWindow", "from Octahedron(4)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrom_Octahedron_4.setObjectName(_fromUtf8("actionFrom_Octahedron_4"))
        self.actionTruncated_Icosahedron = QtGui.QAction(MainWindow)
        self.actionTruncated_Icosahedron.setText(QtGui.QApplication.translate("MainWindow", "Truncated Icosahedron (soccer &ball)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTruncated_Icosahedron.setObjectName(_fromUtf8("actionTruncated_Icosahedron"))
        self.actionDisplay_edges = QtGui.QAction(MainWindow)
        self.actionDisplay_edges.setCheckable(True)
        self.actionDisplay_edges.setText(QtGui.QApplication.translate("MainWindow", "Display &edges", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisplay_edges.setShortcut(QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisplay_edges.setObjectName(_fromUtf8("actionDisplay_edges"))
        self.action_Color_mode = QtGui.QAction(MainWindow)
        self.action_Color_mode.setText(QtGui.QApplication.translate("MainWindow", "&Color mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Color_mode.setShortcut(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Color_mode.setObjectName(_fromUtf8("action_Color_mode"))
        self.actionZoom_In = QtGui.QAction(MainWindow)
        self.actionZoom_In.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setShortcut(QtGui.QApplication.translate("MainWindow", "PgUp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setObjectName(_fromUtf8("actionZoom_In"))
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        self.actionZoom_Out.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_Out.setShortcut(QtGui.QApplication.translate("MainWindow", "PgDown", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_Out.setObjectName(_fromUtf8("actionZoom_Out"))
        self.actionInteractive = QtGui.QAction(MainWindow)
        self.actionInteractive.setCheckable(True)
        self.actionInteractive.setText(QtGui.QApplication.translate("MainWindow", "Interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInteractive.setShortcut(QtGui.QApplication.translate("MainWindow", "Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInteractive.setObjectName(_fromUtf8("actionInteractive"))
        self.menu_File.addAction(self.action_Quit)
        self.menu_Objects.addAction(self.action_Sphere)
        self.menu_Objects.addAction(self.action_Lot_of_Tetras)
        self.menu_Objects.addAction(self.action_Torus)
        self.menu_Objects.addAction(self.action_Torus2)
        self.menu_Objects.addAction(self.actionTruncated_Icosahedron)
        self.menu_Help.addAction(self.action_About)
        self.menu_Platonic_solids_2.addAction(self.action_Tetrahedron)
        self.menu_Platonic_solids_2.addAction(self.action_Cube)
        self.menu_Platonic_solids_2.addAction(self.action_CubeQuad)
        self.menu_Platonic_solids_2.addAction(self.action_Octahedron)
        self.menu_Platonic_solids_2.addAction(self.action_Dodecahedron)
        self.menu_Platonic_solids_2.addAction(self.action_Icosahedron)
        self.menu_Geodesic_domes_2.addAction(self.actionFrom_Tetrahedron_2)
        self.menu_Geodesic_domes_2.addAction(self.actionFrom_Tetrahedron_4)
        self.menu_Geodesic_domes_2.addAction(self.actionFrom_Octahedron_2)
        self.menu_Geodesic_domes_2.addAction(self.actionFrom_Octahedron_4)
        self.menu_Geodesic_domes_2.addAction(self.actionFrom_Icosahedron_2)
        self.menu_Geodesic_domes_2.addAction(self.actionFrom_Icosahedron_4)
        self.menu_Rendering.addAction(self.actionDisplay_edges)
        self.menu_Rendering.addAction(self.action_Color_mode)
        self.menu_Rendering.addAction(self.actionInteractive)
        self.menu_Rendering.addSeparator()
        self.menu_Rendering.addAction(self.actionZoom_In)
        self.menu_Rendering.addAction(self.actionZoom_Out)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Rendering.menuAction())
        self.menubar.addAction(self.menu_Platonic_solids_2.menuAction())
        self.menubar.addAction(self.menu_Geodesic_domes_2.menuAction())
        self.menubar.addAction(self.menu_Objects.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

