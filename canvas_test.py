import sys

import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("グラフ")
        self.setGeometry(300, 300, 500, 500)

        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        # We want the axes cleared every time plot() is called

        self.canvas = FigureCanvas(self.figure)
        self.canvas.move(0, 0)

        self.toolbar = NavigationToolbar(self.canvas, self)
        # self.toolbar.hide()

        # Just some button 
        self.button1 = QtWidgets.QPushButton('Plot', self)
        self.button1.clicked.connect(self.plot)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        btnlayout = QtWidgets.QHBoxLayout()
        btnlayout.addWidget(self.button1)
        qw = QtWidgets.QWidget(self)
        qw.setLayout(btnlayout)
        layout.addWidget(qw)

        self.setLayout(layout)

    def plot(self):
        x1 = np.arange(0, 4 * np.pi, 0.1)
        y1 = np.sin(x1)
        self.axes.plot(x1, y1, c="r", label="sin")
        self.axes.legend(loc="best")
        self.canvas.draw()

        x2 = np.arange(0, 4 * np.pi, 0.1)
        y2 = np.cos(x2)
        self.axes.plot(x2, y2, c="b", label="cos")
        self.axes.legend(loc="best")
        self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.setWindowTitle('Simple QTpy and MatplotLib example with Zoom/Pan')
    main.show()

    sys.exit(app.exec_())
