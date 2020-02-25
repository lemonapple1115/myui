import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, \
    QTextEdit


class LayerFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.layer_info = LayerInfo()

    def init_ui(self):
        self._layer_label = QLabel('Layer Type')
        self._cb1 = QCheckBox('&input layer')
        self._cb2 = QCheckBox('&hidden layer')
        self._cb3 = QCheckBox('o&utput layer')
        self._ac_fn_label = QLabel('Activation Function')
        self._ac_fn_editor = QTextEdit()
        self._neurons_number_label = QLabel('Neurons Number')
        self._neurons_number_editor = QLineEdit()
        self._edit_btn = QPushButton('&edit')
        self._lock_btn = QPushButton('&ok')
        layout = QHBoxLayout()
        cb_layout = QVBoxLayout()
        fn_layout = QVBoxLayout()
        neurons_num_edit_layout = QVBoxLayout()
        cb_layout.addWidget(self._layer_label)
        cb_layout.addWidget(self._cb1)
        cb_layout.addWidget(self._cb2)
        cb_layout.addWidget(self._cb3)
        fn_layout.addWidget(self._ac_fn_label)
        fn_layout.addWidget(self._ac_fn_editor)
        neurons_num_edit_layout.addWidget(self._neurons_number_label)
        neurons_num_edit_layout.addWidget(self._neurons_number_editor)
        neurons_num_edit_layout.addWidget(self._edit_btn)
        neurons_num_edit_layout.addWidget(self._lock_btn)
        layout.addLayout(cb_layout)
        layout.addLayout(fn_layout)
        layout.addLayout(neurons_num_edit_layout)
        self.setLayout(layout)

        self._cb1.clicked.connect(lambda x: self.set_exclusive_check_boxes(1))
        self._cb2.clicked.connect(lambda x: self.set_exclusive_check_boxes(2))
        self._cb3.clicked.connect(lambda x: self.set_exclusive_check_boxes(3))
        self._lock_btn.clicked.connect(lambda x: self.has_locked_layer_info_widgets(True))
        self._edit_btn.clicked.connect(lambda x: self.has_locked_layer_info_widgets(False))

    @pyqtSlot()
    def set_exclusive_check_boxes(self, box_id):
        self.layer_info.set_layer_type(box_id)
        if box_id == 1:
            self._cb1.setChecked(True)
            self._cb2.setChecked(False)
            self._cb3.setChecked(False)
        if box_id == 2:
            self._cb1.setChecked(False)
            self._cb2.setChecked(True)
            self._cb3.setChecked(False)
        if box_id == 3:
            self._cb1.setChecked(False)
            self._cb2.setChecked(False)
            self._cb3.setChecked(True)

    @pyqtSlot()
    def has_locked_layer_info_widgets(self, has_locked):
        self._cb1.setEnabled(not has_locked)
        self._cb2.setEnabled(not has_locked)
        self._cb3.setEnabled(not has_locked)
        self._ac_fn_editor.setEnabled(not has_locked)
        self._neurons_number_editor.setEnabled(not has_locked)
        self._edit_btn.setEnabled(has_locked)
        self._lock_btn.setEnabled(not has_locked)

        # only save layer info when clicked button 'ok'
        if has_locked:
            self.save_layer_info()

    def save_layer_info(self):
        self.layer_info.set_layer_ac_fn(self._ac_fn_editor.toPlainText())
        # [todo] input non number would cause an error
        self.layer_info.set_neurons_num(int(self._neurons_number_editor.text()))


class LayerInfo:
    def __init__(self):
        self.layer_type = ''
        self.activation_function = ''
        self.neurons_number = 0

    def set_layer_type(self, layer_type_index):
        layer_types = {1: "input_layer", 2: "hidden_layer", 3: 'output_layer'}
        self.layer_type = layer_types.get(layer_type_index)
        print(self.layer_type)

    def set_layer_ac_fn(self, layer_ac_fn):
        self.activation_function = layer_ac_fn
        print(self.activation_function)

    def set_neurons_num(self, neurons_num):
        self.neurons_number = neurons_num
        print(self.neurons_number)


app = QApplication(sys.argv)
layer_frame = LayerFrame()
layer_frame.show()
app.exec_()