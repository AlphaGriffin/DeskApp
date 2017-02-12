

from __future__ import unicode_literals
import sys
from PyQt5.uic import loadUiType

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


from PyQt5.QtWidgets import (
                             QApplication as app,
                             QLabel,
                             QSizePolicy,
                             )
from PyQt5.QtCore import (
                          Qt,
                          )

#from PyQt5 import QtCore
#from PyQt5 import QtWidgets

#from PyQt5.QtGui import QKeySequence, QPixmap
#from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
#from PyQt5.QtWidgets import QAction, QLabel, QFileDialog, QStackedWidget, QActionGroup, QSizePolicy
#from PyQt5.QtCore import Qt, QTimer, QFileInfo, QEvent, QMargins, pyqtSignal, pyqtSlot


FRONTEND_VERSION = "0.1.0"

#from log import logview

Ui_MainWindow, QMainWindow = loadUiType('src/ui/main_window.ui')
loadUiType('src/ui/main_window.ui')

class DeskApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Params : Options = """
        super(DeskApp, self).__init__()
        self.setupUi(self)
        
        #logview.setParent(self)
        #logview.setWindowFlags(Qt.Dialog)
        
        self.statusbar_label = QLabel()
        self.statusbar_label.setIndent(2)
        self.statusbar_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        self.statusbar.addPermanentWidget(self.statusbar_label, 1)
        self.status_msg("- AlphaGriffin DeskApp - version {}.".format(FRONTEND_VERSION))
        
        
    def status_msg(self,msg):
        """alert user of changes in statusbar"""
        self.statusbar_label.setText(msg)
        return msg

    def center_widget(self):
        """Centers widget on desktop."""
        size = self.size()
        desktop = app.desktop()
        width, height = size.width(), size.height()
        dwidth, dheight = desktop.width(), desktop.height()
        cw, ch = (dwidth/2)-(width/2), (dheight/2)-(height/2)
        self.move(cw, ch)

    def connect_signals(self):
        """Connects signals."""
        

#class Main(QMainWindow, Ui_MainWindow):
#    def __init__(self, ):
#        super(Main, self).__init__()
#        self.setupUi(self)
#        
#        # add first plot
#        self.add_plot()
#        
#    def add_plot(self):
#        fig1 = Figure()
#        ax1f1 = fig1.add_subplot(111)
#        ax1f1.plot(np.random.rand(5))
#        self.graph_win = FigureCanvas(fig1)
#        #self.mplvl(self.canvas)
#        self.graph_win.draw()

if __name__ == '__main__':
        
    app = app(sys.argv)
    main = DeskApp()
    main.show()
    sys.exit(app.exec_())